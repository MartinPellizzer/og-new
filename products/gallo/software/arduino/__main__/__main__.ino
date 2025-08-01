#include "RTClib.h"
RTC_DS3231 rtc_lib;

#include <EEPROM.h>
#define EEPROM_SIZE 1024

#define CALENDAR_TIMERS_NUM 9

int32_t calendar_times[7][CALENDAR_TIMERS_NUM][2] = {
  {{-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}},
  {{-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}},
  {{-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}},
  {{-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}},
  {{-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}},
  {{-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}},
  {{-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}}
};

int8_t calendar_onoff_old = -2;
int8_t calendar_onoff_tmp = 0;
int8_t calendar_onoff_cur = 0;

int8_t cycle_i = -2;
int8_t day_of_week_old = -2;
int8_t day_of_week_cur = 0;

int32_t hour_from_old = -2;
int32_t hour_from_tmp = 0;
int32_t hour_from_cur = 0;
int32_t minute_from_old = -2;
int32_t minute_from_tmp = 0;
int32_t minute_from_cur = 0;

int32_t hour_to_old = -2;
int32_t hour_to_tmp = 0;
int32_t hour_to_cur = 0;
int32_t minute_to_old = -2;
int32_t minute_to_tmp = 0;
int32_t minute_to_cur = 0;




///////////////////////////////////////////////////////////////////////
// ;rtc
///////////////////////////////////////////////////////////////////////
typedef struct rtc_t 
{
  int16_t hour_old = -1;
  int32_t hour_tmp = 0;
  int16_t hour_cur = 0;
  int16_t minute_old = -1;
  int32_t minute_tmp = 0;
  int16_t minute_cur = 0;
  int32_t second_old = -1;
  int32_t second_tmp = 0;
  int32_t second_cur = 0;

  int16_t year_old = -1;
  int16_t year_tmp = 0;
  int16_t year_cur = 0;
  int16_t month_old = -1;
  int16_t month_tmp = 0;
  int16_t month_cur = 0;
  int16_t day_old = -1;
  int16_t day_tmp = 0;
  int16_t day_cur = 0;

  int16_t day_week_cur;
  int16_t day_week_old;
} rtc_t;
rtc_t rtc = {};
DateTime now_cur;
DateTime now_old;

///////////////////////////////////////////////////////////////////////
// ;power
///////////////////////////////////////////////////////////////////////
#define POWER_TYPE_PIN 15
typedef struct power_t {
  int8_t power_old = -1;
  int8_t power_tmp = 50;
  int8_t power_cur = 50;
  int8_t power_type_old = -2;
  int8_t power_type_tmp = 0;
  int8_t power_type_cur = 0;
} power_t;
power_t power = {};

///////////////////////////////////////////////////////////////////////
// ;sensor
///////////////////////////////////////////////////////////////////////
#define SENSOR1_RE_DE_PIN 16
HardwareSerial Sensor1(1);
#define BUFF_LEN 9
uint8_t buff[BUFF_LEN] = { 0 };
uint8_t i = 0;
uint8_t sensor_new_data = 0;
uint32_t timer = 0;
uint32_t timer_no_signal = 0;
uint32_t sensor_connected_millis = 0;
int sensor_connected_seconds = 0;
typedef struct sensor_t {
  int16_t ppb_old = -2;
  int16_t ppb_cur = -1;
  int8_t is_connected = 0;
} sensor_t;
sensor_t sensor = {};

int is_on_old = -1;
int is_on_cur = 0;
uint32_t cycle_millis_cur = 0;
uint32_t cycle_working_millis_cur = 0;
int8_t cycle_on_old = -1;
int8_t cycle_on_cur = 0;
int8_t cycle_working_state_cur = 0;
uint32_t cycle_working_seconds = 0;
// #define relay_pin 5
#define relay_pin 12

///////////////////////////////////////////////////////////////////////
// ;nextion
///////////////////////////////////////////////////////////////////////
const uint8_t BUFFER_SIZE = 20;
typedef struct nextion_t {  
  uint8_t inputs_buff[BUFFER_SIZE];
  uint8_t bytestream_receiving = 0;
  uint32_t bytestream_millis = 0;
  uint32_t bytestream_buff_index = 0;
  int16_t page_old = -1;
  int16_t page_cur = 0;
} nextion_t;
nextion_t nextion = {};


