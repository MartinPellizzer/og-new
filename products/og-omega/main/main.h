/* ------------------------------------------------------------------------------------- */
/* ;onoff */
/* ------------------------------------------------------------------------------------- */
typedef struct onoff_t
{
  int8_t state;
  int8_t prev_state;
  uint16_t eeprom_state_address;

  int8_t in_cycle;
  int8_t prev_in_cycle;
} onoff_t;

/* ------------------------------------------------------------------------------------- */
/* ;selprog */
/* ------------------------------------------------------------------------------------- */
enum selprog_e
{
  selprog_weekly,
  selprog_daily,
};
typedef struct selprog_t
{
  int8_t type;
  int8_t prev_type;
  int8_t tmp_type;
  uint16_t eeprom_type_address;
} selprog_t;

/* ------------------------------------------------------------------------------------- */
/* ;listprog */
/* ------------------------------------------------------------------------------------- */
enum listprog_e
{
  listprog_weekly,
  listprog_monday,
  listprog_tuesday,
  listprog_wednesday,
  listprog_thursday,
  listprog_friday,
  listprog_saturday,
  listprog_sunday,
};

/* ------------------------------------------------------------------------------------- */
/* ;program */
/* ------------------------------------------------------------------------------------- */
typedef struct program_t
{
  int16_t time_start = 0;
  int16_t time_end = 0;
  int8_t hh_start = 0;
  int8_t mm_start = 0;
  int8_t hh_end = 0;
  int8_t mm_end = 0;
  int16_t prev_time_start = 0;
  int16_t prev_time_end = 0;
  int8_t prev_hh_start = 0;
  int8_t prev_mm_start = 0;
  int8_t prev_hh_end = 0;
  int8_t prev_mm_end = 0;
} program_t;

#define NUM_MAX_PROGRAMS 8
typedef struct programs_t
{
  int8_t index;
  int8_t prev_index;
  program_t programs[NUM_MAX_PROGRAMS];
  uint16_t eeprom_base_address;
} programs_t;

/* ------------------------------------------------------------------------------------- */
/* ;cycle */
/* ------------------------------------------------------------------------------------- */
typedef struct cycle_t
{
  int8_t time_on;
  int8_t prev_time_on;
  int8_t tmp_time_on;

  int8_t time_off;
  int8_t prev_time_off;
  int8_t tmp_time_off;

  uint16_t eeprom_time_on_address;
  uint16_t eeprom_time_off_address;

  uint8_t state;
  uint64_t curr_working_millis;
  uint64_t curr_resting_millis;
  uint8_t id_incremented;
  uint16_t id;
  uint16_t eeprom_id_address;
} cycle_t;

/* ------------------------------------------------------------------------------------- */
/* ;power */
/* ------------------------------------------------------------------------------------- */
typedef struct power_t
{
  int8_t type;
  int8_t prev_type;
  int8_t tmp_type;
  uint16_t eeprom_type_address;

  int8_t manual_val;
  int8_t prev_manual_val;
  int8_t tmp_manual_val;
  uint16_t eeprom_manual_val_address;
} power_t;

/* ------------------------------------------------------------------------------------- */
/* ;rtc */
/* ------------------------------------------------------------------------------------- */
enum month_e
{
  none,
  january,
  february,
  march,
  april,
  may,
  june,
  july,
  august,
  september,
  october,
  november,
  december,
};
enum dayofweek_e
{
  dayofweek_sunday,
  dayofweek_monday,
  dayofweek_tuesday,
  dayofweek_wednesday,
  dayofweek_thursday,
  dayofweek_friday,
  dayofweek_saturday,
};
typedef struct rtc_t
{
  int16_t year;
  int16_t prev_year;
  int16_t tmp_year;
  int8_t month;
  int8_t prev_month;
  int8_t tmp_month;
  int8_t day;
  int8_t prev_day;
  int8_t tmp_day;
  uint8_t hour;
  uint8_t prev_hour;
  uint8_t tmp_hour;
  uint8_t minute;
  uint8_t prev_minute;
  uint8_t tmp_minute;
  uint8_t second;
  uint8_t prev_second;
  uint8_t tmp_second;
  
  uint8_t dayofweek;
  uint8_t prev_dayofweek;
  uint8_t tmp_dayofweek;
  uint16_t time_in_minutes;
} rtc_t;

/* ------------------------------------------------------------------------------------- */
/* ;nextion */
/* ------------------------------------------------------------------------------------- */
enum nextion_page_e
{
  page_dashboard,
  page_settings,
  page_selprog,
  page_setprogweek,
  page_setprogday,
  page_listprog,
  page_addprog,
  page_addprogfrom,
  page_addprogto,
  page_setcycle,
  page_setclock,
  page_setclockymd,
  page_setclockhms,
  page_analytics,
  page_sd,
  page_power,
  page_infosys,
};
typedef struct nextion_t
{
  uint8_t current_page;
  uint8_t prev_page;
  uint8_t refresh;
} nextion_t;

/* ------------------------------------------------------------------------------------- */
/* ;relay */
/* ------------------------------------------------------------------------------------- */
typedef struct relay_t
{
  int8_t curr_state;
  int8_t prev_state;
} relay_t;

/* ------------------------------------------------------------------------------------- */
/* ;sensor */
/* ------------------------------------------------------------------------------------- */
typedef struct sensor_t
{
  int16_t state;
  int16_t prev_state;
  int16_t ppb;
  int16_t prev_ppb;
  int8_t attempts;
  uint32_t attempts_millis;
} sensor_t;

/* ------------------------------------------------------------------------------------- */
/* ;sd */
/* ------------------------------------------------------------------------------------- */
typedef struct sd_card_t
{
  uint8_t state;
  uint8_t is_inserted;
  uint8_t prev_is_inserted;
  uint8_t tried_to_initialize;
  uint8_t pin;
  uint8_t pin_cd;
} sd_card_t;
