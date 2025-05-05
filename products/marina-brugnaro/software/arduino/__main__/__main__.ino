// TODO: maybe do mass reset on eeprom the first start of a new board, to clear all memory (make 0 byte at 123 to check if it's first run or not)

#include "RTClib.h"
RTC_DS3231 rtc_lib;

#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include <EEPROM.h>
#define EEPROM_SIZE 1024

const uint8_t BUFFER_SIZE = 20;

const int CALENDAR_TIMERS_NUM = 16;
const int CALENDAE_DAYS_NUM = 7;
int32_t calendar_days[CALENDAE_DAYS_NUM][CALENDAR_TIMERS_NUM] = {
  { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 },
  { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 },
  { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 },
  { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 },
  { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 },
  { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 },
  { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 },
};

int nextion_calendar_state_old = -1;
int nextion_calendar_state_cur = -1;

bool new_data = false;
unsigned long nextion_current_millis = 0;
int buffer_counter = 0;

int page_old = -1;
int page_current = 0;

int day_old = -1;
int day_curr = 0;

const int relay_pin = 12;

int32_t cycle_seconds_tmp = 0;
int32_t cycle_seconds_curr = 0;
int32_t cycle_second_old = -1;



// ON OFF
bool is_on_old = -1;
bool is_on_cur = 1;


// O3
bool ozone_on = false;
uint32_t ozone_on_current_millis = 0;
uint32_t ozone_on_timer_millis = 0;
int8_t nextion_ozone_on_old = -1;
int8_t nextion_ozone_on_cur = 0;

// yesterday
const uint8_t YESTERDAY_BUFF_NUM = 24;
typedef struct yesterday_t 
{
  int16_t buff[YESTERDAY_BUFF_NUM] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 };
  bool is_buff_updated = false;
  int hour_old = -1;
} yesterday_t;
yesterday_t yesterday = {};

// rtc
typedef struct rtc_t 
{
  int16_t hour_cur;
  int16_t minute_cur;
  int32_t second_cur;
  int32_t second_tmp;
  int32_t second_old;

  int16_t year_cur;
  int16_t year_tmp;
  int16_t year_old;
  int16_t month_cur;
  int16_t month_tmp;
  int16_t month_old;
  int16_t day_tmp;
  int16_t day_cur;
  int16_t day_old;

  int16_t day_week;
} rtc_t;
rtc_t rtc = {};

DateTime now_curr;
DateTime now_old;

//cycle
typedef struct cycle_t {
  int16_t seconds_on_old = -1;
  int16_t seconds_on_tmp = 0;
  int16_t seconds_on_cur = 0;
  int16_t ppb_old = -1;
  int16_t ppb_tmp = 0;
  int16_t ppb_cur = 0;
  int16_t ppb_delta_old = -1;
  int16_t ppb_delta_tmp = 0;
  int16_t ppb_delta_cur = 0;
} cycle_t;
cycle_t cycle = {};

//sd
#define sd_cd 15
uint32_t sd_millis_cur = 0;
typedef struct sd_card_t 
{
  uint8_t state;
  int8_t inserted_old = -1;
  int8_t inserted_cur = 0;
  int8_t tried_to_initialize;
  uint8_t is_initialized = 0;
  uint8_t pin;
  uint8_t pin_cd;
  int16_t minute_cur = -1;
} sd_card_t;
sd_card_t sd_card = {};

//sensor
#define SENSOR1_RE_DE_PIN 16
HardwareSerial Sensor1(1);
#define BUFF_LEN 9
uint8_t buff[BUFF_LEN] = { 0 };
uint8_t i = 0;
uint8_t sensor_new_data = 0;
uint32_t timer = 0;
uint32_t timer_no_signal = 0;
typedef struct sensor_t {
  int16_t ppb_prev;
  int16_t ppb_curr;
  int8_t connected_prev;
  int8_t connected_curr;
  uint32_t connected_millis = 0;
  uint16_t connected_seconds = 0;
} sensor_t;
sensor_t sensor = {};

// ----------------------------------------------------------------------------------------------------------
// ;sd card
// ----------------------------------------------------------------------------------------------------------
File file;
int is_insert = 0;
int is_init = 0;
int sd_val = 123;


void setup() 
{
  pinMode(relay_pin, OUTPUT);

  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);

  /* ;sd */
  sd_card.pin_cd = 15;
  pinMode(sd_card.pin_cd, INPUT);
  
  /* ;sensor */
  sensor.ppb_prev = -1;
  sensor.ppb_curr = 0;

  EEPROM.begin(EEPROM_SIZE);

  // TODO
  for (int day_i = 0; day_i < 7; day_i++)
  {
    for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
    {
      int eeprom_address_hour = 100 + (day_i*100) + (j*2);
      int eeprom_address_minute = 100 + (day_i*100) + (j*2+1);
      int32_t hour = EEPROM.read(eeprom_address_hour);
      int32_t minute = EEPROM.read(eeprom_address_minute);
      if (hour == 255 && minute == 255)
      {
        calendar_days[day_i][j] = -1;
      }
      else
      {
        int32_t seconds = (hour*3600) + (minute*60);
        calendar_days[day_i][j] = seconds;
      }
    }
  }

  int cycle_minutes = EEPROM.read(10);
  cycle.seconds_on_cur = cycle_minutes * 60;
  if (cycle.seconds_on_cur > 10000)
  {
    cycle.seconds_on_cur = 10000;
  }
  int16_t cycle_ppb_1 = EEPROM.read(11) * 10000;
  int16_t cycle_ppb_2 = EEPROM.read(12) * 1000;
  int16_t cycle_ppb_3 = EEPROM.read(13) * 100;
  cycle.ppb_cur = cycle_ppb_1 + cycle_ppb_2 + cycle_ppb_3;
  cycle.ppb_delta_cur = EEPROM.read(14);

  if (0) 
  {
    int eeprom_test_val = EEPROM.read(0);
    Serial.print("EEPROM test val add_0: ");
    Serial.println(eeprom_test_val);
    EEPROM.write(0, eeprom_test_val + 1);
    EEPROM.commit();

    eeprom_test_val = EEPROM.read(100);
    Serial.print("EEPROM test val add_100: ");
    Serial.println(eeprom_test_val);
    EEPROM.write(100, eeprom_test_val + 1);
    EEPROM.commit();

    eeprom_test_val = EEPROM.read(500);
    Serial.print("EEPROM test val add_500: ");
    Serial.println(eeprom_test_val);
    EEPROM.write(500, eeprom_test_val + 1);
    EEPROM.commit();

    eeprom_test_val = EEPROM.read(1000);
    Serial.print("EEPROM test val add_1000: ");
    Serial.println(eeprom_test_val);
    EEPROM.write(1000, eeprom_test_val + 1);
    EEPROM.commit();
  }

  Sensor1.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI
  pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  digitalWrite(SENSOR1_RE_DE_PIN, LOW);

  if (!rtc_lib.begin()) 
  {
    Serial.println("Couldn't find RTC");
    Serial.flush();
    while (1) delay(10);
  }
  if (rtc_lib.lostPower()) 
  {
    Serial.println("RTC lost power, let's set the time!");
    rtc_lib.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }

  rtc.second_old = -1;
  rtc.year_old = -1;
  rtc.month_old = -1;
  rtc.day_old = -1;

  // rtc_lib.adjust(DateTime(F(__DATE__), F(__TIME__)));

  delay(3000);
  page_current = 1;
}


void loop() 
{
  // input
  sensor_input();

  // update

  sd_manager_2();

  /* ;rtc */
  rtc_manager();

  cycle_update();


  yesterday_update();

  nextion_manage();

}
