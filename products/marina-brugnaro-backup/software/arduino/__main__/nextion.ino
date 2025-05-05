
void listenNextion() 
{
  if (Serial2.available()) 
  {
    new_data = true;
    buffer_nextion[buffer_counter] = Serial2.read();
    if (buffer_counter < BUFFER_SIZE) buffer_counter++;
    nextion_current_millis = millis();
  }
  if (new_data) 
  {
    if ((millis() - nextion_current_millis) > 10) 
    {
      new_data = false;
      buffer_counter = 0;
      nextionEvalSerial();

      // digitalWrite(relay_pin, HIGH);
      // delay(1000);
      // digitalWrite(relay_pin, LOW);

      nextionDebugSerial();
      nextionClearBuffer();
    }
  }
}


void nextionEvalSerial() {
  if (page_current == 1) 
  {
    if (compareArray(cmd_home_to_onoff, buffer_nextion)) 
    {
      // is_on_cur = !is_on_cur;
    }

    if (is_on_cur) 
    {
      if (compareArray(cmd_home_to_yesterday, buffer_nextion)) page_current = 10;
      if (compareArray(cmd_home_to_calendar, buffer_nextion)) page_current = 20;
      if (compareArray(cmd_home_to_cycle, buffer_nextion)) page_current = 30;
      if (compareArray(cmd_home_to_clock, buffer_nextion)) page_current = 40;
      if (compareArray(cmd_home_to_panel, buffer_nextion)) page_current = 50;
      if (compareArray(cmd_home_to_sd, buffer_nextion)) page_current = 60;
    }
  } 
  else if (page_current == 10) 
  {
    if (compareArray(cmd_yesterday_to_home, buffer_nextion)) 
    {
      page_current = 1;
    }
  } 
  else if (page_current == 20) 
  {
    if (compareArray(cmd_calendar_back, buffer_nextion)) 
    {
      page_current = 1;
    }
    if (compareArray(cmd_calendar_day_prev, buffer_nextion)) 
    {
      day_curr -= 1;
      if (day_curr < 0) 
      {
        day_curr = 6;
      }
    }
    if (compareArray(cmd_calendar_day_next, buffer_nextion)) {
      day_curr += 1;
      if (day_curr > 6) {
        day_curr = 0;
      }
    }
    if (compareArray(cmd_calendar_add, buffer_nextion)) {
      for (int i = 0; i < CALENDAR_TIMERS_NUM; i++) {
        if (calendar_days[day_curr][i] == -1) {
          page_current = 21;
          break;
        }
      }
    }
    if (compareArray(cmd_calendar_t1, buffer_nextion)) {
      calendar_delete_and_order_ascending(0);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t2, buffer_nextion)) {
      calendar_delete_and_order_ascending(1);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t3, buffer_nextion)) {
      calendar_delete_and_order_ascending(2);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t4, buffer_nextion)) {
      calendar_delete_and_order_ascending(3);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t5, buffer_nextion)) {
      calendar_delete_and_order_ascending(4);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t6, buffer_nextion)) {
      calendar_delete_and_order_ascending(5);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t7, buffer_nextion)) {
      calendar_delete_and_order_ascending(6);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t8, buffer_nextion)) {
      calendar_delete_and_order_ascending(7);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t9, buffer_nextion)) {
      calendar_delete_and_order_ascending(8);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t10, buffer_nextion)) {
      calendar_delete_and_order_ascending(9);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t11, buffer_nextion)) {
      calendar_delete_and_order_ascending(10);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t12, buffer_nextion)) {
      calendar_delete_and_order_ascending(11);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t13, buffer_nextion)) {
      calendar_delete_and_order_ascending(12);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t14, buffer_nextion)) {
      calendar_delete_and_order_ascending(13);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t15, buffer_nextion)) {
      calendar_delete_and_order_ascending(14);
      page_old = -1;
    }
    if (compareArray(cmd_calendar_t16, buffer_nextion)) {
      calendar_delete_and_order_ascending(15);
      page_old = -1;
    }
  } else if (page_current == 21)  // CALENDAR ADD
  {
    if (compareArray(cmd_p_cal_add_back, buffer_nextion)) page_current = 20;
    if (compareArray(cmd_p_cal_add_save, buffer_nextion)) 
    {
      page_current = 20;
      calendar_order_add_ascending();
    }
    if (compareArray(cmd_p_cal_add_hour_up, buffer_nextion)) {
      cycle_seconds_tmp += 3600;
      if (cycle_seconds_tmp >= 86400) {
        cycle_seconds_tmp %= 86400;
      }
    }
    if (compareArray(cmd_p_cal_add_hour_down, buffer_nextion)) {
      cycle_seconds_tmp -= 3600;
      if (cycle_seconds_tmp < 0) {
        cycle_seconds_tmp = 86400 + cycle_seconds_tmp;
      }
    }
    if (compareArray(cmd_p_cal_add_minute_up, buffer_nextion)) {
      cycle_seconds_tmp += 60;
      if (cycle_seconds_tmp >= 86400) {
        cycle_seconds_tmp %= 86400;
      }
    }
    if (compareArray(cmd_p_cal_add_minute_down, buffer_nextion)) {
      cycle_seconds_tmp -= 60;
      if (cycle_seconds_tmp < 0) {
        cycle_seconds_tmp = 86400 + cycle_seconds_tmp;
      }
    }
  }
  // CYCLE
  else if (page_current == 30) {
    if (compareArray(cmd_cycle_back, buffer_nextion)) page_current = 1;
    if (compareArray(cmd_cycle_save, buffer_nextion)) 
    {
      cycle.seconds_on_cur = cycle.seconds_on_tmp;
      cycle.ppb_cur = cycle.ppb_tmp;
      cycle.ppb_delta_cur = cycle.ppb_delta_tmp;
      page_current = 1;
      
      uint8_t cycle_minutes = uint8_t(cycle.seconds_on_cur / 60);
      EEPROM.write(10, cycle_minutes);
      EEPROM.commit();
      uint8_t cycle_ppb_1 = cycle.ppb_cur % 100000 / 10000;
      uint8_t cycle_ppb_2 = cycle.ppb_cur % 10000 / 1000;
      uint8_t cycle_ppb_3 = cycle.ppb_cur % 1000 / 100;
      EEPROM.write(11, cycle_ppb_1);
      EEPROM.write(12, cycle_ppb_2);
      EEPROM.write(13, cycle_ppb_3);
      EEPROM.commit();
      uint8_t cycle_ppb_delta = uint8_t(cycle.ppb_delta_cur);
      EEPROM.write(14, cycle_ppb_delta);
      EEPROM.commit();
    }
    if (compareArray(cmd_cycle_on_sub, buffer_nextion)) {
      cycle.seconds_on_tmp -= 60;
      if (cycle.seconds_on_tmp < 0) {
        cycle.seconds_on_tmp = 0;
      }
    }
    if (compareArray(cmd_cycle_on_add, buffer_nextion)) {
      cycle.seconds_on_tmp += 60;
      if (cycle.seconds_on_tmp > 3600) {
        cycle.seconds_on_tmp = 3600;
      }
    }
    if (compareArray(cmd_cycle_ppb_sub, buffer_nextion)) {
      cycle.ppb_tmp -= 100;
      if (cycle.ppb_tmp < 0) {
        cycle.ppb_tmp = 0;
      }
    }
    if (compareArray(cmd_cycle_ppb_add, buffer_nextion)) {
      cycle.ppb_tmp += 100;
      if (cycle.ppb_tmp > 10000) {
        cycle.ppb_tmp = 10000;
      }
    }
    if (compareArray(cmd_cycle_ppb_delta_sub, buffer_nextion)) {
      cycle.ppb_delta_tmp -= 1;
      if (cycle.ppb_delta_tmp < 0) {
        cycle.ppb_delta_tmp = 0;
      }
    }
    if (compareArray(cmd_cycle_ppb_delta_add, buffer_nextion)) {
      cycle.ppb_delta_tmp += 1;
      if (cycle.ppb_delta_tmp > 50) {
        cycle.ppb_delta_tmp = 50;
      }
    }
  }
  // CLOCK
  else if (page_current == 40) {
    if (compareArray(cmd_p_clk_back, buffer_nextion)) page_current = 1;
    if (compareArray(cmd_p_clk_date, buffer_nextion)) page_current = 41;
    if (compareArray(cmd_p_clk_time, buffer_nextion)) page_current = 42;
  }
  // CLOCK DATE
  else if (page_current == 41) {
    if (compareArray(cmd_p_clk_date_back, buffer_nextion)) page_current = 40;
    if (compareArray(cmd_p_clk_date_save, buffer_nextion)) {
      rtc.year_cur = rtc.year_tmp;
      rtc.month_cur = rtc.month_tmp;
      rtc.day_cur = rtc.day_tmp;
      rtc_lib.adjust(DateTime(rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur, rtc.second_cur));
      page_current = 40;
    }
    if (compareArray(cmd_p_clk_date_year_up, buffer_nextion)) {
      rtc.year_tmp += 1;
      if (rtc.year_tmp >= 2100) {
        rtc.year_tmp = 2100;
      }
    }
    if (compareArray(cmd_p_clk_date_year_down, buffer_nextion)) {
      rtc.year_tmp -= 1;
      if (rtc.year_tmp < 2020) {
        rtc.year_tmp = 2020;
      }
    }
    if (compareArray(cmd_p_clk_date_month_up, buffer_nextion)) {
      rtc.month_tmp += 1;
      rtc.day_tmp = 1;
      if (rtc.month_tmp >= 12) {
        rtc.month_tmp = 12;
      }
    }
    if (compareArray(cmd_p_clk_date_month_down, buffer_nextion)) {
      rtc.month_tmp -= 1;
      rtc.day_tmp = 1;
      if (rtc.month_tmp < 1) {
        rtc.month_tmp = 1;
      }
    }
    if (compareArray(cmd_p_clk_date_day_up, buffer_nextion)) {
      rtc.day_tmp += 1;
      if (rtc.month_tmp == 1) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 2) {
        if (rtc.day_tmp >= 28) { rtc.day_tmp = 28; }
      }
      if (rtc.month_tmp == 3) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 4) {
        if (rtc.day_tmp >= 30) { rtc.day_tmp = 30; }
      }
      if (rtc.month_tmp == 5) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 6) {
        if (rtc.day_tmp >= 30) { rtc.day_tmp = 30; }
      }
      if (rtc.month_tmp == 7) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 8) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 9) {
        if (rtc.day_tmp >= 30) { rtc.day_tmp = 30; }
      }
      if (rtc.month_tmp == 10) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
      if (rtc.month_tmp == 11) {
        if (rtc.day_tmp >= 30) { rtc.day_tmp = 30; }
      }
      if (rtc.month_tmp == 12) {
        if (rtc.day_tmp >= 31) { rtc.day_tmp = 31; }
      }
    }
    if (compareArray(cmd_p_clk_date_day_down, buffer_nextion)) {
      rtc.day_tmp -= 1;
      if (rtc.day_tmp < 1) {
        rtc.day_tmp = 1;
      }
    }
    if (compareArray(cmd_p_clk_time_second_up, buffer_nextion)) {
      rtc.second_tmp += 1;
      if (rtc.second_tmp >= 86400) {
        rtc.second_tmp %= 86400;
      }
    }
    if (compareArray(cmd_p_clk_time_second_down, buffer_nextion)) {
      rtc.second_tmp -= 1;
      if (rtc.second_tmp < 0) {
        rtc.second_tmp = 86400 + rtc.second_tmp;
      }
    }
  }
  // CLOCK TIME
  else if (page_current == 42) 
  {
    if (compareArray(cmd_p_clk_time_back, buffer_nextion)) page_current = 40;
    if (compareArray(cmd_p_clk_time_save, buffer_nextion)) {
      rtc.hour_cur = rtc.second_tmp / 3600;
      rtc.minute_cur = rtc.second_tmp % 3600 / 60;
      rtc.second_cur = rtc.second_tmp % 3600 % 60 / 1;
      rtc_lib.adjust(DateTime(rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur, rtc.second_cur));
      page_current = 40;
    }
    if (compareArray(cmd_p_clk_time_hour_up, buffer_nextion)) {
      rtc.second_tmp += 3600;
      if (rtc.second_tmp >= 86400) {
        rtc.second_tmp %= 86400;
      }
    }
    if (compareArray(cmd_p_clk_time_hour_down, buffer_nextion)) {
      rtc.second_tmp -= 3600;
      if (rtc.second_tmp < 0) {
        rtc.second_tmp = 86400 + rtc.second_tmp;
      }
    }
    if (compareArray(cmd_p_clk_time_minute_up, buffer_nextion)) {
      rtc.second_tmp += 60;
      if (rtc.second_tmp >= 86400) {
        rtc.second_tmp %= 86400;
      }
    }
    if (compareArray(cmd_p_clk_time_minute_down, buffer_nextion)) {
      rtc.second_tmp -= 60;
      if (rtc.second_tmp < 0) {
        rtc.second_tmp = 86400 + rtc.second_tmp;
      }
    }
    if (compareArray(cmd_p_clk_time_second_up, buffer_nextion)) {
      rtc.second_tmp += 1;
      if (rtc.second_tmp >= 86400) {
        rtc.second_tmp %= 86400;
      }
    }
    if (compareArray(cmd_p_clk_time_second_down, buffer_nextion)) {
      rtc.second_tmp -= 1;
      if (rtc.second_tmp < 0) {
        rtc.second_tmp = 86400 + rtc.second_tmp;
      }
    }
  }
  else if (page_current == 50) 
  {
    if (compareArray(cmd_forbidden, buffer_nextion)) 
    {
      page_current = 1;
    }
  }
  else if (page_current == 60) 
  {
    if (compareArray(cmd_forbidden, buffer_nextion)) 
    {
      page_current = 1;
    }
  }
}
