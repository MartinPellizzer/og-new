void sensor_ozone_alarm_read_ppb()
{
  if (millis() - o3_sensor_alarm.millis2_cur > 1000) 
  {
    o3_sensor_alarm.millis2_cur = millis();
    uint32_t result = analogRead(S1_010V);
    uint16_t ppb = map(result, 0, 4095, 0, 10000);
    o3_sensor_alarm.ppb_cur = ppb;
  }
}

void sensor_ozone_alarm_check()
{
  // is sensor over alarm val
  if (o3_sensor_alarm.ppb_cur >= o3_sensor_alarm.ppb_alarm_cur) o3_sensor_alarm.is_over_max_cur = 1;
  else o3_sensor_alarm.is_over_max_cur = 0;

  // if sensor under alarm val -> reset counter
  if (o3_sensor_alarm.is_over_max_cur == 0) o3_sensor_alarm.alarm_millis_cur = millis();

  // count if sensor over alarm val for some time
  uint32_t alarm_timer_millis_cur = (uint32_t)o3_sensor_alarm.alarm_timer_minutes_cur * 60 * 1000;
  if (millis() - o3_sensor_alarm.alarm_millis_cur >= alarm_timer_millis_cur) 
  {
    // trigger alarm / turn off system
    is_on_cur = 0;
    nextion.page_cur = P_OZONE_ALARM;
  }
}

void sensor_ozone_alarm_manager()
{
  if (o3_sensor_alarm.enable_cur == 1)
  {
    sensor_ozone_alarm_read_ppb();
    sensor_ozone_alarm_check();
  }
  else
  {
    o3_sensor_alarm.alarm_millis_cur = millis();
  }
}