void cycle_update() 
{
  int32_t cycle_seconds_base = 1000 * 60 * 30;
  if (is_on_cur)
  {
    if (millis() - cycle_millis_cur > 1000) 
    {
      cycle_millis_cur = millis();

      bool found = false;
      if (calendar_onoff_cur == 1)
      {
        int32_t rtc_seconds_tot = (rtc.hour_cur * 3600) + (rtc.minute_cur * 60) + (rtc.second_cur);
        for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
        {
          if (rtc_seconds_tot > calendar_times[rtc.day_week_cur][j][0] && rtc_seconds_tot < calendar_times[rtc.day_week_cur][j][1])
          {
            found = true;
          }
        }
      }
      else
      {
        found = true;
      }

      if (found == true)
      {
        cycle_on_cur = 1;
        if (cycle_on_old != cycle_on_cur)
        {
          cycle_on_old = cycle_on_cur;
          cycle_working_state_cur = 1;
          digitalWrite(relay_pin, 1);
          cycle_working_millis_cur = millis();
          cycle_working_seconds = int(cycle_seconds_base * (float(power.power_cur) / float(100)));
          // Serial.println(cycle_working_seconds);
        }
      }
      else 
      {
        cycle_on_cur = 0;
        if (cycle_on_old != cycle_on_cur)
        {
          cycle_on_old = cycle_on_cur;
          cycle_working_state_cur = 0;
          digitalWrite(relay_pin, 0);
          cycle_working_millis_cur = millis();
        }
      }

      if (cycle_on_cur == 1)
      {
        if (cycle_working_state_cur == 1)
        {
          if (millis() - cycle_working_millis_cur > cycle_working_seconds) 
          {
            cycle_working_millis_cur = millis();
            cycle_working_state_cur = 0;
            digitalWrite(relay_pin, 0);
          }
        }
        else
        {
          if (millis() - cycle_working_millis_cur > cycle_seconds_base) 
          {
            cycle_working_millis_cur = millis();
            cycle_working_state_cur = 1;
            digitalWrite(relay_pin, 1);
            cycle_working_seconds = int(cycle_seconds_base * (float(power.power_cur) / float(100)));
          }
        }
      }
      else
      {
        cycle_on_cur = 0;
        cycle_working_state_cur = 0;
        digitalWrite(relay_pin, 0);
      }
    }
  }
  else
  {
    cycle_on_cur = 0;
    cycle_on_old = cycle_on_cur;
    cycle_working_state_cur = 0;
    digitalWrite(relay_pin, 0);
    cycle_working_millis_cur = millis();
  }
}

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);

  Sensor1.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI
  pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  digitalWrite(SENSOR1_RE_DE_PIN, LOW);

  pinMode(POWER_TYPE_PIN, INPUT_PULLUP);

  pinMode(relay_pin, OUTPUT);
  
  EEPROM.begin(EEPROM_SIZE);
  
  // power
  int address = 10;
  int eeprom_power = EEPROM.read(address);
  if (eeprom_power == 255)
  {
    power.power_cur = 50;
  }
  else
  {
    power.power_cur = eeprom_power;
  }

  for (int i = 0; i < 7; i++)
  {
    for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
    {
      int address_1 = 100 + (i*100) + (j*10) + 0;
      int32_t hour_from_tmp = EEPROM.read(address_1);
      int address_2 = 100 + (i*100) + (j*10) + 1;
      int32_t minute_from_tmp = EEPROM.read(address_2);
      int address_3 = 100 + (i*100) + (j*10) + 2;
      int32_t hour_to_tmp = EEPROM.read(address_3);
      int address_4 = 100 + (i*100) + (j*10) + 3;
      int32_t minute_to_tmp = EEPROM.read(address_4);

      if (hour_from_tmp == 255)
      {
        calendar_times[i][j][0] = -1;
        calendar_times[i][j][1] = -1;
      }
      else
      {
        int32_t seconds_from = (hour_from_tmp * 3600) + (minute_from_tmp * 60);
        int32_t seconds_to = (hour_to_tmp * 3600) + (minute_to_tmp * 60);
        calendar_times[i][j][0] = seconds_from;
        calendar_times[i][j][1] = seconds_to;
      }
    }
  }

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

  delay(3000);
  nextion.page_cur = 1;
  Serial.println("setup");
}

void loop() 
{
  // ;debug
  // Serial.println(digitalRead(POWER_TYPE_PIN));

  // ;rtc
  rtc_manager();

  // ;sensor
  sensor_update();

  // ;cycle
  cycle_update();

  // ;nextion
  nextion_inputs();
  nextion_update();
}
