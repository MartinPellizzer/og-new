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

const uint8_t BUFFER_SIZE = 20;
uint8_t buffer_nextion[BUFFER_SIZE];

// home
uint8_t cmd_p_home_on[BUFFER_SIZE] = { 101, 1, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_goto_power_warn[BUFFER_SIZE] = { 101, 1, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_goto_calendar_warn[BUFFER_SIZE] = { 101, 1, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_goto_clock_warn[BUFFER_SIZE] = { 101, 1, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// power
uint8_t cmd_p_power_warn_no[BUFFER_SIZE] = { 101, 6, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_warn_yes[BUFFER_SIZE] = { 101, 6, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_back[BUFFER_SIZE] = { 101, 2, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_save[BUFFER_SIZE] = { 101, 2, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_up[BUFFER_SIZE] = { 101, 2, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_down[BUFFER_SIZE] = { 101, 2, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// calendar
uint8_t cmd_p_calendar_warn_no[BUFFER_SIZE] = { 101, 7, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_warn_yes[BUFFER_SIZE] = { 101, 7, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_goto_calendar[BUFFER_SIZE] = { 101, 1, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_back[BUFFER_SIZE] = { 101, 3, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_day_prev[BUFFER_SIZE] = { 101, 3, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_day_next[BUFFER_SIZE] = { 101, 3, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time0[BUFFER_SIZE] = { 101, 3, 40, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time1[BUFFER_SIZE] = { 101, 3, 32, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time2[BUFFER_SIZE] = { 101, 3, 33, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time3[BUFFER_SIZE] = { 101, 3, 34, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time4[BUFFER_SIZE] = { 101, 3, 35, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time5[BUFFER_SIZE] = { 101, 3, 36, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time6[BUFFER_SIZE] = { 101, 3, 37, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time7[BUFFER_SIZE] = { 101, 3, 38, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time8[BUFFER_SIZE] = { 101, 3, 39, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_back[BUFFER_SIZE] = { 101, 8, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_save[BUFFER_SIZE] = { 101, 8, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_from_hour_up[BUFFER_SIZE] = { 101, 8, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_from_hour_down[BUFFER_SIZE] = { 101, 8, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_from_minute_up[BUFFER_SIZE] = { 101, 8, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_from_minute_down[BUFFER_SIZE] = { 101, 8, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_to_hour_up[BUFFER_SIZE] = { 101, 8, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_to_hour_down[BUFFER_SIZE] = { 101, 8, 12, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_to_minute_up[BUFFER_SIZE] = { 101, 8, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_to_minute_down[BUFFER_SIZE] = { 101, 8, 13, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_err_ok[BUFFER_SIZE] = { 101, 10, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_err2_ok[BUFFER_SIZE] = { 101, 11, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_del_no[BUFFER_SIZE] = { 101, 9, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_del_yes[BUFFER_SIZE] = { 101, 9, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// clock
uint8_t cmd_p_calendar_clock_no[BUFFER_SIZE] = { 101, 12, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_clock_yes[BUFFER_SIZE] = { 101, 12, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_back[BUFFER_SIZE] = { 101, 4, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date[BUFFER_SIZE] = { 101, 4, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time[BUFFER_SIZE] = { 101, 4, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_back[BUFFER_SIZE] = { 101, 13, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_save[BUFFER_SIZE] = { 101, 13, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_year_up[BUFFER_SIZE] = { 101, 13, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_year_down[BUFFER_SIZE] = { 101, 13, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_month_up[BUFFER_SIZE] = { 101, 13, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_month_down[BUFFER_SIZE] = { 101, 13, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_day_up[BUFFER_SIZE] = { 101, 13, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_day_down[BUFFER_SIZE] = { 101, 13, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_back[BUFFER_SIZE] = { 101, 14, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_save[BUFFER_SIZE] = { 101, 14, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_hour_up[BUFFER_SIZE] = { 101, 14, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_hour_down[BUFFER_SIZE] = { 101, 14, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_minute_up[BUFFER_SIZE] = { 101, 14, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_minute_down[BUFFER_SIZE] = { 101, 14, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_second_up[BUFFER_SIZE] = { 101, 14, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_second_down[BUFFER_SIZE] = { 101, 14, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// uint8_t cmd_p_home_goto_analytics[BUFFER_SIZE] = { 101, 1, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
// uint8_t cmd_p_home_goto_onoff[BUFFER_SIZE] = { 101, 1, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// uint8_t cmd_p_analytics_back[BUFFER_SIZE] = { 101, 5, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

bool new_data = false;
unsigned long nextion_current_millis = 0;
int buffer_counter = 0;

int page_old = -1;
int page_current = 0;


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
// ;util
///////////////////////////////////////////////////////////////////////
bool compareArray(uint8_t *a, uint8_t *b) {
  for (uint8_t i = 0; i < BUFFER_SIZE; i++) {
    if (a[i] != b[i]) {
      return false;
    }
  }
  return true;
}

void nextionEvalSerial() {
  if (page_current == 1) {
    if (is_on_cur == 0)
    {
      if (compareArray(cmd_p_home_goto_power_warn, buffer_nextion)) page_current = 10;
      if (compareArray(cmd_p_home_goto_calendar_warn, buffer_nextion)) page_current = 20;
      if (compareArray(cmd_p_home_goto_clock_warn, buffer_nextion)) page_current = 30;
      // if (compareArray(cmd_p_home_goto_analytics, buffer_nextion)) page_current = 40;
      //if (compareArray(cmd_p_home_goto_onoff, buffer_nextion)) page_current = 50;
    }
    if (compareArray(cmd_p_home_on, buffer_nextion))
    {
      if (is_on_cur == 1) is_on_cur = 0;
      else if (is_on_cur == 0) is_on_cur = 1;
    }
  } 
  else if (page_current == 10) 
  {
    if (compareArray(cmd_p_power_warn_no, buffer_nextion)) page_current = 1;
    if (compareArray(cmd_p_power_warn_yes, buffer_nextion)) page_current = 11;
  } 
  else if (page_current == 11) 
  {
    if (compareArray(cmd_p_power_back, buffer_nextion)) 
    {
      power.power_tmp = power.power_cur;
      page_current = 1;
    }
    if (compareArray(cmd_p_power_save, buffer_nextion)) 
    {
      power.power_cur = power.power_tmp;
      page_current = 1;
      
      EEPROM.write(10, power.power_cur);
      EEPROM.commit();
    }
    if (compareArray(cmd_p_power_up, buffer_nextion)) 
    {
      power.power_tmp += 10;
      if (power.power_tmp > 100) power.power_tmp = 100;
    }
    if (compareArray(cmd_p_power_down, buffer_nextion)) 
    {
      power.power_tmp -= 10;
      if (power.power_tmp < 10) power.power_tmp = 10;
    }
  } 

  else if (page_current == 20) 
  {
    if (compareArray(cmd_p_calendar_warn_no, buffer_nextion)) page_current = 1;
    if (compareArray(cmd_p_calendar_warn_yes, buffer_nextion)) page_current = 21;
  } 
  else if (page_current == 21) 
  {
    if (compareArray(cmd_p_calendar_back, buffer_nextion)) page_current = 1;
    if (compareArray(cmd_p_calendar_day_prev, buffer_nextion))
    {
      day_of_week_cur -= 1;
      if (day_of_week_cur < 0) day_of_week_cur = 6;
    }
    if (compareArray(cmd_p_calendar_day_next, buffer_nextion))
    {
      day_of_week_cur += 1;
      if (day_of_week_cur > 6) day_of_week_cur = 0;
    }
    if (compareArray(cmd_p_calendar_time0, buffer_nextion))
    {
      cycle_i = 0;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
    if (compareArray(cmd_p_calendar_time1, buffer_nextion))
    {
      cycle_i = 1;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
    if (compareArray(cmd_p_calendar_time2, buffer_nextion))
    {
      cycle_i = 2;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
    if (compareArray(cmd_p_calendar_time3, buffer_nextion))
    {
      cycle_i = 3;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
    if (compareArray(cmd_p_calendar_time4, buffer_nextion))
    {
      cycle_i = 4;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
    if (compareArray(cmd_p_calendar_time5, buffer_nextion))
    {
      cycle_i = 5;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
    if (compareArray(cmd_p_calendar_time6, buffer_nextion))
    {
      cycle_i = 6;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
    if (compareArray(cmd_p_calendar_time7, buffer_nextion))
    {
      cycle_i = 7;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
    if (compareArray(cmd_p_calendar_time8, buffer_nextion))
    {
      cycle_i = 8;
      int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
      if (time_val == -1)
      {
        page_current = 22;
      }
      else
      {
        page_current = 23;
      }
    }
  } 
  else if (page_current == 22) 
  {
    if (compareArray(cmd_p_calendar_add_back, buffer_nextion)) page_current = 21;
    if (compareArray(cmd_p_calendar_add_save, buffer_nextion)) 
    {
      // ;jump
      int32_t seconds_from = (hour_from_tmp * 3600) + (minute_from_tmp * 60);
      int32_t seconds_to = (hour_to_tmp * 3600) + (minute_to_tmp * 60);

      bool is_time_valid = true;
      if (seconds_from >= seconds_to)
      {
        page_current = 24;
        is_time_valid = false;
      }
      for (int i = 0; i < CALENDAR_TIMERS_NUM; i++)
      {
        int32_t seconds_from_old = calendar_times[day_of_week_cur][i][0];
        int32_t seconds_to_old = calendar_times[day_of_week_cur][i][1];
        if (seconds_from >= seconds_from_old && seconds_from <= seconds_to_old)
        {
          page_current = 25;
          is_time_valid = false;
          break;
        }
        if (seconds_to >= seconds_from_old && seconds_to <= seconds_to_old)
        {
          page_current = 25;
          is_time_valid = false;
          break;
        }
        if (seconds_from <= seconds_from_old && seconds_to >= seconds_to_old)
        {
          page_current = 25;
          is_time_valid = false;
          break;
        }
      }

      if (is_time_valid)
      {
        calendar_times[day_of_week_cur][cycle_i][0] = seconds_from;
        calendar_times[day_of_week_cur][cycle_i][1] = seconds_to;
        Serial.print("CYCLE_I: ");
        Serial.println(cycle_i);
        page_current = 21;

        int address_1 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 0;
        int val = hour_from_tmp;
        EEPROM.write(address_1, val);
        EEPROM.commit();
        int address_2 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 1;
        val = minute_from_tmp;
        EEPROM.write(address_2, val);
        EEPROM.commit();
        int address_3 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 2;
        val = hour_to_tmp;
        EEPROM.write(address_3, val);
        EEPROM.commit();
        int address_4 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 3;
        val = minute_to_tmp;
        EEPROM.write(address_4, val);
        EEPROM.commit();
      }
    }
    if (compareArray(cmd_p_calendar_add_from_hour_up, buffer_nextion)) 
    {
      hour_from_tmp += 1;
      if (hour_from_tmp > 23) hour_from_tmp = 0;
    }
    if (compareArray(cmd_p_calendar_add_from_hour_down, buffer_nextion)) 
    {
      hour_from_tmp -= 1;
      if (hour_from_tmp < 0) hour_from_tmp = 23;
    }
    if (compareArray(cmd_p_calendar_add_from_minute_up, buffer_nextion)) 
    {
      minute_from_tmp += 1;
      if (minute_from_tmp > 59) minute_from_tmp = 0;
    }
    if (compareArray(cmd_p_calendar_add_from_minute_down, buffer_nextion)) 
    {
      minute_from_tmp -= 1;
      if (minute_from_tmp < 0) minute_from_tmp = 59;
    }
    if (compareArray(cmd_p_calendar_add_to_hour_up, buffer_nextion)) 
    {
      hour_to_tmp += 1;
      if (hour_to_tmp > 23) hour_to_tmp = 0;
    }
    if (compareArray(cmd_p_calendar_add_to_hour_down, buffer_nextion)) 
    {
      hour_to_tmp -= 1;
      if (hour_to_tmp < 0) hour_to_tmp = 23;
    }
    if (compareArray(cmd_p_calendar_add_to_minute_up, buffer_nextion)) 
    {
      minute_to_tmp += 1;
      if (minute_to_tmp > 59) minute_to_tmp = 0;
    }
    if (compareArray(cmd_p_calendar_add_to_minute_down, buffer_nextion)) 
    {
      minute_to_tmp -= 1;
      if (minute_to_tmp < 0) minute_to_tmp = 59;
    }
  } 
  else if (page_current == 24) 
  {
    if (compareArray(cmd_p_calendar_add_err_ok, buffer_nextion)) page_current = 22;
  }
  else if (page_current == 25) 
  {
    if (compareArray(cmd_p_calendar_add_err2_ok, buffer_nextion)) page_current = 22;
  }
  else if (page_current == 23) 
  {
    if (compareArray(cmd_p_calendar_del_no, buffer_nextion)) page_current = 21;
    if (compareArray(cmd_p_calendar_del_yes, buffer_nextion))
    {
      int32_t seconds_from = -1;
      int32_t seconds_to = -1;
      calendar_times[day_of_week_cur][cycle_i][0] = seconds_from;
      calendar_times[day_of_week_cur][cycle_i][1] = seconds_to;
      page_current = 21;

      int address_1 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 0;
      int val = 255;
      EEPROM.write(address_1, val);
      EEPROM.commit();
      int address_2 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 1;
      val = 255;
      EEPROM.write(address_2, val);
      EEPROM.commit();
      int address_3 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 2;
      val = 255;
      EEPROM.write(address_3, val);
      EEPROM.commit();
      int address_4 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 3;
      val = 255;
      EEPROM.write(address_4, val);
      EEPROM.commit();
    }
  }
  else if (page_current == 30) 
  {
    if (compareArray(cmd_p_calendar_clock_no, buffer_nextion)) page_current = 1;
    if (compareArray(cmd_p_calendar_clock_yes, buffer_nextion)) page_current = 31;
  } 
  else if (page_current == 31) 
  {
    if (compareArray(cmd_p_clock_back, buffer_nextion)) page_current = 1;
    if (compareArray(cmd_p_clock_date, buffer_nextion))
    {
      page_current = 32;
      rtc.year_tmp = rtc.year_cur;
      rtc.month_tmp = rtc.month_cur;
      rtc.day_tmp = rtc.day_cur;
    }
    if (compareArray(cmd_p_clock_time, buffer_nextion)) page_current = 33;
  }
  else if (page_current == 32) 
  {
    if (compareArray(cmd_p_clock_date_back, buffer_nextion)) page_current = 31;
    if (compareArray(cmd_p_clock_date_save, buffer_nextion)) 
    {
      rtc.year_cur = rtc.year_tmp;
      rtc.month_cur = rtc.month_tmp;
      rtc.day_cur = rtc.day_tmp;
      rtc_lib.adjust(DateTime(rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur, rtc.second_cur));
      page_current = 31;
    }
    if (compareArray(cmd_p_clock_date_year_up, buffer_nextion))
    {
      rtc.year_tmp += 1;
    }
    if (compareArray(cmd_p_clock_date_year_down, buffer_nextion))
    {
      rtc.year_tmp -= 1;
      if (rtc.year_tmp < 2020)
      {
        rtc.year_tmp = 2020;
      }
    }
    if (compareArray(cmd_p_clock_date_month_up, buffer_nextion))
    {
      rtc.month_tmp += 1;
      if (rtc.month_tmp > 12)
      {
        rtc.month_tmp = 12;
      }
    }
    if (compareArray(cmd_p_clock_date_month_down, buffer_nextion))
    {
      rtc.month_tmp -= 1;
      if (rtc.month_tmp < 1)
      {
        rtc.month_tmp = 1;
      }
    }
    if (compareArray(cmd_p_clock_date_day_up, buffer_nextion))
    {
      rtc.day_tmp += 1;
      if (rtc.month_tmp == 1) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 2) {
        if (rtc.day_tmp >= 28) { rtc.day_tmp = 28; }
      }
      if (rtc.month_tmp == 3) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 4) {
        if (rtc.day_tmp >= 30) { rtc.day_tmp = 30; }
      }
      if (rtc.month_tmp == 5) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 6) {
        if (rtc.day_tmp >= 30) { rtc.day_tmp = 30; }
      }
      if (rtc.month_tmp == 7) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 8) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 9) {
        if (rtc.day_tmp >= 30) { rtc.day_tmp = 30; }
      }
      if (rtc.month_tmp == 10) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 11) {
        if (rtc.day_tmp >= 30) { rtc.day_tmp = 30; }
      }
      if (rtc.month_tmp == 12) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
    }
    if (compareArray(cmd_p_clock_date_day_down, buffer_nextion))
    {
      rtc.day_tmp -= 1;
      if (rtc.day_tmp < 1)
      {
        rtc.day_tmp = 1;
      }
    }
  }
  else if (page_current == 33) 
  {
    if (compareArray(cmd_p_clock_time_back, buffer_nextion)) page_current = 31;
    if (compareArray(cmd_p_clock_time_save, buffer_nextion)) 
    {
      rtc.hour_cur = rtc.hour_tmp;
      rtc.minute_cur = rtc.minute_tmp;
      rtc.second_cur = rtc.second_tmp;
      rtc_lib.adjust(DateTime(rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur, rtc.second_cur));
      page_current = 31;
    }
    if (compareArray(cmd_p_clock_time_hour_up, buffer_nextion))
    {
      rtc.hour_tmp += 1;
      if (rtc.hour_tmp > 23)
      {
        rtc.hour_tmp = 23;
      }
    }
    if (compareArray(cmd_p_clock_time_hour_down, buffer_nextion))
    {
      rtc.hour_tmp -= 1;
      if (rtc.hour_tmp > 1)
      {
        rtc.hour_tmp = 1;
      }
    }
    if (compareArray(cmd_p_clock_time_minute_up, buffer_nextion))
    {
      rtc.minute_tmp += 1;
      if (rtc.minute_tmp > 59)
      {
        rtc.minute_tmp = 59;
      }
    }
    if (compareArray(cmd_p_clock_time_minute_down, buffer_nextion))
    {
      rtc.minute_tmp -= 1;
      if (rtc.minute_tmp > 1)
      {
        rtc.minute_tmp = 1;
      }
    }
    if (compareArray(cmd_p_clock_time_second_up, buffer_nextion))
    {
      rtc.second_tmp += 1;
      if (rtc.second_tmp > 59)
      {
        rtc.second_tmp = 59;
      }
    }
    if (compareArray(cmd_p_clock_time_second_down, buffer_nextion))
    {
      rtc.second_tmp -= 1;
      if (rtc.second_tmp > 1)
      {
        rtc.second_tmp = 1;
      }
    }
  }
  else if (page_current == 40) 
  {
    // if (compareArray(cmd_p_analytics_back, buffer_nextion)) page_current = 1;
  }
}

void nextionDebugSerial() 
{
  for (int i = 0; i < BUFFER_SIZE; i++) {
    Serial.print(buffer_nextion[i]);
    Serial.print(" ");
  }
  Serial.println();
}

void nextionClearBuffer() {
  for (int i = 0; i < BUFFER_SIZE; i++) {
    buffer_nextion[i] = 0;
  }
}

void listenNextion() {
  if (Serial2.available()) {
    new_data = true;
    buffer_nextion[buffer_counter] = Serial2.read();
    if (buffer_counter < BUFFER_SIZE) buffer_counter++;
    nextion_current_millis = millis();
  }
  if (new_data) {
    if ((millis() - nextion_current_millis) > 10) {
      new_data = false;
      buffer_counter = 0;
      nextionEvalSerial();

      nextionDebugSerial();
      nextionClearBuffer();
    }
  }
}


////////////////////////////////////////////////
// ;nextion
////////////////////////////////////////////////
void updateNextion() {
  uint8_t force_refresh = 0;
  if (page_old != page_current) {
    page_old = page_current;
    force_refresh = 1;
  }
  /**/ if (page_current == 1)  nextion_update_page_home(force_refresh);
  else if (page_current == 10) nextion_update_page_power_warn(force_refresh);
  else if (page_current == 11) nextion_update_page_power(force_refresh);
  else if (page_current == 20) nextion_update_page_calendar_warn(force_refresh);
  else if (page_current == 21) nextion_update_page_calendar(force_refresh);
  else if (page_current == 22) nextion_update_page_calendar_add(force_refresh);
  else if (page_current == 23) nextion_update_page_calendar_del(force_refresh);
  else if (page_current == 24) nextion_update_page_calendar_add_err(force_refresh);
  else if (page_current == 25) nextion_update_page_calendar_add_err2(force_refresh);
  else if (page_current == 30) nextion_update_page_clock_warn(force_refresh);
  else if (page_current == 31) nextion_update_page_clock(force_refresh);
  else if (page_current == 32) nextion_update_page_clock_date(force_refresh);
  else if (page_current == 33) nextion_update_page_clock_time(force_refresh);
  else if (page_current == 40) nextion_update_page_analytics(force_refresh);
  //else if (page_current == 50) nextion_update_page_onoff(force_refresh);
}

////////////////////////////////////////////////////////
// ;home
////////////////////////////////////////////////////////
void nextion_update_page_home(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x68, 0x6F, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
    sensor.ppb_old = -2;
  }
  
  if (force_refresh || is_on_old != is_on_cur) 
  {
    is_on_old = is_on_cur;
    if (is_on_cur == 1)
    {
      uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x38, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x37, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }

  // sensor
  if (force_refresh || sensor.ppb_old != sensor.ppb_cur) 
  {
    sensor.ppb_old = sensor.ppb_cur;
    if (sensor.ppb_cur == -1) 
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x2D, 0x2D, 0x2E, 0x2D, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      // color
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    } 
    else 
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
        _buffer[9] = (sensor.ppb_cur % 10000 / 1000) + 0x30;
        _buffer[11] = (sensor.ppb_cur % 1000 / 100) + 0x30;
        _buffer[12] = (sensor.ppb_cur % 100 / 10) + 0x30;
        _buffer[13] = (0) + 0x30;
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      // color
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x36, 0x35, 0x35, 0x33, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }

  // clock
  if (force_refresh || rtc.second_old != rtc.second_cur) 
  {
    rtc.second_old = rtc.second_cur;      
    uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x55, 0x4E, 0x20, 0x30, 0x37, 0x2F, 0x30, 0x31, 0x2F, 0x32, 0x30, 0x32, 0x30, 0x20, 0x2D, 0x20, 0x31, 0x30, 0x3A, 0x33, 0x30, 0x3A, 0x33, 0x30, 0x22, 0xff, 0xff, 0xff };
    if (rtc.day_week_cur == 0)
    {
      _buffer[8] = 0x44;
      _buffer[9] = 0x4F;
      _buffer[10] = 0x4D;
    }
    else if (rtc.day_week_cur == 1)
    {
      _buffer[8] = 0x4C;
      _buffer[9] = 0x55;
      _buffer[10] = 0x4E;
    }
    else if (rtc.day_week_cur == 2)
    {
      _buffer[8] = 0x4D;
      _buffer[9] = 0x41;
      _buffer[10] = 0x52;
    }
    else if (rtc.day_week_cur == 3)
    {
      _buffer[8] = 0x4D;
      _buffer[9] = 0x45;
      _buffer[10] = 0x52;
    }
    else if (rtc.day_week_cur == 4)
    {
      _buffer[8] = 0x47;
      _buffer[9] = 0x49;
      _buffer[10] = 0x4F;
    }
    else if (rtc.day_week_cur == 5)
    {
      _buffer[8] = 0x56;
      _buffer[9] = 0x45;
      _buffer[10] = 0x4E;
    }
    else if (rtc.day_week_cur == 6)
    {
      _buffer[8] = 0x53;
      _buffer[9] = 0x41;
      _buffer[10] = 0x42;
    }
    
    _buffer[12] = (rtc.day_cur % 100 / 10) + 0x30;
    _buffer[13] = (rtc.day_cur % 10 / 1) + 0x30;
    _buffer[15] = (rtc.month_cur % 100 / 10) + 0x30;
    _buffer[16] = (rtc.month_cur % 10 / 1) + 0x30;
    _buffer[18] = (rtc.year_cur % 10000 / 1000) + 0x30;
    _buffer[19] = (rtc.year_cur % 1000 / 100) + 0x30;
    _buffer[20] = (rtc.year_cur % 100 / 10) + 0x30;
    _buffer[21] = (rtc.year_cur % 10 / 1) + 0x30;

    _buffer[25] = (rtc.hour_cur % 100 / 10) + 0x30;
    _buffer[26] = (rtc.hour_cur % 10 / 1) + 0x30;
    _buffer[28] = (rtc.minute_cur % 100 / 10) + 0x30;
    _buffer[29] = (rtc.minute_cur % 10 / 1) + 0x30;
    _buffer[31] = (rtc.second_cur % 100 / 10) + 0x30;
    _buffer[32] = (rtc.second_cur % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // power
  if (force_refresh || power.power_old != power.power_cur) 
  {
    power.power_old = power.power_cur;
    if (power.power_cur >= 100)
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (power.power_cur % 1000 / 100) + 0x30;
      _buffer[9] = (power.power_cur % 100 / 10) + 0x30;
      _buffer[10] = (power.power_cur % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (power.power_cur % 100 / 10) + 0x30;
      _buffer[9] = (power.power_cur % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

////////////////////////////////////////////////////////
// ;power
////////////////////////////////////////////////////////
void nextion_update_page_power_warn(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x70, 0x6F, 0x77, 0x65, 0x72, 0x5F, 0x77, 0x61, 0x72, 0x6E, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_power(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x70, 0x6F, 0x77, 0x65, 0x72, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh || power.power_old != power.power_tmp)
  {
    power.power_old = power.power_tmp;
    if (power.power_tmp >= 100)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        _buffer[8] = (power.power_tmp % 1000 / 100) + 0x30;
        _buffer[9] = (power.power_tmp % 100 / 10) + 0x30;
        _buffer[10] = (power.power_tmp % 10 / 1) + 0x30;
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        _buffer[8] = (power.power_tmp % 100 / 10) + 0x30;
        _buffer[9] = (power.power_tmp % 10 / 1) + 0x30;
        Serial2.write(_buffer[i]);
      }
    }
  }
}

////////////////////////////////////////////////////////
// ;calendar
////////////////////////////////////////////////////////
void nextion_update_page_calendar_warn(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x77, 0x61, 0x72, 0x6E, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_calendar(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x65, 0x6E, 0x64, 0x61, 0x72, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // DAY
  if (force_refresh || day_of_week_old != day_of_week_cur)
  {
    day_of_week_old = day_of_week_cur;
    if (day_of_week_cur == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x4F, 0x4D, 0x45, 0x4E, 0x49, 0x43, 0x41, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x55, 0x4E, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 2)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x41, 0x52, 0x54, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 3)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x45, 0x52, 0x43, 0x4F, 0x4C, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 4)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x49, 0x4F, 0x56, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 5)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x45, 0x4E, 0x45, 0x52, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 6)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x41, 0x42, 0x41, 0x54, 0x4F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    
    // calendar times
    for (int i = 0; i < CALENDAR_TIMERS_NUM; i++)
    {
      if (calendar_times[day_of_week_cur][i][0] != -1 && calendar_times[day_of_week_cur][i][1] != -1)
      {
        // icon (+, -)
        {
          int _index = i;
          uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x30, 0xff, 0xff, 0xff };
          _buffer[1] = (_index) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        }
        // text
        {
          int _index = 2*i + 1;
          if (_index < 10)
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index) + 0x30;
            int32_t _second = calendar_times[day_of_week_cur][i][0];
            int32_t _hour = _second / 3600; 
            int32_t _minute = _second % 3600 / 60; 
            _buffer[11] = (_hour % 100 / 10) + 0x30;
            _buffer[12] = (_hour % 10 / 1) + 0x30;
            _buffer[14] = (_minute % 100 / 10) + 0x30;
            _buffer[15] = (_minute % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
          else
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index % 100 / 10) + 0x30;
            _buffer[2] = (_index % 10 / 1) + 0x30;
            int32_t _second = calendar_times[day_of_week_cur][i][0];
            int32_t _hour = _second / 3600; 
            int32_t _minute = _second % 3600 / 60; 
            _buffer[12] = (_hour % 100 / 10) + 0x30;
            _buffer[13] = (_hour % 10 / 1) + 0x30;
            _buffer[15] = (_minute % 100 / 10) + 0x30;
            _buffer[16] = (_minute % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
        }
        {
          int _index = 2*i + 2;
          if (_index < 10)
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index) + 0x30;
            int32_t _second = calendar_times[day_of_week_cur][i][1];
            int32_t _hour = _second / 3600; 
            int32_t _minute = _second % 3600 / 60; 
            _buffer[10] = (_hour % 100 / 10) + 0x30;
            _buffer[11] = (_hour % 10 / 1) + 0x30;
            _buffer[13] = (_minute % 100 / 10) + 0x30;
            _buffer[14] = (_minute % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
          else
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index % 100 / 10) + 0x30;
            _buffer[2] = (_index % 10 / 1) + 0x30;
            int32_t _second = calendar_times[day_of_week_cur][i][1];
            int32_t _hour = _second / 3600; 
            int32_t _minute = _second % 3600 / 60; 
            _buffer[11] = (_hour % 100 / 10) + 0x30;
            _buffer[12] = (_hour % 10 / 1) + 0x30;
            _buffer[14] = (_minute % 100 / 10) + 0x30;
            _buffer[15] = (_minute % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
        }
      }
      // not time
      else
      {
        {
          int _index = 2*i + 1;
          if (_index < 10)
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
          else
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index % 100 / 10) + 0x30;
            _buffer[2] = (_index % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
        }
        {
          int _index = 2*i + 2;
          if (_index < 10)
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
          else
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index % 100 / 10) + 0x30;
            _buffer[2] = (_index % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
        }
      }
    }
  }
}
void nextion_update_page_calendar_add(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x61, 0x64, 0x64, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // DAY
  if (force_refresh || day_of_week_old != day_of_week_cur)
  {
    day_of_week_old = day_of_week_cur;
    if (day_of_week_cur == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x4F, 0x4D, 0x45, 0x4E, 0x49, 0x43, 0x41, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x55, 0x4E, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 2)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x41, 0x52, 0x54, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 3)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x45, 0x52, 0x43, 0x4F, 0x4C, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 4)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x49, 0x4F, 0x56, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 5)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x45, 0x4E, 0x45, 0x52, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 6)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x41, 0x42, 0x41, 0x54, 0x4F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || hour_from_old != hour_from_tmp || minute_from_old != minute_from_tmp)
  {
    hour_from_old = hour_from_tmp;
    minute_from_old = minute_from_tmp;
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[11] = (hour_from_tmp % 100 / 10) + 0x30;
      _buffer[12] = (hour_from_tmp % 10 / 1) + 0x30;
      _buffer[14] = (minute_from_tmp % 100 / 10) + 0x30;
      _buffer[15] = (minute_from_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || hour_to_old != hour_to_tmp || minute_to_old != minute_to_tmp)
  {
    hour_to_old = hour_to_tmp;
    minute_to_old = minute_to_tmp;
    {
      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[10] = (hour_to_tmp % 100 / 10) + 0x30;
      _buffer[11] = (hour_to_tmp % 10 / 1) + 0x30;
      _buffer[13] = (minute_to_tmp % 100 / 10) + 0x30;
      _buffer[14] = (minute_to_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}
void nextion_update_page_calendar_add_err(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x61, 0x64, 0x64, 0x5F, 0x65, 0x72, 0x72, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_calendar_add_err2(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x61, 0x64, 0x64, 0x5F, 0x65, 0x72, 0x72, 0x32, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_calendar_del(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x64, 0x65, 0x6C, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_clock_warn(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x77, 0x61, 0x72, 0x6E, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_clock(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6F, 0x63, 0x6B, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x54, 0x41, 0x20, 0x28, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x30, 0x30, 0x29, 0x22, 0xff, 0xff, 0xff };
      _buffer[14] = (rtc.day_cur % 100 / 10) + 0x30;
      _buffer[15] = (rtc.day_cur % 10 / 1) + 0x30;
      _buffer[17] = (rtc.month_cur % 100 / 10) + 0x30;
      _buffer[18] = (rtc.month_cur % 10 / 1) + 0x30;
      _buffer[20] = (rtc.year_cur % 10000 / 1000) + 0x30;
      _buffer[21] = (rtc.year_cur % 1000 / 100) + 0x30;
      _buffer[22] = (rtc.year_cur % 100 / 10) + 0x30;
      _buffer[23] = (rtc.year_cur % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x45, 0x4D, 0x50, 0x4F, 0x20, 0x28, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x29, 0x22, 0xff, 0xff, 0xff };
      _buffer[15] = (rtc.hour_cur % 100 / 10) + 0x30;
      _buffer[16] = (rtc.hour_cur % 10 / 1) + 0x30;
      _buffer[18] = (rtc.minute_cur % 100 / 10) + 0x30;
      _buffer[19] = (rtc.minute_cur % 10 / 1) + 0x30;
      _buffer[21] = (rtc.second_cur % 100 / 10) + 0x30;
      _buffer[22] = (rtc.second_cur % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}
void nextion_update_page_clock_date(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x64, 0x61, 0x74, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh || rtc.year_old != rtc.year_tmp || rtc.month_old != rtc.month_tmp || rtc.day_old != rtc.day_tmp) 
  {
    rtc.year_old = rtc.year_tmp;
    rtc.month_old = rtc.month_tmp;
    rtc.day_old = rtc.day_tmp;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x31, 0x2F, 0x30, 0x31, 0x2F, 0x32, 0x30, 0x32, 0x30, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (rtc.day_tmp % 100 / 10) + 0x30;
    _buffer[9] = (rtc.day_tmp % 10 / 1) + 0x30;
    _buffer[11] = (rtc.month_tmp % 100 / 10) + 0x30;
    _buffer[12] = (rtc.month_tmp % 10 / 1) + 0x30;
    _buffer[14] = (rtc.year_tmp % 10000 / 1000) + 0x30;
    _buffer[15] = (rtc.year_tmp % 1000 / 100) + 0x30;
    _buffer[16] = (rtc.year_tmp % 100 / 10) + 0x30;
    _buffer[17] = (rtc.year_tmp % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_clock_time(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x74, 0x69, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // sensor
  if (force_refresh || rtc.hour_old != rtc.hour_tmp || rtc.minute_old != rtc.minute_tmp || rtc.second_old != rtc.second_tmp) 
  {
    rtc.hour_old = rtc.hour_tmp;
    rtc.minute_old = rtc.minute_tmp;
    rtc.second_old = rtc.second_tmp;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (rtc.hour_tmp % 100 / 10) + 0x30;
    _buffer[9] = (rtc.hour_tmp % 10 / 1) + 0x30;
    _buffer[11] = (rtc.minute_tmp % 100 / 10) + 0x30;
    _buffer[12] = (rtc.minute_tmp % 10 / 1) + 0x30;
    _buffer[14] = (rtc.second_tmp % 100 / 10) + 0x30;
    _buffer[15] = (rtc.second_tmp % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_analytics(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x61, 0x6E, 0x61, 0x6C, 0x79, 0x74, 0x69, 0x63, 0x73, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}



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

// SENSOR
uint32_t sensor_connected_millis = 0;
int sensor_connected_seconds = 0;


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
  page_current = 1;
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

  listenNextion();
  updateNextion();
}
