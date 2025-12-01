
void cycle_update() 
{
  if (ozone_on) 
  {
    nextion_calendar_state_cur = 1;
    if ((millis() - ozone_on_current_millis) > ozone_on_timer_millis) 
    {
      ozone_on = false;
      digitalWrite(relay_pin, LOW);
    }
    else
    {  
      if (sensor.connected_curr == 0)
      {
        nextion_ozone_on_cur = 0;
        digitalWrite(relay_pin, LOW);
      }
      else
      {
        int ppb_min = cycle.ppb_cur - (cycle.ppb_cur / 100 * cycle.ppb_delta_cur);
        int ppb_max = cycle.ppb_cur + (cycle.ppb_cur / 100 * cycle.ppb_delta_cur);
        if (sensor.ppb_curr < ppb_min) 
        {
          digitalWrite(relay_pin, HIGH);
          nextion_ozone_on_cur = 1;
        }
        if (sensor.ppb_curr > ppb_max)
        {
          digitalWrite(relay_pin, LOW);
          nextion_ozone_on_cur = 0;
        }
      }
    }
  }
  else 
  {
    nextion_calendar_state_cur = 0;
    nextion_ozone_on_cur = 0;

    for (int i = 0; i < CALENDAR_TIMERS_NUM; i++) 
    {
      int32_t rtc_seconds_tot = (rtc.hour_cur * 3600) + (rtc.minute_cur * 60) + (rtc.second_cur);
      int32_t calendar_seconds_tot = calendar_days[rtc.day_week][i];
      if (rtc_seconds_tot == calendar_seconds_tot) 
      {
        ozone_on = true;
        ozone_on_current_millis = millis();
        ozone_on_timer_millis = uint32_t(cycle.seconds_on_cur) * 1000;
      }
    }
  }
}
