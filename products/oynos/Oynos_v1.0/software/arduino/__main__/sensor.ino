void sensor_ozone_alarm_read_ppb_old()
{
  if (millis() - o3_sensor_alarm.millis1_cur > 100) 
  {
    o3_sensor_alarm.millis1_cur = millis();
    o3_sensor_alarm.readings_sum += analogRead(S1_010V);
    o3_sensor_alarm.readings_counter += 1;
  }
  if (millis() - o3_sensor_alarm.millis2_cur > 1000) 
  {
    o3_sensor_alarm.millis2_cur = millis();
    uint32_t result = o3_sensor_alarm.readings_sum / o3_sensor_alarm.readings_counter;
    // TODO: check
    // Serial.println(result);
    uint16_t ppb = map(result, 0, 255, 0, 10000);
    o3_sensor_alarm.ppb_cur = ppb;
    // Serial.print("PPB: ");
    // Serial.println(ppb);
    o3_sensor_alarm.readings_sum = 0;
    o3_sensor_alarm.readings_counter = 0;
  }
}
void sensor_ozone_alarm_read_ppb()
{
  // if (millis() - o3_sensor_alarm.millis1_cur > 100) 
  // {
  //   o3_sensor_alarm.millis1_cur = millis();
  //   o3_sensor_alarm.readings_sum += analogRead(S1_010V);
  //   o3_sensor_alarm.readings_counter += 1;
  // }
  if (millis() - o3_sensor_alarm.millis2_cur > 1000) 
  {
    o3_sensor_alarm.millis2_cur = millis();
    uint32_t result = analogRead(S1_010V);
    // TODO: check
    // Serial.print("010V ANALOG READ: ");
    // Serial.println(result);
    uint16_t ppb = map(result, 0, 4095, 0, 10000);
    o3_sensor_alarm.ppb_cur = ppb;
    // Serial.print("PPB: ");
    // Serial.println(ppb);
    o3_sensor_alarm.readings_sum = 0;
    o3_sensor_alarm.readings_counter = 0;
  }
}

void sensor_ozone_alarm_check()
{
  // is sensor over alarm val
  if (o3_sensor_alarm.ppb_cur >= o3_sensor_alarm.ppb_alarm_cur) 
    o3_sensor_alarm.is_over_max_cur = 1;
  else 
    o3_sensor_alarm.is_over_max_cur = 0;

  // if sensor under alarm val -> reset counter
  if (o3_sensor_alarm.is_over_max_cur == 0) 
    o3_sensor_alarm.alarm_millis_cur = millis();

  // count if sensor over alarm val for some time
  uint32_t alarm_timer_millis_cur = (uint32_t)o3_sensor_alarm.alarm_timer_minutes_cur * 60 * 1000;
  // uint32_t alarm_timer_millis_cur = 5000;
  if (millis() - o3_sensor_alarm.alarm_millis_cur >= alarm_timer_millis_cur) 
  {
    // trigger alarm / turn off system
    // o3_sensor_alarm.is_alarm_cur = 1;
    is_on_cur = 0;
    nextion.page_cur = P_OZONE_ALARM;
  }

  // if alarm triggered -> go to alarm screen
  // if (o3_sensor_alarm.is_alarm_old != o3_sensor_alarm.is_alarm_cur)
  // {
  //   o3_sensor_alarm.is_alarm_old = o3_sensor_alarm.is_alarm_cur;
  //   if (o3_sensor_alarm.is_alarm_cur == 1)
  //   {
  //     nextion.page_cur = P_OZONE_ALARM;
  //   }
  // }
}

void sensor_ozone_alarm_manager()
{
  sensor_ozone_alarm_read_ppb();
  sensor_ozone_alarm_check();
}