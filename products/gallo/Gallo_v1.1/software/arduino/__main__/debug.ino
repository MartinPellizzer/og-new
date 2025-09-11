uint32_t debug_millis_cur = 0;

void debug_manager()
{
  // ;debug
  if (millis() - debug_millis_cur > 1000) 
  {
    debug_millis_cur = millis();
    
    // Serial.print("external_input.state_cur: ");
    // Serial.println(external_input.state_cur);
    // Serial.print("external_input.is_abilitated_cur: ");
    // Serial.println(external_input.is_abilitated_cur);
    // Serial.print("sensor_temperature.state_cur: ");
    // Serial.println(sensor_temperature.state_cur);

    // Serial.print("o3_sensor_alarm.is_over_max_cur: ");
    // Serial.println(o3_sensor_alarm.is_over_max_cur);
    // Serial.print("o3_sensor_alarm.alarm_millis_cur: ");
    // Serial.println(millis() - o3_sensor_alarm.alarm_millis_cur);
    // Serial.print("o3_sensor_alarm.is_alarm_cur: ");
    // Serial.println(o3_sensor_alarm.is_alarm_cur);
    // Serial.print("o3_sensor_alarm.ppb_cur: ");
    // Serial.println(o3_sensor_alarm.ppb_cur);
    // Serial.print("o3_sensor_alarm.ppb_alarm_cur: ");
    // Serial.println(o3_sensor_alarm.ppb_alarm_cur);

    // Serial.print("sensor_temperature.state_cur: ");
    // Serial.println(sensor_temperature.state_cur);
    // Serial.print("external_input.is_abilitated_cur: ");
    // Serial.println(external_input.is_abilitated_cur);
    // Serial.print("external_input.state_cur: ");
    // Serial.println(external_input.state_cur);

    // Serial.println();
  }
}
