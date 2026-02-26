

uint8_t get_eeprom_address_calendar(int day_i, int time_i, int offset)
{
  uint8_t eeprom_address = 100 + (day_i*CALENDAR_TIMERS_NUM) + (time_i*4) + offset;
  return eeprom_address;
}

void eeprom_write_uint16(uint16_t start_addr, uint16_t value) 
{
    uint8_t low  = (uint8_t)(value & 0xFF);
    uint8_t high = (uint8_t)((value >> 8) & 0xFF);
    EEPROM.write(start_addr,     low);   // store low byte
    EEPROM.write(start_addr + 1, high);  // store high byte
    EEPROM.commit();
}

uint16_t eeprom_read_uint16(uint16_t start_addr) 
{
    uint8_t low  = EEPROM.read(start_addr);       // read low byte
    uint8_t high = EEPROM.read(start_addr + 1);   // read high byte
    return ((uint16_t)high << 8) | low;  // recombine into uint16_t
}

void eeprom_init() 
{
  // sensor ozone alarm
  uint16_t eeprom_sensor_ozone_alarm_enable_cur = eeprom_read_uint16(SENSOR_OZONE_ALARM_ENABLE);
  if (eeprom_sensor_ozone_alarm_enable_cur != 65535)
  {
    o3_sensor_alarm.enable_cur = eeprom_sensor_ozone_alarm_enable_cur;
  }
  uint16_t eeprom_ppb_alarm_cur = eeprom_read_uint16(ALARM_PPB);
  if (eeprom_ppb_alarm_cur != 65535)
  {
    o3_sensor_alarm.ppb_alarm_cur = eeprom_ppb_alarm_cur;
  }
  uint16_t eeprom_alarm_timer_minutes_cur = eeprom_read_uint16(ALARM_TIMER_MINUTES);
  if (eeprom_alarm_timer_minutes_cur != 65535)
  {
    o3_sensor_alarm.alarm_timer_minutes_cur = eeprom_alarm_timer_minutes_cur;
  }
  // external input
  uint16_t eeprom_external_input_cur = eeprom_read_uint16(EXTERNAL_INPUT);
  if (eeprom_external_input_cur != 65535)
  {
    external_input.is_abilitated_cur = eeprom_external_input_cur;
  }
  // calendar
  uint16_t eeprom_calendar_enabled = eeprom_read_uint16(CALENDAR_ENABLED);
  if (eeprom_calendar_enabled != 65535)
  {
    calendar_onoff_cur = eeprom_calendar_enabled;
  }
  // sensor temperature
  uint16_t eeprom_sensor_temperature_enable_cur = eeprom_read_uint16(SENSOR_TEMPERATURE_ENABLE);
  if (eeprom_sensor_temperature_enable_cur != 65535)
  {
    sensor_temperature.enable_cur = eeprom_sensor_temperature_enable_cur;
  }
  uint16_t eeprom_sensor_temperature_alarm_seconds_cur = eeprom_read_uint16(SENSOR_TEMPERATURE_SECONDS);
  if (eeprom_sensor_temperature_alarm_seconds_cur != 65535)
  {
    sensor_temperature.alarm_seconds_cur = eeprom_sensor_temperature_alarm_seconds_cur;
  }

  // custom cycle
  uint16_t eeprom_custom_state_cur = eeprom_read_uint16(CUSTOM_STATE_CUR);
  if (eeprom_custom_state_cur != 65535)
  {
    cycle.custom_state_cur = eeprom_custom_state_cur;
  }
  
  uint16_t eeprom_custom_minites_working_cur = eeprom_read_uint16(CUSTOM_MINUTES_WORKING_CUR);
  if (eeprom_custom_minites_working_cur != 65535)
  {
    cycle.custom_minutes_working_cur = eeprom_custom_minites_working_cur;
  }
  
  uint16_t eeprom_custom_minites_resting_cur = eeprom_read_uint16(CUSTOM_MINUTES_RESTING_CUR);
  if (eeprom_custom_minites_resting_cur != 65535)
  {
    cycle.custom_minutes_resting_cur = eeprom_custom_minites_resting_cur;
  }
  
  uint16_t eeprom_custom_cycles_num_cur = eeprom_read_uint16(CUSTOM_CYCLES_NUM_CUR);
  if (eeprom_custom_cycles_num_cur != 65535)
  {
    cycle.custom_cycles_num_cur = eeprom_custom_cycles_num_cur;
  }

  // custom cycle operation num target
  uint16_t eeprom_custom_cycle_operation_num_target = eeprom_read_uint16(CUSTOM_CYCLES_OPERATION_NUM_TARGET);
  if (eeprom_custom_cycle_operation_num_target != 65535)
  {
    cycle.custom_cycles_operation_num_target_cur = eeprom_custom_cycle_operation_num_target;
  }

  // custom cycle operation num done
  uint16_t eeprom_custom_cycle_operation_num_done = eeprom_read_uint16(CUSTOM_CYCLES_OPERATION_NUM_DONE);
  if (eeprom_custom_cycle_operation_num_done != 65535)
  {
    cycle.custom_cycles_operation_num_done_cur = eeprom_custom_cycle_operation_num_done;
  }

  // Serial.println(o3_sensor_alarm.ppb_alarm_cur);
  // Serial.println(o3_sensor_alarm.alarm_timer_minutes_cur);
  // Serial.println(external_input.is_abilitated_cur);
  // Serial.println(calendar_onoff_cur);
}