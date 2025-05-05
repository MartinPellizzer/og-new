// TODO: maybe do mass reset on eeprom the first start of a new board, to clear all memory (make 0 byte at 123 to check if it's first run or not)

#include "RTClib.h"
RTC_DS3231 rtc_lib;

#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include <EEPROM.h>
#define EEPROM_SIZE 1024

const uint8_t BUFFER_SIZE = 20;
uint8_t buffer_nextion[BUFFER_SIZE];

uint8_t cmd_splash[BUFFER_SIZE] = { 101, 0, 0, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_home_to_onoff[BUFFER_SIZE] = { 101, 1, 115, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_yesterday[BUFFER_SIZE] = { 101, 1, 112, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_calendar[BUFFER_SIZE] = { 101, 1, 25, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_cycle[BUFFER_SIZE] = { 101, 1, 26, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_clock[BUFFER_SIZE] = { 101, 1, 27, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_panel[BUFFER_SIZE] = { 101, 1, 114, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_sd[BUFFER_SIZE] = { 101, 1, 113, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_forbidden[BUFFER_SIZE] = { 101, 9, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_yesterday_to_home[BUFFER_SIZE] = { 101, 2, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_calendar_back[BUFFER_SIZE] = { 101, 3, 18, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_add[BUFFER_SIZE] = { 101, 3, 19, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_day_prev[BUFFER_SIZE] = { 101, 3, 20, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_day_next[BUFFER_SIZE] = { 101, 3, 21, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t1[BUFFER_SIZE] = { 101, 3, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t2[BUFFER_SIZE] = { 101, 3, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t3[BUFFER_SIZE] = { 101, 3, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t4[BUFFER_SIZE] = { 101, 3, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t5[BUFFER_SIZE] = { 101, 3, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t6[BUFFER_SIZE] = { 101, 3, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t7[BUFFER_SIZE] = { 101, 3, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t8[BUFFER_SIZE] = { 101, 3, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t9[BUFFER_SIZE] = { 101, 3, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t10[BUFFER_SIZE] = { 101, 3, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t11[BUFFER_SIZE] = { 101, 3, 12, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t12[BUFFER_SIZE] = { 101, 3, 13, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t13[BUFFER_SIZE] = { 101, 3, 14, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t14[BUFFER_SIZE] = { 101, 3, 15, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t15[BUFFER_SIZE] = { 101, 3, 16, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t16[BUFFER_SIZE] = { 101, 3, 17, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_cal_add_back[BUFFER_SIZE] = { 101, 5, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_save[BUFFER_SIZE] = { 101, 5, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_hour_up[BUFFER_SIZE] = { 101, 5, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_hour_down[BUFFER_SIZE] = { 101, 5, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_minute_up[BUFFER_SIZE] = { 101, 5, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_minute_down[BUFFER_SIZE] = { 101, 5, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_cycle_back[BUFFER_SIZE] = { 101, 4, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_save[BUFFER_SIZE] = { 101, 4, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_on_sub[BUFFER_SIZE] = { 101, 4, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_on_add[BUFFER_SIZE] = { 101, 4, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_ppb_sub[BUFFER_SIZE] = { 101, 4, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_ppb_add[BUFFER_SIZE] = { 101, 4, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_ppb_delta_sub[BUFFER_SIZE] = { 101, 4, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_ppb_delta_add[BUFFER_SIZE] = { 101, 4, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_clk_back[BUFFER_SIZE] = { 101, 6, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date[BUFFER_SIZE] = { 101, 6, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time[BUFFER_SIZE] = { 101, 6, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_clk_date_back[BUFFER_SIZE] = { 101, 7, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_save[BUFFER_SIZE] = { 101, 7, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_year_up[BUFFER_SIZE] = { 101, 7, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_year_down[BUFFER_SIZE] = { 101, 7, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_month_up[BUFFER_SIZE] = { 101, 7, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_month_down[BUFFER_SIZE] = { 101, 7, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_day_up[BUFFER_SIZE] = { 101, 7, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_day_down[BUFFER_SIZE] = { 101, 7, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_clk_time_back[BUFFER_SIZE] = { 101, 8, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_save[BUFFER_SIZE] = { 101, 8, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_hour_up[BUFFER_SIZE] = { 101, 8, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_hour_down[BUFFER_SIZE] = { 101, 8, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_minute_up[BUFFER_SIZE] = { 101, 8, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_minute_down[BUFFER_SIZE] = { 101, 8, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_second_up[BUFFER_SIZE] = { 101, 8, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_second_down[BUFFER_SIZE] = { 101, 8, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

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

#define SENSOR1_RE_DE_PIN 16
HardwareSerial Sensor1(1);
#define BUFF_LEN 9
uint8_t buff[BUFF_LEN] = { 0 };
uint8_t i = 0;
uint8_t sensor_new_data = 0;
uint32_t timer = 0;
uint32_t timer_no_signal = 0;


// ON OFF
bool is_on_old = -1;
bool is_on_cur = 1;


// O3
bool ozone_on = false;
uint32_t ozone_on_current_millis = 0;
uint32_t ozone_on_timer_millis = 0;
int8_t nextion_ozone_on_old = -1;
int8_t nextion_ozone_on_cur = 0;

// YESTERDAY
// int yesterday_buff[YESTERDAY_BUFF_NUM] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 };


///////////////////////////////////////////////////////////////////////
// ;yesterday
///////////////////////////////////////////////////////////////////////
const uint8_t YESTERDAY_BUFF_NUM = 24;
typedef struct yesterday_t 
{
  int16_t buff[YESTERDAY_BUFF_NUM] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 };
  bool is_buff_updated = false;
  int hour_old = -1;
} yesterday_t;
yesterday_t yesterday = {};

///////////////////////////////////////////////////////////////////////
// ;rtc
///////////////////////////////////////////////////////////////////////
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

DateTime now_curr;
DateTime now_old;

/* ------------------------------------------------------------------------------------- */
/* ;cycle */
/* ------------------------------------------------------------------------------------- */
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

/* ------------------------------------------------------------------------------------- */
/* ;sd */
/* ------------------------------------------------------------------------------------- */
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

/* ------------------------------------------------------------------------------------- */
/* ;sensor */
/* ------------------------------------------------------------------------------------- */
typedef struct sensor_t {
  int16_t ppb_prev;
  int16_t ppb_curr;
  int8_t connected_prev;
  int8_t connected_curr;
} sensor_t;

/* ------------------------------------------------------------------------------------- */
/* ;def */
/* ------------------------------------------------------------------------------------- */
rtc_t rtc = {};
cycle_t cycle = {};
sd_card_t sd_card = {};
sensor_t sensor = {};


// ----------------------------------------------------------------------------------------------------------
// ;sd card
// ----------------------------------------------------------------------------------------------------------
File file;
int is_insert = 0;
int is_init = 0;
int sd_val = 123;
void sd_manager_2() 
{
  sd_card_init_2();
  sd_card_write_2();
}

void sd_card_init_2() 
{
  sd_card.inserted_cur = (digitalRead(sd_card.pin_cd) == LOW) ? 1 : 0;

  if (sd_card.inserted_cur)
  {
    if (!sd_card.tried_to_initialize)
    {
      sd_card.tried_to_initialize = 1;
      if (!SD.begin()) Serial.println("Card Mount Failed");
      else Serial.println("Card Mounted");
    }
  }
  else
  {
    if (sd_card.tried_to_initialize)
    {
      SD.end();
      sd_card.tried_to_initialize = 0;
      Serial.println("Card Unounted");
    }
  }
}

void sd_card_write_2() 
{
  if (sd_card.minute_cur != rtc.minute_cur)
  {
    sd_card.minute_cur = rtc.minute_cur;
    if (sd_card.tried_to_initialize)
    {
      Serial.printf("Appending to file: %s\n", "/data.csv");
      file = SD.open("/data.csv", FILE_APPEND);
      if (!file) Serial.println("Failed to open file for appending");
      if (file.print(String(rtc.year_cur))) Serial.println("Message 1 appended");
      if (file.print(String(","))) Serial.println("Message 2 appended");
      if (file.print(String(rtc.month_cur))) Serial.println("Message 3 appended");
      if (file.print(String(","))) Serial.println("Message 4 appended");
      if (file.print(String(rtc.day_cur))) Serial.println("Message 5 appended");
      if (file.print(String(","))) Serial.println("Message 6 appended");
      if (file.print(String(rtc.hour_cur))) Serial.println("Message 7 appended");
      if (file.print(String(","))) Serial.println("Message 8 appended");
      if (file.print(String(rtc.minute_cur))) Serial.println("Message 9 appended");
      if (file.print(String(","))) Serial.println("Message 10 appended");
      if (file.print(String(rtc.second_cur))) Serial.println("Message 11 appended");
      if (file.print(String(","))) Serial.println("Message 12 appended");
      if (file.print(String(sensor.ppb_curr))) Serial.println("Message 13 appended");
      if (file.print('\n')) Serial.println("Message appended");
      file.close();
    }
  }
}

void sd_manager() 
{
  sd_card_init();
  sd_write_sensor_val_every_minute();
}

void sd_card_init() 
{
  sd_card.inserted_cur = (digitalRead(sd_card.pin_cd) == LOW) ? 1 : 0;

  if (sd_card.inserted_cur) 
  {
    if (!sd_card.tried_to_initialize) 
    {
      sd_card.tried_to_initialize = 1;
      // if (SD.begin(sd_card.pin)) sd_card.state = 1;
      if (SD.begin()) 
      {
        sd_card.state = 1;
        Serial.println("SD INIT: OK");
      }
      else 
      {
        sd_card.state = 0;
        Serial.println("SD INIT: FAIL");
      }
    }
  } 
  else 
  {
    if (sd_card.state == 1) 
    {
      sd_card.state = 0;
      sd_card.tried_to_initialize = 0;
    }
  }
}

void sd_card_write()
{
  if (sd_card.state == 1)
  {
    Serial.println("SD card in");
    // file = SD.open("data.csv", FILE_WRITE);
    
    char char_arr[2];
    sprintf(char_arr, "%d", rtc.second_cur);
    appendFile(SD, "/seconds.csv", char_arr);

    // File file = SD.open("data-2.csv", FILE_APPEND);
    // if (!file) {
    //   Serial.println("Failed to open file for appending");
    // }
    
    // if (file.print(String(rtc.second_cur))) 
    // {
    //   Serial.println(String(rtc.second_cur));
    // }
    // else
    // {
    //   Serial.print("Append failed: ");
    //   Serial.println(String(rtc.second_cur));
    // }

    // if (file.write('\n'))
    // {
    //   Serial.println("-n");
    // }
    // else
    // {
    //   Serial.print("Append failed: ");
    //   Serial.println("-n");
    // }
    
    // file.print(String(rtc.year));
    // file.write(',');
    // file.print(String(rtc.month));
    // file.write(',');
    // file.print(String(rtc.day));
    // file.write(',');
    // file.print(String(rtc.hour));
    // file.write(',');
    // file.print(String(rtc.minute));
    // file.write(',');
    // file.print(String(rtc.second));
    // file.write(',');
    // file.print(String(sensor.ppb()));
    // file.write(',');
    // file.write('\n');

    // file.close();
  }
  else
  {
    Serial.println("SD card not inserted");
  }
}

void sd_write_sensor_val_every_minute()
{
  if (millis() - sd_millis_cur >= 1000)
  {
    sd_millis_cur = millis();

    sd_card_write();
  }
}


void appendFile(fs::FS &fs, const char *path, const char *message) 
{
  Serial.printf("Appending to file: %s\n", path);

  file = fs.open(path, FILE_APPEND);
  if (!file) {
    Serial.println("Failed to open file for appending");
    return;
  }
  if (file.print(message)) {
    Serial.println("Message appended");
  } else {
    Serial.println("Append failed");
  }
  file.close();
}

void calendar_order_add_ascending() 
{
  for (int i = 0; i < CALENDAR_TIMERS_NUM; i++) 
  {
    if (calendar_days[day_curr][i] == -1) 
    {
      calendar_days[day_curr][i] = cycle_seconds_tmp;
      int32_t calendar_tmp[CALENDAR_TIMERS_NUM] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 };
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++) 
      {
        Serial.print(calendar_days[day_curr][j]);
        Serial.print(", ");
      }
      Serial.println();
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++) 
      {
        Serial.print(calendar_tmp[j]);
        Serial.print(", ");
      }
      Serial.println();
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++) 
      {
        int32_t max_val = -1;
        int max_index = 0;
        for (int k = 0; k < CALENDAR_TIMERS_NUM; k++) 
        {
          if (max_val < calendar_days[day_curr][k]) 
          {
            max_val = calendar_days[day_curr][k];
            max_index = k;
          }
        }
        calendar_days[day_curr][max_index] = -1;
        calendar_tmp[j] = max_val;
      }
      for (int j = CALENDAR_TIMERS_NUM - 1; j >= 0; j--) 
      {
        Serial.print(calendar_tmp[j]);
        Serial.print(", ");
      }
      Serial.println();
      int valid_num_index = 0;
      for (int j = CALENDAR_TIMERS_NUM - 1; j >= 0; j--) 
      {
        if (calendar_tmp[j] != -1) 
        {
          calendar_days[day_curr][valid_num_index] = calendar_tmp[j];
          valid_num_index += 1;
        }
        // eeprom_address = 100 + (day_curr*100) + bo?
      }
      
      Serial.print("day: ");
      Serial.println(day_curr);
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
      {
        int16_t timer = calendar_days[day_curr][j];
        Serial.print(j);
        Serial.print(" ");
        Serial.println(timer);
      }
      Serial.println();
      // TODO
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
      {
        int32_t timer = calendar_days[day_curr][j];
        int eeprom_address_hour = 100 + (day_curr*100) + (j*2);
        int eeprom_address_minute = 100 + (day_curr*100) + (j*2+1);
        if (timer != -1)
        {
          uint8_t hour = timer / 3600;
          uint8_t minute = timer % 3600 / 60;
          Serial.print("hour: ");
          Serial.println(hour);
          Serial.print("minute: ");
          Serial.println(minute);
          EEPROM.write(eeprom_address_hour, hour);
          EEPROM.write(eeprom_address_minute, minute);
          EEPROM.commit();
        }
        else
        {
          EEPROM.write(eeprom_address_hour, 255);
          EEPROM.write(eeprom_address_minute, 255);
          EEPROM.commit();
        }
      }
      break;
    }
  }
}

// TODO
void calendar_delete_and_order_ascending(int delete_index) 
{
  calendar_days[day_curr][delete_index] = -1;
  for (int i = delete_index; i < CALENDAR_TIMERS_NUM - 1; i++) 
  {
    calendar_days[day_curr][i] = calendar_days[day_curr][i + 1];
    uint32_t timer = calendar_days[day_curr][i];
    int eeprom_address_hour = 100 + (day_curr*100) + (i*2);
    int eeprom_address_minute = 100 + (day_curr*100) + (i*2+1);
    if (timer != -1)
    {
      uint8_t hour = timer / 3600;
      uint8_t minute = timer % 3600 / 60;
      EEPROM.write(eeprom_address_hour, hour);
      EEPROM.write(eeprom_address_minute, minute);
      EEPROM.commit();
    }
    else
    {
      EEPROM.write(eeprom_address_hour, 255);
      EEPROM.write(eeprom_address_minute, 255);
      EEPROM.commit();
    }
  }
  calendar_days[day_curr][CALENDAR_TIMERS_NUM - 1] = -1;
  int eeprom_address_hour = 100 + (day_curr*100) + ((CALENDAR_TIMERS_NUM - 1)*2);
  int eeprom_address_minute = 100 + (day_curr*100) + ((CALENDAR_TIMERS_NUM - 1)*2+1);
  EEPROM.write(eeprom_address_hour, 255);
  EEPROM.write(eeprom_address_minute, 255);
  EEPROM.commit();

/*
  for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
  {
    int16_t timer = calendar_days[0][j];
    int eeprom_address_hour = 100 + (0*100) + (j*2);
    int eeprom_address_minute = 100 + (0*100) + (j*2+1);
    if (timer != -1)
    {
      uint8_t hour = timer / 3600;
      uint8_t minute = timer % 3600 / 60;
      EEPROM.write(eeprom_address_hour, hour);
      EEPROM.write(eeprom_address_minute, minute);
      EEPROM.commit();
    }
    else
    {
      EEPROM.write(eeprom_address_hour, 255);
      EEPROM.write(eeprom_address_minute, 255);
      EEPROM.commit();
    }
  }
  */
}



////////////////////////////////////////////////
// ;nextion
////////////////////////////////////////////////
void updateNextion() 
{
  uint8_t force_refresh = 0;
  if (page_old != page_current) 
  {
    page_old = page_current;
    force_refresh = 1;
  }
  /**/ if (page_current == 1)  nextion_update_page_home(force_refresh);
  else if (page_current == 10) nextion_update_page_yesterday(force_refresh);
  else if (page_current == 20) nextion_update_page_calendar(force_refresh);
  else if (page_current == 21) nextion_update_p_cal_add(force_refresh);
  else if (page_current == 30) nextion_update_page_cycle(force_refresh);
  else if (page_current == 40) nextion_update_p_clk(force_refresh);
  else if (page_current == 41) nextion_update_p_clk_date(force_refresh);
  else if (page_current == 42) nextion_update_p_clk_time(force_refresh);
  else if (page_current == 50) nextion_update_p_forbidden(force_refresh);
  else if (page_current == 60) nextion_update_p_forbidden(force_refresh);
}

////////////////////////////////////////////////////////
// ;home
////////////////////////////////////////////////////////
void nextion_update_page_home(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x61, 0x67, 0x65, 0x5F, 0x68, 0x6F, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // on/off
  /*
  if (force_refresh || is_on_old != is_on_cur) 
  {
    is_on_old = is_on_cur;
    Serial.println(is_on_cur);
    if (is_on_cur == 0) 
    {
      uint8_t _buffer[] = {0x70, 0x31, 0x30, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x38, 0xff, 0xff, 0xff};
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else 
    {
      uint8_t _buffer[] = {0x70, 0x31, 0x30, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x39, 0xff, 0xff, 0xff};
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  */
  // sd card
  if (force_refresh || sd_card.inserted_old != sd_card.inserted_cur) 
  {
    sd_card.inserted_old = sd_card.inserted_cur;
    if (sd_card.inserted_old == 1) 
    {
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    } else {
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // rtc
  if (force_refresh || now_old != now_curr) {
    now_old = now_curr;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (rtc.hour_cur % 100 / 10) + 0x30;
    _buffer[9] = (rtc.hour_cur % 10 / 1) + 0x30;
    _buffer[11] = (rtc.minute_cur % 100 / 10) + 0x30;
    _buffer[12] = (rtc.minute_cur % 10 / 1) + 0x30;
    _buffer[14] = (rtc.second_cur % 100 / 10) + 0x30;
    _buffer[15] = (rtc.second_cur % 10 / 1) + 0x30;
    _buffer[17] = (rtc.day_week % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
  // ozone
  if (force_refresh || nextion_ozone_on_old != nextion_ozone_on_cur) 
  {
    nextion_ozone_on_old = nextion_ozone_on_cur;
    if (nextion_ozone_on_cur == 1) {
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
    if (nextion_ozone_on_cur == 0) {
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // calendar
  if (force_refresh || nextion_calendar_state_old != nextion_calendar_state_cur) {
    nextion_calendar_state_old = nextion_calendar_state_cur;
    if (nextion_calendar_state_cur == 1) {
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
    if (nextion_calendar_state_cur == 0) {
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // sensor
  if (force_refresh || sensor.connected_prev != sensor.connected_curr) 
  {
    sensor.connected_prev = sensor.connected_curr;
    if (sensor.connected_curr == 0) 
    {
      {
        uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      // rect
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    } else {
      {
        uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      // rect
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  if (force_refresh || sensor.ppb_prev != sensor.ppb_curr) 
  {
    sensor.ppb_prev = sensor.ppb_curr;
    if (sensor.ppb_curr == -1) 
    {
      uint8_t _buffer[] = {0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x2D, 0x2D, 0x2E, 0x2D, 0x2D, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    } 
    else 
    {
      uint8_t _buffer[] = {0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
      _buffer[9] = (sensor.ppb_curr % 10000 / 1000) + 0x30;
      _buffer[11] = (sensor.ppb_curr % 1000 / 100) + 0x30;
      _buffer[12] = (sensor.ppb_curr % 100 / 10) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

///////////////////////////////////////////////////////////////////////
// ;yesterday
///////////////////////////////////////////////////////////////////////
void nextion_update_page_yesterday(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t cmd_page_home[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x61, 0x67, 0x65, 0x5F, 0x79, 0x65, 0x73, 0x74, 0x65, 0x72, 0x64, 0x61, 0x79, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(cmd_page_home) / sizeof(uint8_t); i++) 
    {
      Serial2.write(cmd_page_home[i]);
    }
  }
  if (force_refresh || yesterday.is_buff_updated) 
  {
    yesterday.is_buff_updated = false;
    for (uint8_t i = 0; i < YESTERDAY_BUFF_NUM; i++) 
    {
      if (yesterday.buff[i] != -1) 
      {
        if (i < 10) 
        {
          uint8_t _buffer[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x2D, 0x30, 0x30, 0x3A, 0x20, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
          _buffer[1] = (i) + 0x30;
          _buffer[9] = (i % 100 / 10) + 0x30;
          _buffer[10] = (i % 10 / 1) + 0x30;
          _buffer[13] = (yesterday.buff[i] % 100000 / 10000) + 0x30;
          _buffer[14] = (yesterday.buff[i] % 10000 / 1000) + 0x30;
          _buffer[16] = (yesterday.buff[i] % 1000 / 100) + 0x30;
          _buffer[17] = (yesterday.buff[i] % 100 / 10) + 0x30;
          _buffer[18] = (yesterday.buff[i] % 10 / 1) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        } 
        else 
        {
          uint8_t _buffer[] = {0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x2D, 0x30, 0x30, 0x3A, 0x20, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
          _buffer[1] = (i % 100 / 10) + 0x30;
          _buffer[2] = (i % 10 / 1) + 0x30;
          _buffer[10] = (i % 100 / 10) + 0x30;
          _buffer[11] = (i % 10 / 1) + 0x30;
          _buffer[14] = (yesterday.buff[i] % 100000 / 10000) + 0x30;
          _buffer[15] = (yesterday.buff[i] % 10000 / 1000) + 0x30;
          _buffer[17] = (yesterday.buff[i] % 1000 / 100) + 0x30;
          _buffer[18] = (yesterday.buff[i] % 100 / 10) + 0x30;
          _buffer[19] = (yesterday.buff[i] % 10 / 1) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        } 
      }
    }
  }
}
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* ;calendar */
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_page_calendar(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t cmd_page_home[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x61, 0x67, 0x65, 0x5F, 0x63, 0x61, 0x6C, 0x65, 0x6E, 0x64, 0x61, 0x72, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(cmd_page_home) / sizeof(uint8_t); i++) {
      Serial2.write(cmd_page_home[i]);
    }
    day_old = -1;
  }
  if (force_refresh || day_old != day_curr) {
    day_old = day_curr;
    if (day_curr == 1)  // Lunedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x75, 0x6E, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 2)  // Martedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x61, 0x72, 0x74, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 3)  // Mercoledi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x65, 0x72, 0x63, 0x6F, 0x6C, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 4)  // Giovedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x69, 0x6F, 0x76, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 5)  // Venerdi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x65, 0x6E, 0x65, 0x72, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 6)  // Sabato
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x61, 0x62, 0x61, 0x74, 0x6F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 0)  // Domenica
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x6F, 0x6D, 0x65, 0x6E, 0x69, 0x63, 0x61, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    }

    for (int timer_index = 0; timer_index < CALENDAR_TIMERS_NUM; timer_index++) {
      int32_t _seconds = calendar_days[day_curr][timer_index];
      int timer_index_display = timer_index + 1;  // OFFSET TO THE FIRST TEXT WITGET OF NEXTION TFT
      if (_seconds < 0) {
        if (timer_index_display < 10) {
          uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x5F, 0x5F, 0x3A, 0x5F, 0x5F, 0x22, 0xff, 0xff, 0xff };
          _buffer[1] = (timer_index_display % 10 / 1) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
            Serial2.write(_buffer[i]);
          }
        } else {
          uint8_t _buffer[] = { 0x74, 0x31, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x5F, 0x5F, 0x3A, 0x5F, 0x5F, 0x22, 0xff, 0xff, 0xff };
          _buffer[1] = (timer_index_display % 100 / 10) + 0x30;
          _buffer[2] = (timer_index_display % 10 / 1) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
            Serial2.write(_buffer[i]);
          }
        }
      } 
      else 
      {
        if (timer_index_display < 10) 
        {
          uint8_t _buffer[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x20, 0x58, 0x22, 0xff, 0xff, 0xff};
          _buffer[1] = (timer_index_display % 10 / 1) + 0x30;
          int hour = _seconds / 3600;
          int hour_1 = hour % 100 / 10;
          int hour_2 = hour % 10 / 1;
          int minute = _seconds % 3600 / 60;
          int minute_1 = minute % 100 / 10;
          int minute_2 = minute % 10 / 1;
          _buffer[8] = (hour_1) + 0x30;
          _buffer[9] = (hour_2) + 0x30;
          _buffer[11] = (minute_1) + 0x30;
          _buffer[12] = (minute_2) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        } 
        else 
        {
          uint8_t _buffer[] = {0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x20, 0x58, 0x22, 0xff, 0xff, 0xff};
          _buffer[1] = (timer_index_display % 100 / 10) + 0x30;
          _buffer[2] = (timer_index_display % 10 / 1) + 0x30;
          int hour = _seconds / 3600;
          int hour_1 = hour % 100 / 10;
          int hour_2 = hour % 10 / 1;
          int minute = _seconds % 3600 / 60;
          int minute_1 = minute % 100 / 10;
          int minute_2 = minute % 10 / 1;
          _buffer[9] = (hour_1) + 0x30;
          _buffer[10] = (hour_2) + 0x30;
          _buffer[12] = (minute_1) + 0x30;
          _buffer[13] = (minute_2) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        }
      }
    }
  }
}
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* PAGE CALENDAR ADD */
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_p_cal_add(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x61, 0x64, 0x64, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    day_old = -1;

    cycle_second_old = -1;
    cycle_seconds_tmp = 0;
  }
  if (force_refresh || day_old != day_curr) {
    day_old = day_curr;
    if (day_curr == 1)  // Lunedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x75, 0x6E, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 2)  // Martedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x61, 0x72, 0x74, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 3)  // Mercoledi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x65, 0x72, 0x63, 0x6F, 0x6C, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 4)  // Giovedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x69, 0x6F, 0x76, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 5)  // Venerdi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x65, 0x6E, 0x65, 0x72, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 6)  // Sabato
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x61, 0x62, 0x61, 0x74, 0x6F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 0)  // Domenica
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x6F, 0x6D, 0x65, 0x6E, 0x69, 0x63, 0x61, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || cycle_second_old != cycle_seconds_tmp) {
    cycle_second_old = cycle_seconds_tmp;
    uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    int hour = cycle_seconds_tmp / 3600;
    int hour_1 = hour % 100 / 10;
    int hour_2 = hour % 10 / 1;
    int minute = cycle_seconds_tmp % 3600 / 60;
    int minute_1 = minute % 100 / 10;
    int minute_2 = minute % 10 / 1;
    _buffer[8] = (hour_1) + 0x30;
    _buffer[9] = (hour_2) + 0x30;
    _buffer[11] = (minute_1) + 0x30;
    _buffer[12] = (minute_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
}
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* ;cycle */
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_page_cycle(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x61, 0x67, 0x65, 0x5F, 0x63, 0x79, 0x63, 0x6C, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    cycle.seconds_on_old = -1;
    cycle.seconds_on_tmp = cycle.seconds_on_cur;
    cycle.ppb_old = -1;
    cycle.ppb_tmp = cycle.ppb_cur;
    cycle.ppb_delta_old = -1;
    cycle.ppb_delta_tmp = cycle.ppb_delta_cur;
  }
  if (force_refresh || cycle.seconds_on_old != cycle.seconds_on_tmp) {
    cycle.seconds_on_old = cycle.seconds_on_tmp;
    uint8_t _buffer[] = {0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x45, 0x4D, 0x50, 0x4F, 0x20, 0x43, 0x49, 0x43, 0x4C, 0x4F, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x20, 0x6D, 0x69, 0x6E, 0x75, 0x74, 0x69, 0x22, 0xff, 0xff, 0xff};
    int minute = cycle.seconds_on_tmp / 60;
    int minute_1 = minute % 100 / 10;
    int minute_2 = minute % 10 / 1;
    _buffer[22] = (minute_1) + 0x30;
    _buffer[23] = (minute_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh || cycle.ppb_old != cycle.ppb_tmp) {
    cycle.ppb_old = cycle.ppb_tmp;
    uint8_t _buffer[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x50, 0x4D, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x54, 0x41, 0x52, 0x47, 0x45, 0x54, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
    int ppm = cycle.ppb_tmp;
    int ppm_1 = ppm % 100000 / 10000;
    int ppm_2 = ppm % 10000 / 1000;
    int ppm_3 = ppm % 1000 / 100;
    int ppm_4 = ppm % 100 / 10;
    int ppm_5 = ppm % 10 / 1;
    _buffer[27] = (ppm_1) + 0x30;
    _buffer[28] = (ppm_2) + 0x30;
    _buffer[30] = (ppm_3) + 0x30;
    _buffer[31] = (ppm_4) + 0x30;
    _buffer[32] = (ppm_5) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh || cycle.ppb_delta_old != cycle.ppb_delta_tmp) {
    cycle.ppb_delta_old = cycle.ppb_delta_tmp;
    uint8_t _buffer[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x4F, 0x4C, 0x4C, 0x45, 0x52, 0x41, 0x4E, 0x5A, 0x41, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x2D, 0x20, 0x32, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff};
    int ppm_delta = cycle.ppb_delta_tmp;
    int ppm_delta_1 = ppm_delta % 100 / 10;
    int ppm_delta_2 = ppm_delta % 10 / 1;
    _buffer[27] = (ppm_delta_1) + 0x30;
    _buffer[28] = (ppm_delta_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
}
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* ;clock */
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_p_clk(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x73, 0x65, 0x74, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    // DATE
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x54, 0x41, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x20, 0x28, 0x61, 0x6E, 0x6E, 0x6F, 0x2F, 0x6D, 0x65, 0x73, 0x65, 0x2F, 0x67, 0x69, 0x6F, 0x72, 0x6E, 0x6F, 0x29, 0x22, 0xff, 0xff, 0xff };
      int year_1 = rtc.year_cur % 10000 / 1000;
      int year_2 = rtc.year_cur % 1000 / 100;
      int year_3 = rtc.year_cur % 100 / 10;
      int year_4 = rtc.year_cur % 10 / 1;
      _buffer[15] = (year_1) + 0x30;
      _buffer[16] = (year_2) + 0x30;
      _buffer[17] = (year_3) + 0x30;
      _buffer[18] = (year_4) + 0x30;
      int month_1 = rtc.month_cur % 100 / 10;
      int month_2 = rtc.month_cur % 10 / 1;
      _buffer[20] = (month_1) + 0x30;
      _buffer[21] = (month_2) + 0x30;
      int day_1 = rtc.day_cur % 100 / 10;
      int day_2 = rtc.day_cur % 10 / 1;
      _buffer[23] = (day_1) + 0x30;
      _buffer[24] = (day_2) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    }
    // TIME
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x45, 0x4D, 0x50, 0x4F, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x20, 0x28, 0x6F, 0x72, 0x61, 0x3A, 0x6D, 0x69, 0x6E, 0x75, 0x74, 0x6F, 0x3A, 0x73, 0x65, 0x63, 0x6F, 0x6E, 0x64, 0x6F, 0x29, 0x22, 0xff, 0xff, 0xff };
      int hour = rtc.hour_cur;
      int hour_1 = hour % 100 / 10;
      int hour_2 = hour % 10 / 1;
      _buffer[16] = (hour_1) + 0x30;
      _buffer[17] = (hour_2) + 0x30;
      int minute = rtc.minute_cur;
      int minute_1 = minute % 100 / 10;
      int minute_2 = minute % 10 / 1;
      _buffer[19] = (minute_1) + 0x30;
      _buffer[20] = (minute_2) + 0x30;
      int second = rtc.second_cur;
      int second_1 = second % 100 / 10;
      int second_2 = second % 10 / 1;
      _buffer[22] = (second_1) + 0x30;
      _buffer[23] = (second_2) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* PAGE CLOCK DATE*/
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_p_clk_date(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x64, 0x61, 0x74, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    rtc.year_old = -1;
    rtc.year_tmp = rtc.year_cur;
    rtc.month_old = -1;
    rtc.month_tmp = rtc.month_cur;
    rtc.day_old = -1;
    rtc.day_tmp = rtc.day_cur;
  }
  if (force_refresh || rtc.year_old != rtc.year_tmp || rtc.month_old != rtc.month_tmp || rtc.day_old != rtc.day_tmp) {
    rtc.year_old = rtc.year_tmp;
    rtc.month_old = rtc.month_tmp;
    rtc.day_old = rtc.day_tmp;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    int year_1 = rtc.year_tmp % 10000 / 1000;
    int year_2 = rtc.year_tmp % 1000 / 100;
    int year_3 = rtc.year_tmp % 100 / 10;
    int year_4 = rtc.year_tmp % 10 / 1;
    _buffer[8] = (year_1) + 0x30;
    _buffer[9] = (year_2) + 0x30;
    _buffer[10] = (year_3) + 0x30;
    _buffer[11] = (year_4) + 0x30;
    int month_1 = rtc.month_tmp % 100 / 10;
    int month_2 = rtc.month_tmp % 10 / 1;
    _buffer[13] = (month_1) + 0x30;
    _buffer[14] = (month_2) + 0x30;
    int day_1 = rtc.day_tmp % 100 / 10;
    int day_2 = rtc.day_tmp % 10 / 1;
    _buffer[16] = (day_1) + 0x30;
    _buffer[17] = (day_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
}

/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* PAGE CLOCK TIME*/
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_p_clk_time(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x74, 0x69, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    rtc.second_old = -1;
    rtc.second_tmp = rtc.second_cur + (rtc.minute_cur * 60) + (rtc.hour_cur * 3600);
  }
  if (force_refresh || rtc.second_old != rtc.second_tmp) {
    rtc.second_old = rtc.second_tmp;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    int hour = rtc.second_tmp / 3600;
    int hour_1 = hour % 100 / 10;
    int hour_2 = hour % 10 / 1;
    int minute = rtc.second_tmp % 3600 / 60;
    int minute_1 = minute % 100 / 10;
    int minute_2 = minute % 10 / 1;
    int second = rtc.second_tmp % 3600 % 60 / 1;
    int second_1 = second % 100 / 10;
    int second_2 = second % 10 / 1;
    _buffer[8] = (hour_1) + 0x30;
    _buffer[9] = (hour_2) + 0x30;
    _buffer[11] = (minute_1) + 0x30;
    _buffer[12] = (minute_2) + 0x30;
    _buffer[14] = (second_1) + 0x30;
    _buffer[15] = (second_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
}

///////////////////////////////////////////////////////
// ;forbidden
///////////////////////////////////////////////////////
void nextion_update_p_forbidden(uint8_t force_refresh) 
{
 if (force_refresh) 
 {
    uint8_t _buffer[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x66, 0x6F, 0x72, 0x62, 0x69, 0x64, 0x64, 0x65, 0x6E, 0xff, 0xff, 0xff};
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}

bool compareArray(uint8_t *a, uint8_t *b) {
  for (uint8_t i = 0; i < BUFFER_SIZE; i++) {
    if (a[i] != b[i]) {
      return false;
    }
  }
  return true;
}

void nextionClearBuffer() {
  for (int i = 0; i < BUFFER_SIZE; i++) {
    buffer_nextion[i] = 0;
  }
}

void nextionDebugSerial() {
  for (int i = 0; i < BUFFER_SIZE; i++) {
    Serial.print(buffer_nextion[i]);
    Serial.print(" ");
  }
  Serial.println();
}

bool nextionExecCommand(uint8_t arr[], uint8_t arr_size) {
  for (uint8_t i = 0; i < arr_size; i++) {
    Serial2.write(arr[i]);
  }
}

void clear_buffer(uint8_t buff[], uint8_t len) {
  for (int i = 0; i < len; i++) buff[i] = 0;
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


// OZONE
/*
void cycle_update() 
{
  if (sensor.connected_curr == 0)
  {}
  if (ozone_on) 
  {
    if ((millis() - ozone_on_current_millis) > ozone_on_timer_millis) 
    {
      ozone_on = false;
      digitalWrite(relay_pin, LOW);
    } 
    else 
    {
      int ppb_min = cycle.ppb_cur - (cycle.ppb_cur / 100 * cycle.ppb_delta_cur);
      int ppb_max = cycle.ppb_cur + (cycle.ppb_cur / 100 * cycle.ppb_delta_cur);
      if (sensor.ppb_curr < ppb_min) 
      {
        digitalWrite(relay_pin, HIGH);
        nextion_ozone_on_cur = 1;
      } 
      if (sensor.ppb_curr > ppb_max)
      {
        digitalWrite(relay_pin, LOW);
        nextion_ozone_on_cur = 0;
      }
    }
    nextion_calendar_state_cur = 1;
  } 
  else 
  {
    for (int i = 0; i < CALENDAR_TIMERS_NUM; i++) 
    {
      int32_t rtc_seconds_tot = (rtc.hour_cur * 3600) + (rtc.minute_cur * 60) + (rtc.second_cur);
      int32_t calendar_seconds_tot = calendar_days[rtc.day_week][i];
      if (rtc_seconds_tot == calendar_seconds_tot) 
      {
        ozone_on = true;
        ozone_on_current_millis = millis();
        ozone_on_timer_millis = uint32_t(cycle.seconds_on_cur) * 1000;
      }
    }
    nextion_ozone_on_cur = 0;
    nextion_calendar_state_cur = 0;
  }
}
*/
void cycle_update() 
{
  if (ozone_on) 
  {
    nextion_calendar_state_cur = 1;
    if ((millis() - ozone_on_current_millis) > ozone_on_timer_millis) 
    {
      ozone_on = false;
      digitalWrite(relay_pin, LOW);
    }
    else
    {  
      if (sensor.connected_curr == 0)
      {
        nextion_ozone_on_cur = 0;
        digitalWrite(relay_pin, LOW);
      }
      else
      {
        int ppb_min = cycle.ppb_cur - (cycle.ppb_cur / 100 * cycle.ppb_delta_cur);
        int ppb_max = cycle.ppb_cur + (cycle.ppb_cur / 100 * cycle.ppb_delta_cur);
        if (sensor.ppb_curr < ppb_min) 
        {
          digitalWrite(relay_pin, HIGH);
          nextion_ozone_on_cur = 1;
        }
        if (sensor.ppb_curr > ppb_max)
        {
          digitalWrite(relay_pin, LOW);
          nextion_ozone_on_cur = 0;
        }
      }
    }
  }
  else 
  {
    nextion_calendar_state_cur = 0;
    nextion_ozone_on_cur = 0;

    for (int i = 0; i < CALENDAR_TIMERS_NUM; i++) 
    {
      int32_t rtc_seconds_tot = (rtc.hour_cur * 3600) + (rtc.minute_cur * 60) + (rtc.second_cur);
      int32_t calendar_seconds_tot = calendar_days[rtc.day_week][i];
      if (rtc_seconds_tot == calendar_seconds_tot) 
      {
        ozone_on = true;
        ozone_on_current_millis = millis();
        ozone_on_timer_millis = uint32_t(cycle.seconds_on_cur) * 1000;
      }
    }
  }
}

// SENSOR
uint32_t sensor_connected_millis = 0;
int sensor_connected_seconds = 0;

void sensor_update() 
{
  if (sensor.connected_curr == 1) 
  {
    if (millis() - sensor_connected_millis > 1000) 
    {
      sensor_connected_millis = millis();
      sensor_connected_seconds += 1;
      if (sensor_connected_seconds > 5) 
      {
        sensor.connected_curr = 0;
        sensor.ppb_curr = -1;
        sensor.ppb_prev = 0;
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
      sensor.ppb_curr = 0;
      if (checksum(buff, 9) == buff[8]) 
      {
        sensor.ppb_curr = buff[4] * 256 + buff[5];
        sensor_connected_millis = millis();
        sensor_connected_seconds = 0;
        sensor.connected_curr = 1;
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

void yesterday_update() 
{
  if (yesterday.hour_old != rtc.hour_cur) 
  {
    yesterday.hour_old = rtc.hour_cur;
    for (int i = YESTERDAY_BUFF_NUM - 1; i >= 0; i--)
    {
      yesterday.buff[i+1] = yesterday.buff[i];
    }
    yesterday.buff[0] = sensor.ppb_curr;
    yesterday.is_buff_updated = true;
  }
}

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

void rtc_manager() {
  now_curr = rtc_lib.now();
  rtc.second_cur = now_curr.second();
  rtc.minute_cur = now_curr.minute();
  rtc.hour_cur = now_curr.hour();
  rtc.day_week = now_curr.dayOfTheWeek();

  rtc.year_cur = now_curr.year();
  rtc.month_cur = now_curr.month();
  rtc.day_cur = now_curr.day();
}

void loop() 
{
  /* ;sd */
  sd_manager_2();

  /* ;rtc */
  rtc_manager();

  cycle_update();

  sensor_update();

  yesterday_update();

  listenNextion();
  updateNextion();

}
