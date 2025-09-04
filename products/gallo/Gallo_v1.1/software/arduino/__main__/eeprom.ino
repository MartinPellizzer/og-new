uint8_t get_eeprom_address_calendar(int day_i, int time_i, int offset)
{
  uint8_t eeprom_address = 100 + (day_i*CALENDAR_TIMERS_NUM) + (time_i*4) + offset;
  return eeprom_address;
}