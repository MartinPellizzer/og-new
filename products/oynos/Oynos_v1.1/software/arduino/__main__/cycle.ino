bool is_time_cur_in_calendar()
{
  bool found = false;
  int32_t rtc_seconds_tot = (rtc.hour_cur * 3600) + (rtc.minute_cur * 60) + (rtc.second_cur);
  for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
  {
    if (rtc_seconds_tot > calendar_times[rtc.day_week_cur][j][0] && rtc_seconds_tot < calendar_times[rtc.day_week_cur][j][1])
    {
      found = true;
    }
  }
  return found;
}


void cycle_start()
{
  cycle.state_cur = 1;
  if (cycle.state_old != cycle.state_cur)
  {
    cycle.state_old = cycle.state_cur;
    cycle_state = OXY_01;
    cycle_millis_cur = millis();
    Serial.print("cycle.state_cur");
    Serial.println(cycle.state_cur);
  }
  if (cycle_state == OXY_01)
  {
    digitalWrite(RO_1, 1);
  }
  if (cycle_state == O3_01)
  {
    digitalWrite(RO_2, 1);
  }
  if (cycle_state == OXY_02)
  {
    digitalWrite(RO_3, 1);
  }
  if (cycle_state == O3_02)
  {
    digitalWrite(RO_6, 1);
  }
  // if (cycle_state == OXY_03)
  // {
  //   digitalWrite(RO_7, 1);
  // }
  // if (cycle_state == O3_03)
  // {
  //   digitalWrite(RO_8, 1);
  // }
  if (millis() - cycle_millis_cur > 5000) 
  {
    cycle_millis_cur = millis();
    if (power.power_cur == 0)
    {
      if (cycle_state == OXY_01) {cycle_state = O3_01;}
    }
    else if (power.power_cur == 1)
    {
      if (cycle_state == OXY_01) {cycle_state = O3_01;}
      else if (cycle_state == O3_01) {cycle_state = OXY_02;}
      else if (cycle_state == OXY_02) {cycle_state = O3_02;}
    }
    else if (power.power_cur == 2)
    {
      if (cycle_state == OXY_01) {cycle_state = O3_01;}
      else if (cycle_state == O3_01) {cycle_state = OXY_02;}
      else if (cycle_state == OXY_02) {cycle_state = O3_02;}
      // else if (cycle_state == O3_02) {cycle_state = OXY_03;}
      // else if (cycle_state == OXY_03) {cycle_state = O3_03;}
    }
  }
}

void cycle_stop()
{
  cycle.state_cur = 0;
  if (cycle.state_old != cycle.state_cur)
  {
    cycle.state_old = cycle.state_cur;
    cycle_state = OFF_O3;
    cycle_millis_cur = millis();
    Serial.print("cycle.state_cur");
    Serial.println(cycle.state_cur);
  }
  if (cycle_state == OFF_O3)
  {
    digitalWrite(RO_2, 0);
    digitalWrite(RO_6, 0);
    // digitalWrite(RO_8, 0);
  }
  else if (cycle_state == OFF_OXY)
  {
    digitalWrite(RO_1, 0);
    digitalWrite(RO_3, 0);
    // digitalWrite(RO_7, 0);
  }
  if (millis() - cycle_millis_cur > 5000) 
  {
    cycle_millis_cur = millis();
    if (cycle_state == OFF_O3) {cycle_state = OFF_OXY;}
  }
}

void cycle_manager()
{
  // external input abilitate (state 0)
  if (external_input.is_abilitated_cur == 0)
  {
    if (external_input.state_cur == 0)
    {
      if (is_on_cur)
      {
        if (calendar_onoff_cur)
        {
          bool is_time_calendar = is_time_cur_in_calendar();
          if (is_time_calendar)
          {
            cycle_start();
          }
          else
          {
            cycle_stop();
          }
        }
        else
        {
          cycle_start();
        }
      }
      else
      {
        cycle_stop();
      }
    }
    else
    {
        cycle_stop();
    }
  }
  else 
  {
    if (is_on_cur)
    {
      if (calendar_onoff_cur)
      {
        bool is_time_calendar = is_time_cur_in_calendar();
        if (is_time_calendar)
        {
          cycle_start();
        }
        else
        {
          cycle_stop();
        }
      }
      else
      {
        cycle_start();
      }
    }
    else
    {
      cycle_stop();
    }
  }
}
