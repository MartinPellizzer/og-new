void sensor_temperature_manager()
{
  sensor_temperature.state_cur = digitalRead(RI_2);
  if (sensor_temperature.state_cur == 1) // alarm
  {
    is_on_cur = 0;
    nextion.page_cur = P_TEMPERATURE_ALARM;
  }
}