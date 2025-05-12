/* ------------------------------------------------------------------------------------- */
/* ;libraries */
/* ------------------------------------------------------------------------------------- */
#include "main.h"
#include <EEPROM.h>

#include <Wire.h>
#include "RTClib.h"
RTC_DS3231 rtc_ds3231;
DateTime now;

#include <SPI.h>
#include <SD.h>
File file;

/* ------------------------------------------------------------------------------------- */
/* ;structs */
/* ------------------------------------------------------------------------------------- */
nextion_t nextion = {};
relay_t relay = {};
sensor_t sensor = {};
sd_card_t sd_card = {};
rtc_t rtc = {};

onoff_t onoff = {};
power_t power = {};
cycle_t cycle = {};
selprog_t selprog = {};

program_t tmp_prog = {};
programs_t week_programs = {};
programs_t monday_programs = {};
programs_t tuesday_programs = {};
programs_t wednesday_programs = {};
programs_t thursday_programs = {};
programs_t friday_programs = {};
programs_t saturday_programs = {};
programs_t sunday_programs = {};
programs_t *curr_programs = NULL;

/* ------------------------------------------------------------------------------------- */
/* ;variables */
/* ------------------------------------------------------------------------------------- */
unsigned long second_millis_current = 0;
int8_t curr_setprog;
int8_t curr_listprog_index = 0;
int8_t prev_listprog_index = -1;

bool new_data = false;
unsigned long nextion_current_millis = 0;
int buffer_counter = 0;

/* sensor average in 1 min */

uint8_t value_written = 0;
uint32_t curr_millis = 0;
#define NUM_ELEM 60
int16_t buff_index = 0;
int16_t buff[NUM_ELEM] = {};

/* ------------------------------------------------------------------------------------- */
/* ;commands */
/* ------------------------------------------------------------------------------------- */
const uint8_t BUFFER_SIZE = 20;
uint8_t buffer_nextion[BUFFER_SIZE];

