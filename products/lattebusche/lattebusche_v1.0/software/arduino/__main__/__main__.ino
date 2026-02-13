// TODO: fai in modo che la lettura di un giorno non possa essere inferiore o uguale come tempistica
//       dalla ultima lettura del giorno stesso (se succede ce un problema, forse rtc da reimpostare)
//       aggiungi codice errore: es. E4
// TODO: fai medie per ora (colonna di destra)
// TODO: dai un occhiata a sensore (delle volte smette di segnare quando riavvio scheda principale con bottone EN)
// TODO: completa la homepage, lascia solo dati rilevanti per lattebusche (no potenza generatore, segnale esterno, ecc...)

#include "RTClib.h"
RTC_DS3231 rtc_lib;

#include "FS.h"
#include "SD.h"
#include "SPI.h"

#include <EEPROM.h>
#define EEPROM_SIZE 1024

#define RO_1 12

typedef struct core_t 
{
  uint8_t placeholder = 0;
} core_t;
core_t core = {};






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
} power_t;
power_t power = {};

///////////////////////////////////////////////////////////////////////
// ;cycle
///////////////////////////////////////////////////////////////////////

typedef struct cycle_t {
  int8_t  state_working_old = -2;
  int8_t  state_working_cur = -1;
  int8_t  state_on_old = -2;
  int8_t  state_on_cur = -1;
  int32_t millis_cur = 0;
  int32_t working_millis_timer = 0;
  int32_t resting_millis_timer = 10*1000;
  int8_t  mode_old = -2;
  int8_t  mode_tmp = -1;
  int8_t  mode_cur = 0;
} cycle_t;
cycle_t cycle = {};

// enum Cycle {
//   OXY_01,
//   O3_01,
//   OXY_02,
//   O3_02,
//   OFF_O3,
//   OFF_OXY
// };

// enum Cycle cycle_state;

enum Nextion_Pages {
  P_SPLASH,
  P_HOME,
  P_PASSWORD,
  P_SD,
  P_SET,
  P_POWER,
  P_CAL_EN,
  P_CAL_TIME,
  P_CAL_ADD,
  P_CAL_DEL,
  P_CAL_ADD_ERR_NEG,
  P_CAL_ADD_ERR_OVR,
  P_CLK,
  P_CLK_DATE,
  P_CLK_TIME,
  P_EXT,
  P_SENSOR_ALARM,
  P_OZONE_ALARM,
  P_TEMPERATURE_ALARM,
  P_TEMPERATURE,
  P_SENSOR_OZONE,
};

///////////////////////////////////////////////////////////////////////
// ;O3 sensor internal alarm
///////////////////////////////////////////////////////////////////////
// typedef struct o3_sensor_alarm_t {
//   int8_t enable_old = -2;
//   int8_t enable_tmp = -1;
//   int8_t enable_cur = 1;
//   int16_t ppb_old = -2;
//   int16_t ppb_cur = -1;
//   uint32_t millis1_cur = 0;
//   uint32_t millis2_cur = 0;
//   int16_t ppb_alarm_old = -2;
//   int16_t ppb_alarm_tmp = -2;
//   int16_t ppb_alarm_cur = 100;
//   int16_t alarm_timer_minutes_old = -2;
//   int16_t alarm_timer_minutes_tmp = -2;
//   int16_t alarm_timer_minutes_cur = 2;
//   int8_t is_over_max_old = -2;
//   int8_t is_over_max_cur = 0;
//   int8_t is_alarm_old = -2;
//   int8_t is_alarm_cur = 0;
//   int32_t alarm_millis_cur = 0;
  
// } o3_sensor_alarm_t;
// o3_sensor_alarm_t o3_sensor_alarm = {};

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
  int16_t target_ppb_old = -2;
  int16_t target_ppb_tmp = -1;
  int16_t target_ppb_cur = 100;
  int8_t delta_perc_old = -2;
  int8_t delta_perc_tmp = -1;
  int8_t delta_perc_cur = 20;
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

///////////////////////////////////////////////////////////////////////
// ;external input (signal to abilitate cycle)
///////////////////////////////////////////////////////////////////////
// typedef struct external_input_t {  
//   int8_t state_old = -2;
//   int8_t state_cur = -1;
//   int8_t is_abilitated_old = -2;
//   int8_t is_abilitated_tmp = -1;
//   int8_t is_abilitated_cur = 0;
// } external_input_t;
// external_input_t external_input = {};

typedef struct mode_2_t {  
  int8_t state_old = -2;
  int8_t state_cur = -1;
  int8_t is_abilitated_old = -2;
  int8_t is_abilitated_tmp = -1;
  int8_t is_abilitated_cur = 0;
} mode_2_t;
mode_2_t external_input = {};

// typedef struct mode_t {
//   int8_t state_old = -2;
//   int8_t state_cur = -1;
//   int8_t is_abilitated_old = -2;
//   int8_t is_abilitated_tmp = -1;
//   int8_t is_abilitated_cur = 0;
// } mode_t;
// mode_t mode = {};


