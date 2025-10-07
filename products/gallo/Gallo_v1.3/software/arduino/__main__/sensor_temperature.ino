void sensor_temperature_manager_old()
{
  sensor_temperature.state_cur = digitalRead(RI_2);
  if (sensor_temperature.state_cur == 1) // alarm
  {
    is_on_cur = 0;
    nextion.page_cur = P_TEMPERATURE_ALARM;
  }
}

void sensor_temperature_manager()
{
  sensor_temperature.state_cur = digitalRead(RI_2);
  if (sensor_temperature.state_cur == 1) // alarm
  {
    if (millis() - sensor_temperature.alarm_millis_cur >= 60000) 
    {
      is_on_cur = 0;
      nextion.page_cur = P_TEMPERATURE_ALARM;
    }
  }
  else
  {
    sensor_temperature.alarm_millis_cur = millis();
  }
}