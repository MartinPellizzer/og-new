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
typedef struct power_t {
  int8_t power_old = -1;
  int8_t power_tmp = 50;
  int8_t power_cur = 50;
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


unsigned char checksum(unsigned char *i, unsigned char ln) {
  unsigned char j, tempq = 0;
  i += 1;
  for (j = 0; j < (ln - 2); j++) {
    tempq += *i;
    i++;
  }
  tempq = (~tempq) + 1;
  return (tempq);
}


void clear_buffer(uint8_t buff[], uint8_t len) 
{
  for (int i = 0; i < len; i++) buff[i] = 0;
}

void sensor_update() 
{
  // check if sensor is connected, otherwise update state/val
  if (sensor.is_connected == 1) 
  {
    if (millis() - sensor_connected_millis > 1000) 
    {
      sensor_connected_millis = millis();
      sensor_connected_seconds += 1;
      if (sensor_connected_seconds > 5)
      {
        sensor.is_connected = 0;
        sensor.ppb_old = -2;
        sensor.ppb_cur = -1;
      }
    }
  }

  if (sensor_new_data) 
  {
    if (millis() - timer > 40) 
    {
      timer_no_signal = millis();
      i = 0;
      sensor_new_data = 0;
      sensor.ppb_cur = 0;
      if (checksum(buff, 9) == buff[8]) 
      {
        sensor.ppb_cur = buff[4] * 256 + buff[5];
        sensor_connected_millis = millis();
        sensor_connected_seconds = 0;
        sensor.is_connected = 1;
        Serial.println(sensor.ppb_cur);
      }
      clear_buffer(buff, BUFF_LEN);
    }
  }
  if (Sensor1.available() > 0) 
  {
    uint8_t c = Sensor1.read();
    // Serial.println(c);
    buff[i] = c;
    i++;
    sensor_new_data = 1;
    timer = millis();
  }
}

uint8_t get_eeprom_address_calendar(int day_i, int time_i, int offset)
{
  uint8_t eeprom_address = 100 + (day_i*CALENDAR_TIMERS_NUM) + (time_i*4) + offset;
  return eeprom_address;
}

void rtc_manager() {
  now_cur = rtc_lib.now();
  rtc.second_cur = now_cur.second();
  rtc.minute_cur = now_cur.minute();
  rtc.hour_cur = now_cur.hour();
  rtc.day_week_cur = now_cur.dayOfTheWeek();

  rtc.year_cur = now_cur.year();
  rtc.month_cur = now_cur.month();
  rtc.day_cur = now_cur.day();
}

void cycle_update() 
{
  int32_t cycle_seconds_base = 1000 * 60 * 30;
  if (is_on_cur)
  {
    if (millis() - cycle_millis_cur > 1000) 
    {
      cycle_millis_cur = millis();
      int32_t rtc_seconds_tot = (rtc.hour_cur * 3600) + (rtc.minute_cur * 60) + (rtc.second_cur);
      bool found = false;
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
      {
        if (rtc_seconds_tot > calendar_times[rtc.day_week_cur][j][0] && rtc_seconds_tot < calendar_times[rtc.day_week_cur][j][1])
        {
          found = true;
        }
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
          Serial.println(cycle_working_seconds);
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