///////////////////////////////////////////////////////////////////////
// ;sensor temperature
///////////////////////////////////////////////////////////////////////
// typedef struct sensor_temperature_t {  
//   int8_t state_old = -2;
//   int8_t state_cur = -1;
//   int32_t alarm_millis_cur = 0;
//   int8_t enable_old = -2;
//   int8_t enable_tmp = -1;
//   int8_t enable_cur = 1;
//   int8_t alarm_seconds_old = -2;
//   int8_t alarm_seconds_tmp = -1;
//   int8_t alarm_seconds_cur = 5;
// } sensor_temperature_t;
// sensor_temperature_t sensor_temperature = {};

///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
#define PASSWORD_DIGITS_NUM 8
typedef struct password_t {
  int8_t digits_old[PASSWORD_DIGITS_NUM] = {-2, -2, -2, -2, -2, -2, -2, -2};
  int8_t digits_cur[PASSWORD_DIGITS_NUM] = {-1, -1, -1, -1, -1, -1, -1, -1};
  int8_t digits_password[PASSWORD_DIGITS_NUM] = {1, 2, 3, 4, -1, -1, -1, -1};
  int8_t password_errata_old = -1;
  int8_t password_errata_cur = 0;
  int8_t digit_counter = 0;
} password_t;
password_t password = {};


///////////////////////////////////////////////////////////////////////
// ;sd
///////////////////////////////////////////////////////////////////////
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
  uint8_t nextion_update = 0;
  uint8_t demo_val = 0;
  uint32_t demo_val_millis_cur = 0;
  uint32_t demo_val_millis_tmr = 1000;
  
  uint8_t second_old = -2;
  uint8_t second_cur = 0;
  uint8_t buff_minute_old = -2;
  uint8_t buff_minute_cur = 0;
  uint8_t buff_hour_old = -2;
  uint8_t buff_hour_cur = 0;
} sd_card_t;
sd_card_t sd_card = {};


#define LINES 10
#define LINE_SIZE 30+1

uint16_t sd_hour_buff[60] = {0};
uint8_t sd_hour_buff_i = 0;

char sd_minute_line_cur_buff[LINE_SIZE] = {0};
char sd_minute_nextion_lines_buff[LINES][LINE_SIZE] = {0};
char sd_hour_nextion_lines_buff[LINES][LINE_SIZE] = {0};

#define MAX_LINE_LENGTH 64
#define MAX_FIELDS 10

char lastRow[MAX_LINE_LENGTH];
char *fields[MAX_FIELDS];
int fieldCount = 0;

// ----------------------------------------------------------------------------------------------------------
// ;sd card
// ----------------------------------------------------------------------------------------------------------
File file;
int is_insert = 0;
int is_init = 0;
int sd_val = 123;



void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);

  Sensor1.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI
  pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  digitalWrite(SENSOR1_RE_DE_PIN, LOW);

  /* ;sd */
  sd_card.pin_cd = 15;
  pinMode(sd_card.pin_cd, INPUT);

  // pinMode(RI_1, INPUT_PULLUP);
  // pinMode(RI_2, INPUT_PULLUP);

  pinMode(RO_1, OUTPUT);
  digitalWrite(RO_1, 0);
  
  EEPROM.begin(EEPROM_SIZE);
  
  // power
  int address = 10;
  int eeprom_power = EEPROM.read(address);
  if (eeprom_power == 255)
  {
    power.power_cur = 1;
  }
  else
  {
    power.power_cur = eeprom_power;
  }

  eeprom_init();

  // while (1) delay(10);

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

  bool rtc_init_success = false;
  for (int i = 0; i < 10; i++)
  {
    if (!rtc_lib.begin()) 
    {
      Serial.print("RTC INIT ATTEMPT ");
      Serial.print(i);
      Serial.println(": FAILED");
      Serial.flush();
      delay(1000);
    }
    else
    {
      Serial.print("RTC INIT ATTEMPT ");
      Serial.print(i);
      Serial.println(": SUCCES");
      rtc_init_success = true;
      break;
    }
  }
  if (!rtc_init_success)
  {
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


#define MAX_LINES 10
#define MAX_LINE_LENGTH 128

char lastLines[MAX_LINES][MAX_LINE_LENGTH];
int lineCount = 0;
int storedLines = 0;




void loop() 
{
  // external_input.state_cur = digitalRead(RI_1);
  
  debug_manager();

  sensor_ozone_manager();
  // sensor_ozone_alarm_manager();
  // sensor_temperature_manager();

  // ;cycle
  cycle_manager();

  // ;rtc
  rtc_manager();

  // ;nextion
  nextion_manager();

  // ;sd
  sd_manager();

  // ;valves
  // valves_manager();

  // if (millis() - sd_card.demo_val_millis_cur > sd_card.demo_val_millis_tmr) 
  // {
  //   sd_card.demo_val_millis_cur = millis();
  //   sd_card.demo_val = (sd_card.demo_val + 1) % 10;
  //   sd_card.nextion_update = 1;
  // }

  if (millis() - sd_card.demo_val_millis_cur > sd_card.demo_val_millis_tmr) 
  {
    sd_card.demo_val_millis_cur = millis();

    if (sd_card.tried_to_initialize)
    {
      // readFile(SD, "/data.csv");
      readLastCSVLinesOrdered(SD, "/data.csv");
    }
    Serial.println();

    sd_card.demo_val = (sd_card.demo_val + 1) % 10;
    // sd_card.nextion_update = 1;
  }

}