uint8_t cmd_dashboard_gear_icon[BUFFER_SIZE] = {101, 1, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_dashboard_onoff_icon[BUFFER_SIZE] = {101, 1, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_settings_backarrow_icon[BUFFER_SIZE] = {101, 2, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_settings_select_icon[BUFFER_SIZE] = {101, 2, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_settings_calendar_icon[BUFFER_SIZE] = {101, 2, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_settings_cycle_icon[BUFFER_SIZE] = {101, 2, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_settings_clock_icon[BUFFER_SIZE] = {101, 2, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_settings_infosys_icon[BUFFER_SIZE] = {101, 2, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_settings_sd_icon[BUFFER_SIZE] = {101, 2, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_settings_power_icon[BUFFER_SIZE] = {101, 2, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_selprog_backarrow_icon[BUFFER_SIZE] = {101, 3, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_selprog_save_icon[BUFFER_SIZE] = {101, 3, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_selprog_prog_leftarrow_icon[BUFFER_SIZE] = {101, 3, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_selprog_prog_rightarrow_icon[BUFFER_SIZE] = {101, 3, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_setprog_backarrow_icon[BUFFER_SIZE] = {101, 4, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprog_daily_button[BUFFER_SIZE] = {101, 4, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprog_weekly_button[BUFFER_SIZE] = {101, 4, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_setprogday_backarrow_icon[BUFFER_SIZE] = {101, 5, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprogday_monday_button[BUFFER_SIZE] = {101, 5, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprogday_tuesday_button[BUFFER_SIZE] = {101, 5, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprogday_wednesday_button[BUFFER_SIZE] = {101, 5, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprogday_thursday_button[BUFFER_SIZE] = {101, 5, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprogday_friday_button[BUFFER_SIZE] = {101, 5, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprogday_saturday_button[BUFFER_SIZE] = {101, 5, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setprogday_sunday_button[BUFFER_SIZE] = {101, 5, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_listprog_backarrow_icon[BUFFER_SIZE] = {101, 6, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_listprog_add_icon[BUFFER_SIZE] = {101, 6, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_listprog_prog_leftdoublearrow_icon[BUFFER_SIZE] = {101, 6, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_listprog_prog_rightdoublearrow_icon[BUFFER_SIZE] = {101, 6, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_listprog_prog_delete_icon[BUFFER_SIZE] = {101, 6, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_addprog_backarrow_icon[BUFFER_SIZE] = {101, 7, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprog_save_icon[BUFFER_SIZE] = {101, 7, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprog_startarrow_icon[BUFFER_SIZE] = {101, 7, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprog_endarrow_icon[BUFFER_SIZE] = {101, 7, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_addprogfrom_backarrow_icon[BUFFER_SIZE] = {101, 13, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogfrom_save_icon[BUFFER_SIZE] = {101, 13, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogfrom_hh_leftarrow_icon[BUFFER_SIZE] = {101, 13, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogfrom_hh_rightarrow_icon[BUFFER_SIZE] = {101, 13, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogfrom_mm_leftarrow_icon[BUFFER_SIZE] = {101, 13, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogfrom_mm_rightarrow_icon[BUFFER_SIZE] = {101, 13, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_addprogto_backarrow_icon[BUFFER_SIZE] = {101, 14, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogto_save_icon[BUFFER_SIZE] = {101, 14, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogto_hh_leftarrow_icon[BUFFER_SIZE] = {101, 14, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogto_hh_rightarrow_icon[BUFFER_SIZE] = {101, 14, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogto_mm_leftarrow_icon[BUFFER_SIZE] = {101, 14, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_addprogto_mm_rightarrow_icon[BUFFER_SIZE] = {101, 14, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_setcycle_backarrow_icon[BUFFER_SIZE] = {101, 8, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setcycle_save_icon[BUFFER_SIZE] = {101, 8, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setcycle_on_leftarrow_icon[BUFFER_SIZE] = {101, 8, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setcycle_on_rightarrow_icon[BUFFER_SIZE] = {101, 8, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setcycle_off_leftarrow_icon[BUFFER_SIZE] = {101, 8, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setcycle_off_rightarrow_icon[BUFFER_SIZE] = {101, 8, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_setclock_backarrow_icon[BUFFER_SIZE] = {101, 9, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclock_ymdarrow_icon[BUFFER_SIZE] = {101, 9, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclock_hmsarrow_icon[BUFFER_SIZE] = {101, 9, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_setclockymd_backarrow_icon[BUFFER_SIZE] = {101, 10, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockymd_save_icon[BUFFER_SIZE] = {101, 10, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockymd_dd_leftarrow_icon[BUFFER_SIZE] = {101, 10, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockymd_dd_rightarrow_icon[BUFFER_SIZE] = {101, 10, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockymd_mm_leftarrow_icon[BUFFER_SIZE] = {101, 10, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockymd_mm_rightarrow_icon[BUFFER_SIZE] = {101, 10, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockymd_yy_leftarrow_icon[BUFFER_SIZE] = {101, 10, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockymd_yy_rightarrow_icon[BUFFER_SIZE] = {101, 10, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_setclockhms_backarrow_icon[BUFFER_SIZE] = {101, 11, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockhms_save_icon[BUFFER_SIZE] = {101, 11, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockhms_hh_leftarrow_icon[BUFFER_SIZE] = {101, 11, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockhms_hh_rightarrow_icon[BUFFER_SIZE] = {101, 11, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockhms_mm_leftarrow_icon[BUFFER_SIZE] = {101, 11, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockhms_mm_rightarrow_icon[BUFFER_SIZE] = {101, 11, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockhms_ss_leftarrow_icon[BUFFER_SIZE] = {101, 11, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_setclockhms_ss_rightarrow_icon[BUFFER_SIZE] = {101, 11, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_analytics_backarrow_icon[BUFFER_SIZE] = {101, 12, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_sd_backarrow_icon[BUFFER_SIZE] = {101, 12, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_power_backarrow_icon[BUFFER_SIZE] = {101, 15, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_power_save_icon[BUFFER_SIZE] = {101, 15, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_power_type_leftarrow_icon[BUFFER_SIZE] = {101, 15, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_power_type_rightarrow_icon[BUFFER_SIZE] = {101, 15, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_power_manual_val_leftarrow_icon[BUFFER_SIZE] = {101, 15, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
uint8_t cmd_power_manual_val_rightarrow_icon[BUFFER_SIZE] = {101, 15, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

uint8_t cmd_infosys_backarrow_icon[BUFFER_SIZE] = {101, 16, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

// -------------------------------------------------------------------------------------------------------------------------
// ;eeprom
// -------------------------------------------------------------------------------------------------------------------------
void eeprom_init_first_time()
{
  eeprom_write_int(cycle.eeprom_id_address, 0);
  eeprom_write_int(cycle.eeprom_time_on_address, 20);
  eeprom_write_int(cycle.eeprom_time_off_address, 10);
}

void eeprom_write_int(int address, int value)
{
  byte two = (value & 0xFF);
  byte one = ((value >> 8) & 0xFF);

  EEPROM.update(address, two);
  EEPROM.update(address + 1, one);
}

int eeprom_read_int(int address)
{
  long two = EEPROM.read(address);
  long one = EEPROM.read(address + 1);

  return ((two << 0) & 0xFFFFFF) + ((one << 8) & 0xFFFFFFFF);
}

void eeprom_write_byte(int address, int value)
{
  EEPROM.update(address, value);
}

int eeprom_read_byte(int address)
{
  return EEPROM.read(address);
}

// -------------------------------------------------------------------------------------------------------------------------
// ;sensor
// -------------------------------------------------------------------------------------------------------------------------

void sensor_manager()
{
  sensor_read();
  sensor_check_working();
}

unsigned char get_checksum(unsigned char *i, unsigned char ln)
{
  unsigned char j, tempq = 0;
  i += 1;
  for (j = 0; j < (ln - 2); j++)
  {
    tempq += *i;
    i++;
  }
  tempq = (~tempq) + 1; return (tempq);
}

void add_buff(int16_t val)
{
  buff[buff_index] = val;
  buff_index++;
  buff_index %= NUM_ELEM;
}

int32_t avg_buff()
{
  int32_t res = 0;
  for (int16_t i = 0; i < NUM_ELEM; i++)
  {
    res += buff[i];
  }
  res /= NUM_ELEM;
  return (res);
}

void sensor_read()
{
  if (Serial1.available() > 0)
  {
    byte buff[8];
    Serial1.readBytes(buff, 9);
    if (get_checksum(buff, 9) == buff[8])
    {
      int tmp = buff[4] * 256 + buff[5];
      if (tmp >= 0 && tmp <= 10000)
      {
        sensor.ppb = tmp;
        sensor.prev_ppb = -1;
        sensor.attempts = 0;
      }
    }
  }
}

void sensor_check_working()
{
  if (millis() - sensor.attempts_millis > 1000)
  {
    sensor.attempts_millis = millis();

    if (sensor.attempts >= 5) sensor.state = 0;
    else 
    {
      sensor.attempts++;
      sensor.state = 1;
    }
  }
}

// -------------------------------------------------------------------------------------------------------------------------
// ;nextion_util
// -------------------------------------------------------------------------------------------------------------------------
bool compare_array(uint8_t *a, uint8_t *b)
{
  for (uint8_t i = 0; i < BUFFER_SIZE; i++)
  {
    if (a[i] != b[i])
    {
      return false;
    }
  }
  return true;
}

void nextion_clear_buffer()
{
  for (int i = 0; i < BUFFER_SIZE; i++)
    buffer_nextion[i] = 0;
}

bool nextionExecCommand(uint8_t arr[], uint8_t arr_size)
{
  for (uint8_t i = 0; i < arr_size; i++)
  {
    Serial.write(arr[i]);
  }
}

void nextion_debug_serial()
{
  for (int i = 0; i < BUFFER_SIZE; i++)
  {
    Serial.print(buffer_nextion[i]);
    Serial.print(" ");
  }
  Serial.println();
}

// -------------------------------------------------------------------------------------------------------------------------
// ;programs
// -------------------------------------------------------------------------------------------------------------------------
/* set curr_programs based on selprog */
void programs_get_current()
{
  if (selprog.type == 0)
  {
    switch (rtc.dayofweek)
    {
      case 0:
        curr_programs = &sunday_programs;
        break;
      case 1:
        curr_programs = &monday_programs;
        break;
      case 2:
        curr_programs = &tuesday_programs;
        break;
      case 3:
        curr_programs = &wednesday_programs;
        break;
      case 4:
        curr_programs = &thursday_programs;
        break;
      case 5:
        curr_programs = &friday_programs;
        break;
      case 6:
        curr_programs = &saturday_programs;
        break;
    }
  }
  else
  {
    curr_programs = &week_programs;
  }
}

void listprog_add(programs_t *curr_programs)
{
  if (tmp_prog.time_start != 0 || tmp_prog.time_end != 0)
  {
    if (curr_programs->index < NUM_MAX_PROGRAMS)
    {
      curr_programs->programs[curr_programs->index].time_start = tmp_prog.time_start;
      curr_programs->programs[curr_programs->index].time_end = tmp_prog.time_end;
      eeprom_write_int(curr_programs->eeprom_base_address + 10 + (4 * curr_programs->index) + 0, tmp_prog.time_start);
      eeprom_write_int(curr_programs->eeprom_base_address + 10 + (4 * curr_programs->index) + 2, tmp_prog.time_end);
      curr_programs->index++;
      eeprom_write_byte(curr_programs->eeprom_base_address, curr_programs->index);
      nextion_goto_page_listprog();
    }
  }
}

void listprog_delete(programs_t *curr_programs)
{
  if (curr_programs->index > 0)
  {
    curr_programs->programs[curr_listprog_index] = curr_programs->programs[curr_programs->index - 1];
    curr_programs->programs[curr_programs->index].time_start = 0;
    curr_programs->programs[curr_programs->index].time_end = 0;
    eeprom_write_int(curr_programs->eeprom_base_address + 10 + (4 * curr_listprog_index) + 0, curr_programs->programs[curr_programs->index - 1].time_start);
    eeprom_write_int(curr_programs->eeprom_base_address + 10 + (4 * curr_listprog_index) + 2, curr_programs->programs[curr_programs->index - 1].time_end);
    curr_programs->index--;
    eeprom_write_byte(curr_programs->eeprom_base_address, curr_programs->index);
    curr_listprog_index = 0;
  }
}

void listprog_prev(programs_t *curr_programs)
{
  curr_listprog_index--;
  if (curr_listprog_index < 0) curr_listprog_index = curr_programs->index - 1;
}

void listprog_next(programs_t *curr_programs)
{
  curr_listprog_index++;
  if (curr_listprog_index > curr_programs->index - 1) curr_listprog_index = 0;
}

// -------------------------------------------------------------------------------------------------------------------------
// ;nextion_read
// -------------------------------------------------------------------------------------------------------------------------
void nextion_listen()
{
  if (Serial.available())
  {
    new_data = true;
    buffer_nextion[buffer_counter] = Serial.read();
    if (buffer_counter < BUFFER_SIZE) buffer_counter++;
    nextion_current_millis = millis();
  }
  if (new_data)
  {
    if ((millis() - nextion_current_millis) > 10)
    {
      new_data = false;
      buffer_counter = 0;
      nextion_eval_serial();

      //nextion_debug_serial();
      nextion_clear_buffer();
    }
  }
}

void nextion_eval_serial()
{
  switch (nextion.current_page)
  {
    case page_dashboard:
      {
        if (compare_array(cmd_dashboard_gear_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_dashboard_onoff_icon, buffer_nextion))
        {
          onoff.state = !onoff.state;
          eeprom_write_int(onoff.eeprom_state_address, onoff.state);
        }
      } break;
    case page_settings:
      {
        if (compare_array(cmd_settings_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_dashboard();
        }
        else if (compare_array(cmd_settings_select_icon, buffer_nextion))
        {
          nextion_goto_page_selprog();
        }
        else if (compare_array(cmd_settings_calendar_icon, buffer_nextion))
        {
          nextion_goto_page_setprogweek();
        }
        else if (compare_array(cmd_settings_cycle_icon, buffer_nextion))
        {
          nextion_goto_page_setcycle();
        }
        else if (compare_array(cmd_settings_clock_icon, buffer_nextion))
        {
          nextion_goto_page_setclock();
        }
        else if (compare_array(cmd_settings_sd_icon, buffer_nextion))
        {
          nextion_goto_page_sd();
        }
        else if (compare_array(cmd_settings_power_icon, buffer_nextion))
        {
          nextion_goto_page_power();
        }
        else if (compare_array(cmd_settings_infosys_icon, buffer_nextion))
        {
          nextion_goto_page_infosys();
        }
      } break;
    case page_selprog:
      {
        if (compare_array(cmd_selprog_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_selprog_save_icon, buffer_nextion))
        {
          selprog.type = selprog.tmp_type;
          eeprom_write_byte(selprog.eeprom_type_address, selprog.type);
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_selprog_prog_leftarrow_icon, buffer_nextion))
        {
          selprog.tmp_type--;
          if (selprog.tmp_type < 0) selprog.tmp_type = 1;
        }
        else if (compare_array(cmd_selprog_prog_rightarrow_icon, buffer_nextion))
        {
          selprog.tmp_type++;
          if (selprog.tmp_type > 1) selprog.tmp_type = 0;
        }
      } break;
    case page_setprogweek:
      {
        if (compare_array(cmd_setprog_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_setprog_daily_button, buffer_nextion))
        {
          nextion_goto_page_setprogday();
        }
        else if (compare_array(cmd_setprog_weekly_button, buffer_nextion))
        {
          curr_setprog = listprog_weekly;
          nextion_goto_page_listprog();
        }
      } break;
    case page_setprogday:
      {
        if (compare_array(cmd_setprogday_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_setprogweek();
        }
        else if (compare_array(cmd_setprogday_monday_button, buffer_nextion))
        {
          curr_setprog = listprog_monday;
          nextion_goto_page_listprog();
        }
        else if (compare_array(cmd_setprogday_tuesday_button, buffer_nextion))
        {
          curr_setprog = listprog_tuesday;
          nextion_goto_page_listprog();
        }
        else if (compare_array(cmd_setprogday_wednesday_button, buffer_nextion))
        {
          curr_setprog = listprog_wednesday;
          nextion_goto_page_listprog();
        }
        else if (compare_array(cmd_setprogday_thursday_button, buffer_nextion))
        {
          curr_setprog = listprog_thursday;
          nextion_goto_page_listprog();
        }
        else if (compare_array(cmd_setprogday_friday_button, buffer_nextion))
        {
          curr_setprog = listprog_friday;
          nextion_goto_page_listprog();
        }
        else if (compare_array(cmd_setprogday_saturday_button, buffer_nextion))
        {
          curr_setprog = listprog_saturday;
          nextion_goto_page_listprog();
        }
        else if (compare_array(cmd_setprogday_sunday_button, buffer_nextion))
        {
          curr_setprog = listprog_sunday;
          nextion_goto_page_listprog();
        }
      } break;
    case page_listprog:
      {
        if (compare_array(cmd_listprog_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_setprogweek();
        }
        else if (compare_array(cmd_listprog_add_icon, buffer_nextion))
        {
          /* check if reached max num programs */
          programs_t *tmp_setprog = NULL;
          switch (curr_setprog)
          {
            case listprog_weekly:
              tmp_setprog = &week_programs;
              break;
            case listprog_monday:
              tmp_setprog = &monday_programs;
              break;
            case listprog_tuesday:
              tmp_setprog = &tuesday_programs;
              break;
            case listprog_wednesday:
              tmp_setprog = &wednesday_programs;
              break;
            case listprog_thursday:
              tmp_setprog = &thursday_programs;
              break;
            case listprog_friday:
              tmp_setprog = &friday_programs;
              break;
            case listprog_saturday:
              tmp_setprog = &saturday_programs;
              break;
            case listprog_sunday:
              tmp_setprog = &sunday_programs;
              break;
          }
          if (tmp_setprog->index < NUM_MAX_PROGRAMS)
          {
            tmp_prog.time_start = 0;
            tmp_prog.time_end = 0;
            nextion_goto_page_addprog();
          }
        }
        else if (compare_array(cmd_listprog_prog_leftdoublearrow_icon, buffer_nextion))
        {
          switch (curr_setprog)
          {
            case listprog_weekly:
              listprog_prev(&week_programs);
              break;
            case listprog_monday:
              listprog_prev(&monday_programs);
              break;
            case listprog_tuesday:
              listprog_prev(&tuesday_programs);
              break;
            case listprog_wednesday:
              listprog_prev(&wednesday_programs);
              break;
            case listprog_thursday:
              listprog_prev(&thursday_programs);
              break;
            case listprog_friday:
              listprog_prev(&friday_programs);
              break;
            case listprog_saturday:
              listprog_prev(&saturday_programs);
              break;
            case listprog_sunday:
              listprog_prev(&sunday_programs);
              break;
          }
        }
        else if (compare_array(cmd_listprog_prog_rightdoublearrow_icon, buffer_nextion))
        {
          switch (curr_setprog)
          {
            case listprog_weekly:
              listprog_next(&week_programs);
              break;
            case listprog_monday:
              listprog_next(&monday_programs);
              break;
            case listprog_tuesday:
              listprog_next(&tuesday_programs);
              break;
            case listprog_wednesday:
              listprog_next(&wednesday_programs);
              break;
            case listprog_thursday:
              listprog_next(&thursday_programs);
              break;
            case listprog_friday:
              listprog_next(&friday_programs);
              break;
            case listprog_saturday:
              listprog_next(&saturday_programs);
              break;
            case listprog_sunday:
              listprog_next(&sunday_programs);
              break;
          }
        }
        else if (compare_array(cmd_listprog_prog_delete_icon, buffer_nextion))
        {
          switch (curr_setprog)
          {
            case listprog_weekly:
              listprog_delete(&week_programs);
              break;
            case listprog_monday:
              listprog_delete(&monday_programs);
              break;
            case listprog_tuesday:
              listprog_delete(&tuesday_programs);
              break;
            case listprog_wednesday:
              listprog_delete(&wednesday_programs);
              break;
            case listprog_thursday:
              listprog_delete(&thursday_programs);
              break;
            case listprog_friday:
              listprog_delete(&friday_programs);
              break;
            case listprog_saturday:
              listprog_delete(&saturday_programs);
              break;
            case listprog_sunday:
              listprog_delete(&sunday_programs);
              break;
          }
        }
      } break;
    case page_addprog:
      {
        if (compare_array(cmd_addprog_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_listprog();
        }
        else if (compare_array(cmd_addprog_save_icon, buffer_nextion))
        {
          switch (curr_setprog)
          {
            case listprog_weekly:
              listprog_add(&week_programs);
              break;
            case listprog_monday:
              listprog_add(&monday_programs);
              break;
            case listprog_tuesday:
              listprog_add(&tuesday_programs);
              break;
            case listprog_wednesday:
              listprog_add(&wednesday_programs);
              break;
            case listprog_thursday:
              listprog_add(&thursday_programs);
              break;
            case listprog_friday:
              listprog_add(&friday_programs);
              break;
            case listprog_saturday:
              listprog_add(&saturday_programs);
              break;
            case listprog_sunday:
              listprog_add(&sunday_programs);
              break;
          }
        }
        else if (compare_array(cmd_addprog_startarrow_icon, buffer_nextion))
        {
          nextion_goto_page_addprogfrom();
        }
        else if (compare_array(cmd_addprog_endarrow_icon, buffer_nextion))
        {
          nextion_goto_page_addprogto();
        }
      } break;
    case page_addprogfrom:
      {
        if (compare_array(cmd_addprogfrom_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_addprog();
        }
        else if (compare_array(cmd_addprogfrom_save_icon, buffer_nextion))
        {
          tmp_prog.time_start = tmp_prog.hh_start * 60 + tmp_prog.mm_start;
          nextion_goto_page_addprog();
        }
        else if (compare_array(cmd_addprogfrom_hh_leftarrow_icon, buffer_nextion))
        {
          tmp_prog.hh_start--;
          if (tmp_prog.hh_start < 0) tmp_prog.hh_start = 23;
        }
        else if (compare_array(cmd_addprogfrom_hh_rightarrow_icon, buffer_nextion))
        {
          tmp_prog.hh_start++;
          if (tmp_prog.hh_start > 23) tmp_prog.hh_start = 0;
        }
        else if (compare_array(cmd_addprogfrom_mm_leftarrow_icon, buffer_nextion))
        {
          tmp_prog.mm_start--;
          if (tmp_prog.mm_start < 0) tmp_prog.mm_start = 59;
        }
        else if (compare_array(cmd_addprogfrom_mm_rightarrow_icon, buffer_nextion))
        {
          tmp_prog.mm_start++;
          if (tmp_prog.mm_start > 59) tmp_prog.mm_start = 0;
        }
      } break;
    case page_addprogto:
      {
        if (compare_array(cmd_addprogto_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_addprog();
        }
        else if (compare_array(cmd_addprogto_save_icon, buffer_nextion))
        {
          tmp_prog.time_end = tmp_prog.hh_end * 60 + tmp_prog.mm_end;
          nextion_goto_page_addprog();
        }
        else if (compare_array(cmd_addprogto_hh_leftarrow_icon, buffer_nextion))
        {
          tmp_prog.hh_end--;
          if (tmp_prog.hh_end < 0) tmp_prog.hh_end = 23;
        }
        else if (compare_array(cmd_addprogto_hh_rightarrow_icon, buffer_nextion))
        {
          tmp_prog.hh_end++;
          if (tmp_prog.hh_end > 23) tmp_prog.hh_end = 0;
        }
        else if (compare_array(cmd_addprogto_mm_leftarrow_icon, buffer_nextion))
        {
          tmp_prog.mm_end--;
          if (tmp_prog.mm_end < 0) tmp_prog.mm_end = 59;
        }
        else if (compare_array(cmd_addprogto_mm_rightarrow_icon, buffer_nextion))
        {
          tmp_prog.mm_end++;
          if (tmp_prog.mm_end > 59) tmp_prog.mm_end = 0;
        }
      } break;
    case page_setcycle:
      {
        if (compare_array(cmd_setcycle_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_setcycle_save_icon, buffer_nextion))
        {
          cycle.time_on = cycle.tmp_time_on;
          cycle.time_off = cycle.tmp_time_off;
          eeprom_write_int(cycle.eeprom_time_on_address, cycle.time_on);
          eeprom_write_int(cycle.eeprom_time_off_address, cycle.time_off);
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_setcycle_on_leftarrow_icon, buffer_nextion))
        {
          cycle.tmp_time_on--;
          if (cycle.tmp_time_on < 0) cycle.tmp_time_on = 0;
        }
        else if (compare_array(cmd_setcycle_on_rightarrow_icon, buffer_nextion))
        {
          cycle.tmp_time_on++;
          if (cycle.tmp_time_on > 60) cycle.tmp_time_on = 60;
        }
        else if (compare_array(cmd_setcycle_off_leftarrow_icon, buffer_nextion))
        {
          cycle.tmp_time_off--;
          if (cycle.tmp_time_off < 0) cycle.tmp_time_off = 0;
        }
        else if (compare_array(cmd_setcycle_off_rightarrow_icon, buffer_nextion))
        {
          cycle.tmp_time_off++;
          if (cycle.tmp_time_off > 60) cycle.tmp_time_off = 60;
        }
      } break;
    case page_setclock:
      {
        if (compare_array(cmd_setclock_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_setclock_ymdarrow_icon, buffer_nextion))
        {
          nextion_goto_page_setclockymd();
        }
        else if (compare_array(cmd_setclock_hmsarrow_icon, buffer_nextion))
        {
          nextion_goto_page_setclockhms();
        }
      } break;
    case page_setclockymd:
      {
        if (compare_array(cmd_setclockymd_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_setclock();
        }
        else if (compare_array(cmd_setclockymd_save_icon, buffer_nextion))
        {
          rtc.year = rtc.tmp_year;
          rtc.month = rtc.tmp_month;
          rtc.day = rtc.tmp_day;
          rtc_ds3231.adjust(DateTime(rtc.year, rtc.month, rtc.day, rtc.hour, rtc.minute, rtc.second));
          nextion_goto_page_setclock();
        }
        else if (compare_array(cmd_setclockymd_yy_leftarrow_icon, buffer_nextion))
        {
          rtc.tmp_year--;
          if (rtc.tmp_year < 2000) rtc.tmp_year = 2100;
          rtc.tmp_day = 1;
        }
        else if (compare_array(cmd_setclockymd_yy_rightarrow_icon, buffer_nextion))
        {
          rtc.tmp_year++;
          if (rtc.tmp_year > 2100) rtc.tmp_year = 2000;
          rtc.tmp_day = 1;
        }
        else if (compare_array(cmd_setclockymd_mm_leftarrow_icon, buffer_nextion))
        {
          rtc.tmp_month--;
          if (rtc.tmp_month < 1) rtc.tmp_month = 12;
          rtc.tmp_day = 1;
        }
        else if (compare_array(cmd_setclockymd_mm_rightarrow_icon, buffer_nextion))
        {
          rtc.tmp_month++;
          if (rtc.tmp_month > 12) rtc.tmp_month = 1;
          rtc.tmp_day = 1;
        }
        else if (compare_array(cmd_setclockymd_dd_leftarrow_icon, buffer_nextion))
        {
          rtc.tmp_day--;
          if (rtc.tmp_day < 1)
          {
            if (rtc.tmp_month == january) rtc.tmp_day = 31;
            else if (rtc.tmp_month == february)
            {
              if(rtc.tmp_year % 4 == 0 && rtc.tmp_year % 100 != 0 || rtc.tmp_year % 400 == 0)
              {
                rtc.tmp_day = 29;
              }
              else
              {
                rtc.tmp_day = 28;
              }
            }
            else if (rtc.tmp_month == march) rtc.tmp_day = 31;
            else if (rtc.tmp_month == april) rtc.tmp_day = 30;
            else if (rtc.tmp_month == may) rtc.tmp_day = 31;
            else if (rtc.tmp_month == june) rtc.tmp_day = 30;
            else if (rtc.tmp_month == july) rtc.tmp_day = 31;
            else if (rtc.tmp_month == august) rtc.tmp_day = 31;
            else if (rtc.tmp_month == september) rtc.tmp_day = 30;
            else if (rtc.tmp_month == october) rtc.tmp_day = 31;
            else if (rtc.tmp_month == november) rtc.tmp_day = 30;
            else if (rtc.tmp_month == december) rtc.tmp_day = 31;
          }
        }
        else if (compare_array(cmd_setclockymd_dd_rightarrow_icon, buffer_nextion))
        {
          rtc.tmp_day++;
          if (rtc.tmp_month == january && rtc.tmp_day > 31) rtc.tmp_day = 1;
          else if (rtc.tmp_month == february) 
          {
            if(rtc.tmp_year % 4 == 0 && rtc.tmp_year % 100 != 0 || rtc.tmp_year % 400 == 0)
              {
                if(rtc.tmp_day > 29) rtc.tmp_day = 1;
              }
              else
              {
                if(rtc.tmp_day > 28) rtc.tmp_day = 1;
              }
          }
          else if (rtc.tmp_month == march && rtc.tmp_day > 31) rtc.tmp_day = 1;
          else if (rtc.tmp_month == april && rtc.tmp_day > 30) rtc.tmp_day = 1;
          else if (rtc.tmp_month == may && rtc.tmp_day > 31) rtc.tmp_day = 1;
          else if (rtc.tmp_month == june && rtc.tmp_day > 30) rtc.tmp_day = 1;
          else if (rtc.tmp_month == july && rtc.tmp_day > 31) rtc.tmp_day = 1;
          else if (rtc.tmp_month == august && rtc.tmp_day > 31) rtc.tmp_day = 1;
          else if (rtc.tmp_month == september && rtc.tmp_day > 30) rtc.tmp_day = 1;
          else if (rtc.tmp_month == october && rtc.tmp_day > 31) rtc.tmp_day = 1;
          else if (rtc.tmp_month == november && rtc.tmp_day > 30) rtc.tmp_day = 1;
          else if (rtc.tmp_month == december && rtc.tmp_day > 31) rtc.tmp_day = 1;
        }
      } break;
    case page_setclockhms:
      {
        if (compare_array(cmd_setclockhms_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_setclock();
        }
        else if (compare_array(cmd_setclockhms_save_icon, buffer_nextion))
        {
          rtc.hour = rtc.tmp_hour;
          rtc.minute = rtc.tmp_minute;
          rtc.second = rtc.tmp_second;
          rtc_ds3231.adjust(DateTime(rtc.year, rtc.month, rtc.day, rtc.hour, rtc.minute, rtc.second));
          nextion_goto_page_setclock();
        }
        else if (compare_array(cmd_setclockhms_hh_leftarrow_icon, buffer_nextion))
        {
          rtc.tmp_hour--;
          if (rtc.tmp_hour > 23) rtc.tmp_hour = 23;
        }
        else if (compare_array(cmd_setclockhms_hh_rightarrow_icon, buffer_nextion))
        {
          rtc.tmp_hour++;
          rtc.tmp_hour %= 24;
        }
        else if (compare_array(cmd_setclockhms_mm_leftarrow_icon, buffer_nextion))
        {
          rtc.tmp_minute--;
          if (rtc.tmp_minute > 59) rtc.tmp_minute = 59;
        }
        else if (compare_array(cmd_setclockhms_mm_rightarrow_icon, buffer_nextion))
        {
          rtc.tmp_minute++;
          rtc.tmp_minute %= 60;
        }
        else if (compare_array(cmd_setclockhms_ss_leftarrow_icon, buffer_nextion))
        {
          rtc.tmp_second--;
          if (rtc.tmp_second > 59) rtc.tmp_second = 59;
        }
        else if (compare_array(cmd_setclockhms_ss_rightarrow_icon, buffer_nextion))
        {
          rtc.tmp_second++;
          rtc.tmp_second %= 60;
        }
      } break;
    case page_analytics:
      {
        if (compare_array(cmd_analytics_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
      } break;
    case page_sd:
      {
        if (compare_array(cmd_sd_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
      } break;
    case page_power:
      {
        if (compare_array(cmd_power_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_power_save_icon, buffer_nextion))
        {
          power.type = power.tmp_type;
          power.manual_val = power.tmp_manual_val;
          eeprom_write_byte(power.eeprom_type_address, power.type);
          eeprom_write_byte(power.eeprom_manual_val_address, power.manual_val);
          eeprom_write_int(onoff.eeprom_state_address, onoff.state);
          nextion_goto_page_settings();
        }
        else if (compare_array(cmd_power_type_leftarrow_icon, buffer_nextion))
        {
          power.tmp_type--;
          if (power.tmp_type < 0) power.tmp_type = 1;
        }
        else if (compare_array(cmd_power_type_rightarrow_icon, buffer_nextion))
        {
          power.tmp_type++;
          if (power.tmp_type > 1) power.tmp_type = 0;
        }
        else if (compare_array(cmd_power_manual_val_leftarrow_icon, buffer_nextion))
        {
          power.tmp_manual_val--;
          if (power.tmp_manual_val < 0) power.tmp_manual_val = 1;
        }
        else if (compare_array(cmd_power_manual_val_rightarrow_icon, buffer_nextion))
        {
          power.tmp_manual_val++;
          if (power.tmp_manual_val > 1) power.tmp_manual_val = 0;
        }
      } break;
    case page_infosys:
      {
        if (compare_array(cmd_infosys_backarrow_icon, buffer_nextion))
        {
          nextion_goto_page_settings();
        }
      } break;
  }
}

/* --------------------------------------------------------------------- */
/* ;nextion write
  /* --------------------------------------------------------------------- */
bool rtc_manager(uint8_t arr[], uint8_t arr_size)
{
  for (uint8_t i = 0; i < arr_size; i++)
  {
    Serial.write(arr[i]);
  }
}

void nextion_goto_page_dashboard()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6F, 0x61, 0x72, 0x64, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_dashboard;
  nextion.refresh = 1;
}
void nextion_goto_page_settings()
{
  uint8_t buff[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x73, 0x65, 0x74, 0x74, 0x69, 0x6E, 0x67, 0x73, 0xff, 0xff, 0xff};
  rtc_manager(buff, sizeof(buff));
  nextion.current_page = page_settings;
  nextion.refresh = 1;
}
void nextion_goto_page_selprog()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x73, 0x65, 0x6C, 0x70, 0x72, 0x6F, 0x67, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_selprog;
  nextion.refresh = 1;
}
void nextion_goto_page_setprogweek()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x73, 0x65, 0x74, 0x70, 0x72, 0x6F, 0x67, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_setprogweek;
  nextion.refresh = 1;
}
void nextion_goto_page_setprogday()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x73, 0x65, 0x74, 0x70, 0x72, 0x6F, 0x67, 0x64, 0x61, 0x79, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_setprogday;
  nextion.refresh = 1;
}
void nextion_goto_page_listprog()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x6C, 0x69, 0x73, 0x74, 0x70, 0x72, 0x6F, 0x67, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_listprog;
  nextion.refresh = 1;
}
void nextion_goto_page_addprog()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x61, 0x64, 0x64, 0x70, 0x72, 0x6F, 0x67, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_addprog;
  nextion.refresh = 1;
}
void nextion_goto_page_addprogfrom()
{
  uint8_t cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x61, 0x64, 0x64, 0x70, 0x72, 0x6F, 0x67, 0x66, 0x72, 0x6F, 0x6D, 0xff, 0xff, 0xff};
  rtc_manager(cmd, sizeof(cmd));
  nextion.current_page = page_addprogfrom;
  nextion.refresh = 1;
}
void nextion_goto_page_addprogto()
{
  uint8_t cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x61, 0x64, 0x64, 0x70, 0x72, 0x6F, 0x67, 0x74, 0x6F, 0xff, 0xff, 0xff};
  rtc_manager(cmd, sizeof(cmd));
  nextion.current_page = page_addprogto;
  nextion.refresh = 1;
}
void nextion_goto_page_setcycle()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x73, 0x65, 0x74, 0x63, 0x79, 0x63, 0x6C, 0x65, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_setcycle;
  nextion.refresh = 1;
}
void nextion_goto_page_setclock()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x73, 0x65, 0x74, 0x63, 0x6C, 0x6F, 0x63, 0x6B, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_setclock;
  nextion.refresh = 1;
}
void nextion_goto_page_setclockymd()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x73, 0x65, 0x74, 0x63, 0x6C, 0x6F, 0x63, 0x6B, 0x79, 0x6D, 0x64, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_setclockymd;
  nextion.refresh = 1;
}
void nextion_goto_page_setclockhms()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x73, 0x65, 0x74, 0x63, 0x6C, 0x6F, 0x63, 0x6B, 0x68, 0x6D, 0x73, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_setclockhms;
  nextion.refresh = 1;
}
void nextion_goto_page_sd()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x69, 0x6E, 0x66, 0x6F, 0x73, 0x64, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_sd;
  nextion.refresh = 1;
}
void nextion_goto_page_power()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x6F, 0x77, 0x65, 0x72, 0x6F, 0x6E, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_power;
  nextion.refresh = 1;
}
void nextion_goto_page_infosys()
{
  uint8_t _cmd[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x69, 0x6E, 0x66, 0x6F, 0x73, 0x79, 0x73, 0xff, 0xff, 0xff};
  rtc_manager(_cmd, sizeof(_cmd));
  nextion.current_page = page_infosys;
  nextion.refresh = 1;
}

/* --------------------------------------------------------------------- */
/* ;render nextion */
/* --------------------------------------------------------------------- */
void render_page_dashboard()
{
  if (nextion.refresh ||
      onoff.prev_state != onoff.state ||
      rtc.prev_second != rtc.second ||
      relay.prev_state != relay.curr_state ||
      sensor.prev_ppb != sensor.ppb)
  {
    if (nextion.refresh)
    {
      nextion.refresh = 0;
    }
    rtc.prev_second = rtc.second;
    relay.prev_state = relay.curr_state;
    onoff.prev_state = onoff.state;
    sensor.prev_ppb = sensor.ppb;

    {
      if (onoff.state == 1)
      {
        uint8_t buff[] = {0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x34, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
      else
      {
        uint8_t buff[] = {0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x33, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
    }

    {
      /* onoff: 0=off, 1=on|standby */
      if (onoff.state == 1)
      {
        if (cycle_time_in_program_range() == 1)
        {
          uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x69, 0x73, 0x74, 0x65, 0x6D, 0x61, 0x20, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        else
        {
          uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x69, 0x73, 0x74, 0x65, 0x6D, 0x61, 0x20, 0x53, 0x54, 0x41, 0x4E, 0x44, 0x42, 0x59, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
      }
      else if (onoff.state == 0)
      {
        uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x69, 0x73, 0x74, 0x65, 0x6D, 0x61, 0x20, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
    }
    {
      /* selprog: 0=giornaliero, 1=settimanale */
      if (selprog.type == 0)
      {
        uint8_t buff[] = {0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x72, 0x6F, 0x67, 0x2E, 0x20, 0x47, 0x69, 0x6F, 0x72, 0x6E, 0x61, 0x6C, 0x69, 0x65, 0x72, 0x6F, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
      else
      {
        uint8_t buff[] = {0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x72, 0x6F, 0x67, 0x2E, 0x20, 0x53, 0x65, 0x74, 0x74, 0x69, 0x6D, 0x61, 0x6E, 0x61, 0x6C, 0x65, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
    }
    {
      /* time ciclo on */
      uint8_t buff[] = {0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x43, 0x69, 0x63, 0x6C, 0x6F, 0x20, 0x4F, 0x4E, 0x20, 0x30, 0x30, 0x6D, 0x69, 0x6E, 0x22, 0xff, 0xff, 0xff};
      buff[17] = (cycle.time_on % 100 / 10) + 0x30;
      buff[18] = (cycle.time_on % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      /* time ciclo off */
      uint8_t buff[] = {0x74, 0x34, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x43, 0x69, 0x63, 0x6C, 0x6F, 0x20, 0x4F, 0x46, 0x46, 0x20, 0x30, 0x30, 0x6D, 0x69, 0x6E, 0x22, 0xff, 0xff, 0xff};
      buff[18] = (cycle.time_off % 100 / 10) + 0x30;
      buff[19] = (cycle.time_off % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      /* sensor */
      uint8_t buff[] = {0x74, 0x35, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x7A, 0x6F, 0x6E, 0x6F, 0x20, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
      if (sensor.state == 1)
      {
        buff[14] = (sensor.ppb % 10000 / 1000) + 0x30;
        buff[16] = (sensor.ppb % 1000 / 100) + 0x30;
        buff[17] = (sensor.ppb % 100 / 10) + 0x30;
        buff[18] = (sensor.ppb % 10 / 1) + 0x30;
      }
      else
      {
        buff[14] = 0x3F;
        buff[16] = 0x3F;
        buff[17] = 0x3F;
        buff[18] = 0x3F;
      }
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      /* rtc time */
      uint8_t buff[] = {0x74, 0x31, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[9] = (rtc.day % 100 / 10) + 0x30;
      buff[10] = (rtc.day % 10 / 1) + 0x30;
      buff[12] = (rtc.month % 100 / 10) + 0x30;
      buff[13] = (rtc.month % 10 / 1) + 0x30;
      buff[15] = (rtc.year % 10000 / 1000) + 0x30;
      buff[16] = (rtc.year % 1000 / 100) + 0x30;
      buff[17] = (rtc.year % 100 / 10) + 0x30;
      buff[18] = (rtc.year % 10 / 1) + 0x30;
      buff[20] = (rtc.hour % 100 / 10) + 0x30;
      buff[21] = (rtc.hour % 10 / 1) + 0x30;
      buff[23] = (rtc.minute % 100 / 10) + 0x30;
      buff[24] = (rtc.minute % 10 / 1) + 0x30;
      buff[26] = (rtc.second % 100 / 10) + 0x30;
      buff[27] = (rtc.second % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    /* rtc day of week */
    switch (rtc.dayofweek)
    {
      case dayofweek_sunday:
        {
          uint8_t buff[] = {0x74, 0x31, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x4F, 0x4D, 0x45, 0x4E, 0x49, 0x43, 0x41, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        } break;
      case dayofweek_monday:
        {
          uint8_t buff[] = {0x74, 0x31, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x55, 0x4E, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        } break;
      case dayofweek_tuesday:
        {
          uint8_t buff[] = {0x74, 0x31, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x41, 0x52, 0x54, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        } break;
      case dayofweek_wednesday:
        {
          uint8_t buff[] = {0x74, 0x31, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x45, 0x52, 0x43, 0x4F, 0x4C, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        } break;
      case dayofweek_thursday:
        {
          uint8_t buff[] = {0x74, 0x31, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x49, 0x4F, 0x56, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        } break;
      case dayofweek_friday:
        {
          uint8_t buff[] = {0x74, 0x31, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x45, 0x4E, 0x45, 0x52, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        } break;
      case dayofweek_saturday:
        {
          uint8_t buff[] = {0x74, 0x31, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x41, 0x42, 0x41, 0x54, 0x4F, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        } break;
    }
    {
      /* sd */
      if (sd_card.state == 1)
      {
        uint8_t buff[] = {0x74, 0x36, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x44, 0x20, 0x49, 0x6E, 0x73, 0x65, 0x72, 0x69, 0x74, 0x61, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
      else
      {
        uint8_t buff[] = {0x74, 0x36, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x44, 0x20, 0x52, 0x69, 0x6D, 0x6F, 0x73, 0x73, 0x61, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
    }
    {
      /* num ciclo */
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x43, 0x69, 0x63, 0x6C, 0x6F, 0x20, 0x23, 0x30, 0x30, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[15] = (cycle.id % 10000 / 1000) + 0x30;
      buff[16] = (cycle.id % 1000 / 100) + 0x30;
      buff[17] = (cycle.id % 100 / 10) + 0x30;
      buff[18] = (cycle.id % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_selprog()
{
  if (nextion.refresh ||
      selprog.prev_type != selprog.tmp_type)
  {
    selprog.prev_type = selprog.tmp_type;
    if (nextion.refresh)
    {
      nextion.refresh = 0;
      selprog.tmp_type = selprog.type;
    }

    if (selprog.tmp_type == 0)
    {
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x49, 0x4F, 0x52, 0x4E, 0x41, 0x4C, 0x49, 0x45, 0x52, 0x4F, 0x22, 0xff, 0xff, 0xff}; /* giornalero */
      nextionExecCommand(buff, sizeof(buff));
    }
    else
    {
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x45, 0x54, 0x54, 0x49, 0x4D, 0x41, 0x4E, 0x41, 0x4C, 0x45, 0x22, 0xff, 0xff, 0xff}; /* settimanale */
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_listprog_prog(programs_t *curr_programs)
{
  if (curr_programs->index == 0)
  {
    {
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x22, 0xff, 0xff, 0xff};
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      uint8_t buff[] = {0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x45, 0x53, 0x53, 0x55, 0x4E, 0x20, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x41, 0x22, 0xff, 0xff, 0xff};
      nextionExecCommand(buff, sizeof(buff));
    }
  }
  else
  {
    {
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x70, 0x72, 0x6F, 0x67, 0x72, 0x61, 0x6D, 0x20, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[16] = ((curr_listprog_index + 1) % 100 / 10) + 0x30;
      buff[17] = ((curr_listprog_index + 1) % 10 / 1) + 0x30;
      buff[19] = ((curr_programs->index) % 100 / 10) + 0x30;
      buff[20] = ((curr_programs->index) % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      uint8_t buff[] = {0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = ((curr_programs->programs[curr_listprog_index].time_start / 60) % 100 / 10) + 0x30;
      buff[9] = ((curr_programs->programs[curr_listprog_index].time_start / 60) % 10 / 1) + 0x30;
      buff[11] = ((curr_programs->programs[curr_listprog_index].time_start % 60) % 100 / 10) + 0x30;
      buff[12] = ((curr_programs->programs[curr_listprog_index].time_start % 60) % 10 / 1) + 0x30;
      buff[16] = ((curr_programs->programs[curr_listprog_index].time_end / 60) % 100 / 10) + 0x30;
      buff[17] = ((curr_programs->programs[curr_listprog_index].time_end / 60) % 10 / 1) + 0x30;
      buff[19] = ((curr_programs->programs[curr_listprog_index].time_end % 60) % 100 / 10) + 0x30;
      buff[20] = ((curr_programs->programs[curr_listprog_index].time_end % 60) % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_listprog()
{
  if (nextion.refresh ||
      prev_listprog_index != curr_listprog_index ||
      week_programs.prev_index != week_programs.index ||
      monday_programs.prev_index != monday_programs.index ||
      tuesday_programs.prev_index != tuesday_programs.index ||
      wednesday_programs.prev_index != wednesday_programs.index ||
      thursday_programs.prev_index != thursday_programs.index ||
      friday_programs.prev_index != friday_programs.index ||
      saturday_programs.prev_index != saturday_programs.index ||
      sunday_programs.prev_index != sunday_programs.index
     )
  {
    prev_listprog_index = curr_listprog_index;
    week_programs.prev_index = week_programs.index;
    monday_programs.prev_index = monday_programs.index;
    tuesday_programs.prev_index = tuesday_programs.index;
    wednesday_programs.prev_index = wednesday_programs.index;
    thursday_programs.prev_index = thursday_programs.index;
    friday_programs.prev_index = friday_programs.index;
    saturday_programs.prev_index = saturday_programs.index;
    sunday_programs.prev_index = sunday_programs.index;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
      curr_listprog_index = 0;
    }

    switch (curr_setprog)
    {
      case listprog_weekly:
        {
          uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x49, 0x20, 0x2D, 0x20, 0x53, 0x45, 0x54, 0x54, 0x49, 0x4D, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        render_page_listprog_prog(&week_programs);
        break;
      case listprog_monday:
        {
          uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x49, 0x20, 0x2D, 0x20, 0x4C, 0x55, 0x4E, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        render_page_listprog_prog(&monday_programs);
        break;
      case listprog_tuesday:
        {
          uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x49, 0x20, 0x2D, 0x20, 0x4D, 0x41, 0x52, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        render_page_listprog_prog(&tuesday_programs);
        break;
      case listprog_wednesday:
        {
          uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x49, 0x20, 0x2D, 0x20, 0x4D, 0x45, 0x52, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        render_page_listprog_prog(&wednesday_programs);
        break;
      case listprog_thursday:
        {
          uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x49, 0x20, 0x2D, 0x20, 0x47, 0x49, 0x4F, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        render_page_listprog_prog(&thursday_programs);
        break;
      case listprog_friday:
        {
          uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x49, 0x20, 0x2D, 0x20, 0x56, 0x45, 0x4E, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        render_page_listprog_prog(&friday_programs);
        break;
      case listprog_saturday:
        {
          uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x49, 0x20, 0x2D, 0x20, 0x53, 0x41, 0x42, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        render_page_listprog_prog(&saturday_programs);
        break;
      case listprog_sunday:
        {
          uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x52, 0x4F, 0x47, 0x52, 0x41, 0x4D, 0x4D, 0x49, 0x20, 0x2D, 0x20, 0x44, 0x4F, 0x4D, 0x22, 0xff, 0xff, 0xff};
          nextionExecCommand(buff, sizeof(buff));
        }
        render_page_listprog_prog(&sunday_programs);
        break;
    }
  }
}

void render_page_addprog()
{
  if (nextion.refresh ||
      tmp_prog.prev_time_start != tmp_prog.time_start ||
      tmp_prog.prev_time_end != tmp_prog.time_end)
  {
    tmp_prog.prev_time_start = tmp_prog.time_start;
    tmp_prog.prev_time_end = tmp_prog.time_end;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
    }
    {
      uint8_t hh_start = tmp_prog.time_start / 60;
      uint8_t mm_start = tmp_prog.time_start % 60;
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (hh_start % 100 / 10) + 0x30;
      buff[9] = (hh_start % 10 / 1) + 0x30;
      buff[11] = (mm_start % 100 / 10) + 0x30;
      buff[12] = (mm_start % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      uint8_t hh_end = tmp_prog.time_end / 60;
      uint8_t mm_end = tmp_prog.time_end % 60;
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (hh_end % 100 / 10) + 0x30;
      buff[9] = (hh_end % 10 / 1) + 0x30;
      buff[11] = (mm_end % 100 / 10) + 0x30;
      buff[12] = (mm_end % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_addprogfrom()
{
  if (nextion.refresh ||
      tmp_prog.prev_hh_start != tmp_prog.hh_start ||
      tmp_prog.prev_mm_start != tmp_prog.mm_start)
  {
    tmp_prog.prev_hh_start = tmp_prog.hh_start;
    tmp_prog.prev_mm_start = tmp_prog.mm_start;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
      tmp_prog.prev_hh_start = tmp_prog.hh_start = 0;
      tmp_prog.prev_mm_start = tmp_prog.mm_start = 0;
    }

    {
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (tmp_prog.hh_start % 100 / 10) + 0x30;
      buff[9] = (tmp_prog.hh_start % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (tmp_prog.mm_start % 100 / 10) + 0x30;
      buff[9] = (tmp_prog.mm_start % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_addprogto()
{
  if (nextion.refresh ||
      tmp_prog.prev_hh_end != tmp_prog.hh_end ||
      tmp_prog.prev_mm_end != tmp_prog.mm_end)
  {
    tmp_prog.prev_hh_end = tmp_prog.hh_end;
    tmp_prog.prev_mm_end = tmp_prog.mm_end;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
      tmp_prog.prev_hh_end = tmp_prog.hh_end = 0;
      tmp_prog.prev_mm_end = tmp_prog.mm_end = 0;
    }
    {
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (tmp_prog.hh_end % 100 / 10) + 0x30;
      buff[9] = (tmp_prog.hh_end % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (tmp_prog.mm_end % 100 / 10) + 0x30;
      buff[9] = (tmp_prog.mm_end % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_setcycle()
{
  if (nextion.refresh ||
      cycle.prev_time_on != cycle.tmp_time_on ||
      cycle.prev_time_off != cycle.tmp_time_off)
  {
    cycle.prev_time_on = cycle.tmp_time_on;
    cycle.prev_time_off = cycle.tmp_time_off;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
      cycle.tmp_time_on = cycle.time_on;
      cycle.tmp_time_off = cycle.time_off;
    }
    {
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (cycle.prev_time_on % 100 / 10) + 0x30;
      buff[9] = (cycle.prev_time_on % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (cycle.prev_time_off % 100 / 10) + 0x30;
      buff[9] = (cycle.prev_time_off % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_setclock()
{
  if (nextion.refresh ||
      rtc.prev_second != rtc.second)
  {
    rtc.prev_second = rtc.second;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
    }
    {
      /* yyyy/mm/dd */
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (rtc.day % 100 / 10) + 0x30;
      buff[9] = (rtc.day % 10 / 1) + 0x30;
      buff[11] = (rtc.month % 100 / 10) + 0x30;
      buff[12] = (rtc.month % 10 / 1) + 0x30;
      buff[14] = (rtc.year % 10000 / 1000) + 0x30;
      buff[15] = (rtc.year % 1000 / 100) + 0x30;
      buff[16] = (rtc.year % 100 / 10) + 0x30;
      buff[17] = (rtc.year % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      /* hh/mm/ss */
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x32, 0x33, 0x3A, 0x30, 0x38, 0x3A, 0x32, 0x31, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (rtc.hour % 100 / 10) + 0x30;
      buff[9] = (rtc.hour % 10 / 1) + 0x30;
      buff[11] = (rtc.minute % 100 / 10) + 0x30;
      buff[12] = (rtc.minute % 10 / 1) + 0x30;
      buff[14] = (rtc.second % 100 / 10) + 0x30;
      buff[15] = (rtc.second % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_setclockymd()
{
  if (nextion.refresh ||
      rtc.prev_year != rtc.tmp_year ||
      rtc.prev_month != rtc.tmp_month ||
      rtc.prev_day != rtc.tmp_day)
  {
    rtc.prev_year = rtc.tmp_year;
    rtc.prev_month = rtc.tmp_month;
    rtc.prev_day = rtc.tmp_day;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
      rtc.tmp_year = rtc.year;
      rtc.tmp_month = rtc.month;
      rtc.tmp_day = rtc.day;
    }
    {
      /* day */
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (rtc.tmp_day % 100 / 10) + 0x30;
      buff[9] = (rtc.tmp_day % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      /* month */
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (rtc.tmp_month % 100 / 10) + 0x30;
      buff[9] = (rtc.tmp_month % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      /* year */
      uint8_t buff[] = {0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (rtc.tmp_year % 10000 / 1000) + 0x30;
      buff[9] = (rtc.tmp_year % 1000 / 100) + 0x30;
      buff[10] = (rtc.tmp_year % 100 / 10) + 0x30;
      buff[11] = (rtc.tmp_year % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_setclockhms()
{
  if (nextion.refresh ||
      rtc.prev_second != rtc.tmp_second ||
      rtc.prev_minute != rtc.tmp_minute ||
      rtc.prev_hour != rtc.tmp_hour)
  {
    rtc.prev_hour = rtc.tmp_hour;
    rtc.prev_minute = rtc.tmp_minute;
    rtc.prev_second = rtc.tmp_second;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
      rtc.tmp_hour = rtc.hour;
      rtc.tmp_minute = rtc.minute;
      rtc.tmp_second = rtc.second;
    }
    {
      /* hour */
      uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (rtc.tmp_hour % 100 / 10) + 0x30;
      buff[9] = (rtc.tmp_hour % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      /* minute */
      uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (rtc.tmp_minute % 100 / 10) + 0x30;
      buff[9] = (rtc.tmp_minute % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
    {
      /* second */
      uint8_t buff[] = {0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff};
      buff[8] = (rtc.tmp_second % 100 / 10) + 0x30;
      buff[9] = (rtc.tmp_second % 10 / 1) + 0x30;
      nextionExecCommand(buff, sizeof(buff));
    }
  }
}

void render_page_sd()
{
  if (nextion.refresh ||
      sd_card.prev_is_inserted != sd_card.is_inserted)
  {
    sd_card.prev_is_inserted = sd_card.is_inserted;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
    }
    {
      if (sd_card.is_inserted)
      {
        uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x49, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
      else
      {
        uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
    }
  }
}

void render_page_power()
{
  if (nextion.refresh ||
      power.prev_type != power.tmp_type ||
      power.prev_manual_val != power.tmp_manual_val)
  {
    power.prev_type = power.tmp_type;
    power.prev_manual_val = power.tmp_manual_val;

    if (nextion.refresh)
    {
      nextion.refresh = 0;
      power.tmp_type = power.type;
      power.tmp_manual_val = power.manual_val;
    }
    {
      /* power type: 0=memoria, 1=manuale*/
      if (power.tmp_type == 0)
      {
        uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x45, 0x4D, 0x4F, 0x52, 0x49, 0x41, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
      else
      {
        uint8_t buff[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x41, 0x4E, 0x55, 0x41, 0x4C, 0x45, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
    }
    {
      /* power manual val: 0=off, 1=on*/
      if (power.tmp_manual_val == 0)
      {
        uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
      else
      {
        uint8_t buff[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff};
        nextionExecCommand(buff, sizeof(buff));
      }
    }
  }
}

void render_page_infosys()
{
  if (nextion.refresh)
  {
    if (nextion.refresh)
    {
      nextion.refresh = 0;
    }
  }
}

// ----------------------------------------------------------------------------------------------------------
// ;sd card
// ----------------------------------------------------------------------------------------------------------
void sd_manager()
{
  sd_card_init();
  sd_write_mean_sensor_val_every_60_seconds();
}

void sd_card_init()
{
  sd_card.is_inserted = (digitalRead(sd_card.pin_cd) == LOW) ? 1 : 0;

  if (sd_card.is_inserted)
  {
    if (!sd_card.tried_to_initialize)
    {
      sd_card.tried_to_initialize = 1;
      if (SD.begin(sd_card.pin)) sd_card.state = 1;
      else sd_card.state = 0;

      file = SD.open("log.txt", FILE_WRITE);
      file.print("");
      file.close();
    }
  }
  else
  {
    sd_card.tried_to_initialize = 0;
    sd_card.state = 0;
  }
}

void sd_card_wtite()
{
  if (sd_card.state == 1)
  {
    file = SD.open(String(cycle.id) + ".csv", FILE_WRITE);
    file.print(String(rtc.year));
    file.write(',');
    file.print(String(rtc.month));
    file.write(',');
    file.print(String(rtc.day));
    file.write(',');
    file.print(String(rtc.hour));
    file.write(',');
    file.print(String(rtc.minute));
    file.write(',');
    file.print(String(rtc.second));
    file.write(',');
    file.print(String(avg_buff()));
    file.write(',');
    file.write('\n');
    file.close();
  }
}

void sd_write_mean_sensor_val_every_60_seconds()
{
  if (onoff.state && cycle_time_in_program_range())
  {
    if (millis() - curr_millis >= 1000)
    {
      curr_millis = millis();

      add_buff(sensor.ppb);
      if (buff_index == 0)
      {
        sd_card_wtite();
      }
    }
  }
  else
  {
    buff_index = 0;
    curr_millis = 0;
  }
}

// ----------------------------------------------------------------------------------------------------------
// ;cycle
// ----------------------------------------------------------------------------------------------------------
int8_t cycle_time_in_program_range()
{
  int8_t found = 0;
  for (int i = 0; i < curr_programs->index; i++)
  {
    if (  rtc.time_in_minutes >= curr_programs->programs[i].time_start &&
          rtc.time_in_minutes < curr_programs->programs[i].time_end)
    {
      found = 1;
      break;
    }
  }
  return found;
}

void cycle_run_with_cooldown()
{
  onoff.in_cycle = 1;
  if (onoff.prev_in_cycle != onoff.in_cycle)
  {
    onoff.prev_in_cycle = onoff.in_cycle;
    cycle.curr_working_millis = millis();
    cycle.state = 1;
    digitalWrite(24, HIGH);
  }

  if (cycle.state == 1)
  {
    if (millis() - cycle.curr_working_millis > (uint64_t)cycle.time_on * 60 * 1000)
    {
      cycle.curr_resting_millis = millis();
      cycle.state = 0;
      digitalWrite(24, LOW);
    }
  }
  else
  {
    if (millis() - cycle.curr_resting_millis > (uint64_t)cycle.time_off * 60 * 1000)
    {
      cycle.curr_working_millis = millis();
      cycle.state = 1;
      digitalWrite(24, HIGH);
    }
  }
}

void cycle_stop()
{
  onoff.in_cycle = 0;
  if (onoff.prev_in_cycle != onoff.in_cycle)
  {
    onoff.prev_in_cycle = onoff.in_cycle;
    digitalWrite(24, LOW);
  }
  cycle.id_incremented = 0;
}

void cycle_inc_id()
{
  if (!cycle.id_incremented)
  {
    cycle.id_incremented = 1;
    cycle.id = eeprom_read_int(cycle.eeprom_id_address);
    cycle.id++;
    eeprom_write_int(cycle.eeprom_id_address, cycle.id);
  }
}

void cycle_manager()
{
  if (onoff.state && cycle_time_in_program_range())
  {
    cycle_inc_id();
    cycle_run_with_cooldown();

    if (millis() - curr_millis >= 1000)
    {
      curr_millis = millis();
      add_buff(sensor.ppb);
      if (buff_index == 0)
      {
        sd_card_wtite();
      }
    }
  }
  else
  {
    cycle_stop();
  }
}

// ----------------------------------------------------------------------------------------------------------
// ;rtc
// ----------------------------------------------------------------------------------------------------------
void rtc_manager()
{
  now = rtc_ds3231.now();
  rtc.year = now.year();
  rtc.month = now.month();
  rtc.day = now.day();
  rtc.hour = now.hour();
  rtc.minute = now.minute();
  rtc.second = now.second();
  rtc.dayofweek = now.dayOfTheWeek();
  rtc.time_in_minutes = ((int16_t)rtc.hour * 60) + (int16_t)rtc.minute;
}

// -------------------------------------------------------------------------------------------------------------------------
// ;setup
// -------------------------------------------------------------------------------------------------------------------------
void setup()
{
  /* ;onoff init */
  onoff.eeprom_state_address = 2;

  /* ;power init */
  power.eeprom_type_address = 4;
  power.eeprom_manual_val_address = 5;

  /* ;selprog init */
  selprog.eeprom_type_address = 6;

  /* ;sd init */
  sd_card.pin = 4;
  sd_card.pin_cd = 3;

  /* ;cycle init */
  cycle.eeprom_id_address = 10;
  cycle.eeprom_time_on_address = 12;
  cycle.eeprom_time_off_address = 14;

  /* ;sensor init */
  sensor.attempts = 5;
  sensor.state = 0;

  week_programs.eeprom_base_address = 100;
  monday_programs.eeprom_base_address = 200;
  tuesday_programs.eeprom_base_address = 300;
  wednesday_programs.eeprom_base_address = 400;
  thursday_programs.eeprom_base_address = 500;
  friday_programs.eeprom_base_address = 600;
  saturday_programs.eeprom_base_address = 700;
  sunday_programs.eeprom_base_address = 800;

  Serial.begin(9600);
  Serial1.begin(9600);

  digitalWrite(22, LOW);
  pinMode(22, OUTPUT);
  digitalWrite(23, LOW);
  pinMode(23, OUTPUT);
  digitalWrite(24, LOW);
  pinMode(24, OUTPUT);

  /* ;sd pin */
  pinMode(3, INPUT);

  if (!rtc_ds3231.begin()) {}
  else {}

  if (rtc_ds3231.lostPower())
  {
    rtc_ds3231.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }
  /* rtc_ds3231.adjust(DateTime(2019, 5, 24, 1, 25, 0)); */

  /* ;eeprom init */
  if (EEPROM.read(0) != 23)
  {
    for (int i = 0; i < 1024; i++)
    {
      EEPROM.update(i, 0);
    }
    EEPROM.update(0, 23);
    eeprom_init_first_time();
  }

  cycle.time_on = 20;
  cycle.prev_time_on = 255;
  cycle.time_off = 10;
  cycle.prev_time_off = 255;

  selprog.type = 0;
  selprog.prev_type = -1;

  week_programs.index = eeprom_read_int(week_programs.eeprom_base_address);
  for (int i = 0; i < week_programs.index; i++)
  {
    week_programs.programs[i].time_start = eeprom_read_int(week_programs.eeprom_base_address + 10 + (4 * i) + 0);
    week_programs.programs[i].time_end = eeprom_read_int(week_programs.eeprom_base_address + 10 + (4 * i) + 2);
  }
  monday_programs.index = eeprom_read_int(monday_programs.eeprom_base_address);
  for (int i = 0; i < monday_programs.index; i++)
  {
    monday_programs.programs[i].time_start = eeprom_read_int(monday_programs.eeprom_base_address + 10 + (4 * i) + 0);
    monday_programs.programs[i].time_end = eeprom_read_int(monday_programs.eeprom_base_address + 10 + (4 * i) + 2);
  }
  tuesday_programs.index = eeprom_read_int(tuesday_programs.eeprom_base_address);
  for (int i = 0; i < tuesday_programs.index; i++)
  {
    tuesday_programs.programs[i].time_start = eeprom_read_int(tuesday_programs.eeprom_base_address + 10 + (4 * i) + 0);
    tuesday_programs.programs[i].time_end = eeprom_read_int(tuesday_programs.eeprom_base_address + 10 + (4 * i) + 2);
  }
  wednesday_programs.index = eeprom_read_int(wednesday_programs.eeprom_base_address);
  for (int i = 0; i < wednesday_programs.index; i++)
  {
    wednesday_programs.programs[i].time_start = eeprom_read_int(wednesday_programs.eeprom_base_address + 10 + (4 * i) + 0);
    wednesday_programs.programs[i].time_end = eeprom_read_int(wednesday_programs.eeprom_base_address + 10 + (4 * i) + 2);
  }
  thursday_programs.index = eeprom_read_int(thursday_programs.eeprom_base_address);
  for (int i = 0; i < thursday_programs.index; i++)
  {
    thursday_programs.programs[i].time_start = eeprom_read_int(thursday_programs.eeprom_base_address + 10 + (4 * i) + 0);
    thursday_programs.programs[i].time_end = eeprom_read_int(thursday_programs.eeprom_base_address + 10 + (4 * i) + 2);
  }
  friday_programs.index = eeprom_read_int(friday_programs.eeprom_base_address);
  for (int i = 0; i < friday_programs.index; i++)
  {
    friday_programs.programs[i].time_start = eeprom_read_int(friday_programs.eeprom_base_address + 10 + (4 * i) + 0);
    friday_programs.programs[i].time_end = eeprom_read_int(friday_programs.eeprom_base_address + 10 + (4 * i) + 2);
  }
  saturday_programs.index = eeprom_read_int(saturday_programs.eeprom_base_address);
  for (int i = 0; i < saturday_programs.index; i++)
  {
    saturday_programs.programs[i].time_start = eeprom_read_int(saturday_programs.eeprom_base_address + 10 + (4 * i) + 0);
    saturday_programs.programs[i].time_end = eeprom_read_int(saturday_programs.eeprom_base_address + 10 + (4 * i) + 2);
  }
  sunday_programs.index = eeprom_read_int(sunday_programs.eeprom_base_address);
  for (int i = 0; i < sunday_programs.index; i++)
  {
    sunday_programs.programs[i].time_start = eeprom_read_int(sunday_programs.eeprom_base_address + 10 + (4 * i) + 0);
    sunday_programs.programs[i].time_end = eeprom_read_int(sunday_programs.eeprom_base_address + 10 + (4 * i) + 2);
  }

  cycle.id = eeprom_read_int(cycle.eeprom_id_address);
  cycle.time_on = eeprom_read_int(cycle.eeprom_time_on_address);
  cycle.time_off = eeprom_read_int(cycle.eeprom_time_off_address);


  power.type = eeprom_read_byte(power.eeprom_type_address);
  power.manual_val = eeprom_read_byte(power.eeprom_manual_val_address);

  selprog.type = eeprom_read_byte(selprog.eeprom_type_address);

  delay(3000);
  nextion.prev_page = 255;
  nextion_goto_page_dashboard();

  if (power.type == 0)
  {
    onoff.state = eeprom_read_int(onoff.eeprom_state_address);
  }
  else
  {
    onoff.state = power.manual_val;
  }

  
  /* ;programs: must be run once before cycle_manager()? */
  programs_get_current();
}

// -------------------------------------------------------------------------------------------------------------------------
// ;main
// -------------------------------------------------------------------------------------------------------------------------
void loop()
{
  /* ;sd */
  sd_manager();
  
  /* ;rtc */
  rtc_manager();

  /* ;nextion */
  nextion_listen();

  /* ;sensor */
  sensor_manager();

  /* ;programs */
  programs_get_current();
  
  /* ;cycle */
  cycle_manager();

  // -------------------------------------------------------------------------------------------------------------------------
  // ;render
  // -------------------------------------------------------------------------------------------------------------------------
  switch (nextion.current_page)
  {
    case page_dashboard:
      render_page_dashboard();
      break;
    case page_selprog:
      render_page_selprog();
      break;
    case page_listprog:
      render_page_listprog();
      break;
    case page_addprog:
      render_page_addprog();
      break;
    case page_addprogfrom:
      render_page_addprogfrom();
      break;
    case page_addprogto:
      render_page_addprogto();
      break;
    case page_setcycle:
      render_page_setcycle();
      break;
    case page_setclock:
      render_page_setclock();
      break;
    case page_setclockymd:
      render_page_setclockymd();
      break;
    case page_setclockhms:
      render_page_setclockhms();
      break;
    case page_sd:
      render_page_sd();
      break;
    case page_power:
      render_page_power();
      break;
  }
}
