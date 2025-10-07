// void sensor_temperature_manager_old()
// {
//   sensor_temperature.state_cur = digitalRead(RI_2);
//   if (sensor_temperature.state_cur == 1) // alarm
//   {
//     is_on_cur = 0;
//     nextion.page_cur = 90;
//   }
// }

void sensor_temperature_manager()
{
  if (sensor_temperature.enable_cur == 1)
  {
    sensor_temperature.state_cur = digitalRead(RI_2);
    if (sensor_temperature.state_cur == 1) // alarm
    {
      if (millis() - sensor_temperature.alarm_millis_cur >= ((int32_t)sensor_temperature.alarm_seconds_cur * 1000)) 
      {
        is_on_cur = 0;
        nextion.page_cur = 90;
      }
    }
    else
    {
      sensor_temperature.alarm_millis_cur = millis();
    }
  }
  else
  {
    sensor_temperature.alarm_millis_cur = millis();
  }
}