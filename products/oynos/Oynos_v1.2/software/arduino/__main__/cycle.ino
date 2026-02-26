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

void cycle_manager_default()
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

////////////////////////////////////////////////////////////////////////////////
// CUSTOM CYCLE
////////////////////////////////////////////////////////////////////////////////

void cycle_custom_stop()
{
  cycle.state_cur = 0;
  if (cycle.state_old != cycle.state_cur)
  {
    cycle.state_old = cycle.state_cur;
    cycle_state = OFF_O3;
    cycle_millis_cur = millis();
  }
  if (cycle_state == OFF_O3)
  {
    digitalWrite(RO_2, 0);
    digitalWrite(RO_6, 0);
  }
  else if (cycle_state == OFF_OXY)
  {
    digitalWrite(RO_1, 0);
    digitalWrite(RO_3, 0);
  }
  if (millis() - cycle_millis_cur > 5000) 
  {
    cycle_millis_cur = millis();
    if (cycle_state == OFF_O3) { cycle_state = OFF_OXY; }
  }
}

void cycle_custom_start()
{
  if (cycle.custom_cycles_init_state == 1)
  {
    cycle.custom_cycles_init_state = 0;
    cycle.custom_cycles_num_counter = 0;
    cycle.custom_cycles_working_state = 1;
    cycle.custom_cycles_millis_cur = millis();
  }
}

void cycle_custom_run_working()
{
  cycle.state_cur = 1;
  if (cycle.state_old != cycle.state_cur)
  {
    cycle.state_old = cycle.state_cur;
    cycle.custom_cycles_operation_num_update = 1;
    cycle_state = OXY_01;
    cycle_millis_cur = millis();
  }
  if (millis() - cycle_millis_cur > 5000) 
  {
    cycle_millis_cur = millis();
    if (power.power_cur == 0)
    {
      if (cycle_state == OXY_01)      { cycle_state = O3_01;  }
    }
    else if (power.power_cur == 1)
    {
      if (cycle_state == OXY_01)      { cycle_state = O3_01;  }
      else if (cycle_state == O3_01)  { cycle_state = OXY_02; }
      else if (cycle_state == OXY_02) { cycle_state = O3_02;  }
    }
    else if (power.power_cur == 2)
    {
      if (cycle_state == OXY_01)      { cycle_state = O3_01;  }
      else if (cycle_state == O3_01)  { cycle_state = OXY_02; }
      else if (cycle_state == OXY_02) { cycle_state = O3_02;  }
    }
  }
  if (cycle_state == OXY_01) digitalWrite(RO_1, 1);
  if (cycle_state == O3_01)  digitalWrite(RO_2, 1);
  if (cycle_state == OXY_02) digitalWrite(RO_3, 1);
  if (cycle_state == O3_02)  digitalWrite(RO_6, 1);
}

void cycle_custom_run_resting()
{
  cycle.state_cur = 0;
  if (cycle.state_old != cycle.state_cur)
  {
    cycle.state_old = cycle.state_cur;
    cycle_state = OFF_O3;
    cycle_millis_cur = millis();
  }
  if (millis() - cycle_millis_cur > 5000) 
  {
    cycle_millis_cur = millis();
    if (cycle_state == OFF_O3) {cycle_state = OFF_OXY;}
  }
  if (cycle_state == OFF_O3)
  {
    digitalWrite(RO_2, 0);
    digitalWrite(RO_6, 0);
  }
  else if (cycle_state == OFF_OXY)
  {
    digitalWrite(RO_1, 0);
    digitalWrite(RO_3, 0);
  }
}

void cycle_custom_run()
{
  if (cycle.custom_cycles_working_state == 0)
  {
    int32_t timer = (int32_t)cycle.custom_minutes_resting_cur * 60 * 1000;
    if (millis() - cycle.custom_cycles_millis_cur > timer)
    {
      cycle.custom_cycles_millis_cur = millis();
      cycle.custom_cycles_working_state = 1;
      if (++cycle.custom_cycles_num_counter >= cycle.custom_cycles_num_cur*2)
      {
        is_on_cur = 0;
        cycle.custom_cycles_operation_num_done_cur += 1;
        eeprom_write_uint16(CUSTOM_CYCLES_OPERATION_NUM_DONE, cycle.custom_cycles_operation_num_done_cur);
        return;
      }
    }
  }
  else
  {
    int32_t timer = (int32_t)cycle.custom_minutes_working_cur * 60 * 1000;
    if (millis() - cycle.custom_cycles_millis_cur > timer)
    {
      cycle.custom_cycles_millis_cur = millis();
      cycle.custom_cycles_working_state = 0;
      if (++cycle.custom_cycles_num_counter >= cycle.custom_cycles_num_cur*2)
      {
        is_on_cur = 0;
        return;
      }
    }
  }
  if (cycle.custom_cycles_working_state == 1) cycle_custom_run_working();
  else cycle_custom_run_resting();
}

// TODO: run play/pause x num cycles (add counter)
void cycle_manager_custom()
{
  if (is_on_cur)
  {
    cycle_custom_start();
    cycle_custom_run();
  }
  else
  {
    cycle_custom_stop();
  }
}

void cycle_manager()
{
  if (cycle.custom_state_cur == 0)
  {
    cycle_manager_default();
  }
  else
  {
    cycle_manager_custom();
  }
}
