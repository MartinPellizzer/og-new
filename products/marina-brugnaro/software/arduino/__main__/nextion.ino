uint8_t buffer_nextion[BUFFER_SIZE];

uint8_t cmd_splash[BUFFER_SIZE] = { 101, 0, 0, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_home_to_onoff[BUFFER_SIZE] = { 101, 1, 123, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_cycle[BUFFER_SIZE] = { 101, 1, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_calendar[BUFFER_SIZE] = { 101, 1, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_clock[BUFFER_SIZE] = { 101, 1, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_yesterday[BUFFER_SIZE] = { 101, 1, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_panel[BUFFER_SIZE] = { 101, 1, 123, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_home_to_sd[BUFFER_SIZE] = { 101, 1, 123, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_forbidden[BUFFER_SIZE] = { 101, 9, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_yesterday_to_home[BUFFER_SIZE] = { 101, 2, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_calendar_back[BUFFER_SIZE] = { 101, 3, 18, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_add[BUFFER_SIZE] = { 101, 3, 19, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_day_prev[BUFFER_SIZE] = { 101, 3, 20, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_day_next[BUFFER_SIZE] = { 101, 3, 21, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t1[BUFFER_SIZE] = { 101, 3, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t2[BUFFER_SIZE] = { 101, 3, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t3[BUFFER_SIZE] = { 101, 3, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t4[BUFFER_SIZE] = { 101, 3, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t5[BUFFER_SIZE] = { 101, 3, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t6[BUFFER_SIZE] = { 101, 3, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t7[BUFFER_SIZE] = { 101, 3, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t8[BUFFER_SIZE] = { 101, 3, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t9[BUFFER_SIZE] = { 101, 3, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t10[BUFFER_SIZE] = { 101, 3, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t11[BUFFER_SIZE] = { 101, 3, 12, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t12[BUFFER_SIZE] = { 101, 3, 13, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t13[BUFFER_SIZE] = { 101, 3, 14, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t14[BUFFER_SIZE] = { 101, 3, 15, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t15[BUFFER_SIZE] = { 101, 3, 16, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_calendar_t16[BUFFER_SIZE] = { 101, 3, 17, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_cal_add_back[BUFFER_SIZE] = { 101, 5, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_save[BUFFER_SIZE] = { 101, 5, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_hour_up[BUFFER_SIZE] = { 101, 5, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_hour_down[BUFFER_SIZE] = { 101, 5, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_minute_up[BUFFER_SIZE] = { 101, 5, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_cal_add_minute_down[BUFFER_SIZE] = { 101, 5, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_cycle_back[BUFFER_SIZE] = { 101, 4, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_save[BUFFER_SIZE] = { 101, 4, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_on_sub[BUFFER_SIZE] = { 101, 4, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_on_add[BUFFER_SIZE] = { 101, 4, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_ppb_sub[BUFFER_SIZE] = { 101, 4, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_ppb_add[BUFFER_SIZE] = { 101, 4, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_ppb_delta_sub[BUFFER_SIZE] = { 101, 4, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_cycle_ppb_delta_add[BUFFER_SIZE] = { 101, 4, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_clk_back[BUFFER_SIZE] = { 101, 6, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date[BUFFER_SIZE] = { 101, 6, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time[BUFFER_SIZE] = { 101, 6, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_clk_date_back[BUFFER_SIZE] = { 101, 7, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_save[BUFFER_SIZE] = { 101, 7, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_year_up[BUFFER_SIZE] = { 101, 7, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_year_down[BUFFER_SIZE] = { 101, 7, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_month_up[BUFFER_SIZE] = { 101, 7, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_month_down[BUFFER_SIZE] = { 101, 7, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_day_up[BUFFER_SIZE] = { 101, 7, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_date_day_down[BUFFER_SIZE] = { 101, 7, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_clk_time_back[BUFFER_SIZE] = { 101, 8, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_save[BUFFER_SIZE] = { 101, 8, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_hour_up[BUFFER_SIZE] = { 101, 8, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_hour_down[BUFFER_SIZE] = { 101, 8, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_minute_up[BUFFER_SIZE] = { 101, 8, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_minute_down[BUFFER_SIZE] = { 101, 8, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_second_up[BUFFER_SIZE] = { 101, 8, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clk_time_second_down[BUFFER_SIZE] = { 101, 8, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

bool compareArray(uint8_t *a, uint8_t *b) {
  for (uint8_t i = 0; i < BUFFER_SIZE; i++) {
    if (a[i] != b[i]) {
      return false;
    }
  }
  return true;
}

void nextionClearBuffer() {
  for (int i = 0; i < BUFFER_SIZE; i++) {
    buffer_nextion[i] = 0;
  }
}

void nextionDebugSerial() {
  for (int i = 0; i < BUFFER_SIZE; i++) {
    Serial.print(buffer_nextion[i]);
    Serial.print(" ");
  }
  Serial.println();
}

bool nextionExecCommand(uint8_t arr[], uint8_t arr_size) {
  for (uint8_t i = 0; i < arr_size; i++) {
    Serial2.write(arr[i]);
  }
}

void clear_buffer(uint8_t buff[], uint8_t len) {
  for (int i = 0; i < len; i++) buff[i] = 0;
}

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
      if (cycle.ppb_tmp > 9900) {
        cycle.ppb_tmp = 9900;
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


////////////////////////////////////////////////
// ;nextion
////////////////////////////////////////////////
void updateNextion() 
{
  uint8_t force_refresh = 0;
  if (page_old != page_current) 
  {
    page_old = page_current;
    force_refresh = 1;
  }
  if      (page_current == 1)  nextion_update_page_home(force_refresh);
  else if (page_current == 10) nextion_update_page_yesterday(force_refresh);
  else if (page_current == 20) nextion_update_page_calendar(force_refresh);
  else if (page_current == 21) nextion_update_p_cal_add(force_refresh);
  else if (page_current == 30) nextion_update_page_cycle(force_refresh);
  else if (page_current == 40) nextion_update_p_clk(force_refresh);
  else if (page_current == 41) nextion_update_p_clk_date(force_refresh);
  else if (page_current == 42) nextion_update_p_clk_time(force_refresh);
  else if (page_current == 50) nextion_update_p_forbidden(force_refresh);
  else if (page_current == 60) nextion_update_p_forbidden(force_refresh);
}

////////////////////////////////////////////////////////
// ;home
////////////////////////////////////////////////////////
void nextion_update_page_home(uint8_t force_refresh) 
{
  // page
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x61, 0x67, 0x65, 0x5F, 0x68, 0x6F, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // cycle minutes
  if (force_refresh) 
  {
    uint16_t minutes = cycle.seconds_on_cur / 60;
    if (minutes < 10)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (minutes % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (minutes < 100)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (minutes % 100 / 10) + 0x30;
      _buffer[9] = (minutes % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // cycle ppb
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (cycle.ppb_cur % 10000 / 1000) + 0x30;
    _buffer[10] = (cycle.ppb_cur % 1000 / 100) + 0x30;
    _buffer[11] = (cycle.ppb_cur % 100 / 10) + 0x30;
    _buffer[12] = (cycle.ppb_cur % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // sensor
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (sensor.ppb_curr % 10000 / 1000) + 0x30;
    _buffer[10] = (sensor.ppb_curr % 1000 / 100) + 0x30;
    _buffer[11] = (sensor.ppb_curr % 100 / 10) + 0x30;
    _buffer[12] = (sensor.ppb_curr % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }

  // rtc date
  if (force_refresh || rtc.day_tmp != rtc.day_cur) 
  {
    rtc.day_tmp = rtc.day_cur;
    uint8_t _buffer[] = { 0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x31, 0x2F, 0x30, 0x31, 0x2F, 0x32, 0x35, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (rtc.day_cur % 100 / 10) + 0x30;
    _buffer[9] = (rtc.day_cur % 10 / 1) + 0x30;
    _buffer[11] = (rtc.month_cur % 100 / 10) + 0x30;
    _buffer[12] = (rtc.month_cur % 10 / 1) + 0x30;
    _buffer[14] = (rtc.year_cur % 100 / 10) + 0x30;
    _buffer[15] = (rtc.year_cur % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
  
  // rtc time
  if (force_refresh || rtc.second_tmp != rtc.second_cur) 
  {
    rtc.second_tmp = rtc.second_cur;
    uint8_t _buffer[] = { 0x74, 0x34, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (rtc.hour_cur % 100 / 10) + 0x30;
    _buffer[9] = (rtc.hour_cur % 10 / 1) + 0x30;
    _buffer[11] = (rtc.minute_cur % 100 / 10) + 0x30;
    _buffer[12] = (rtc.minute_cur % 10 / 1) + 0x30;
    _buffer[14] = (rtc.second_cur % 100 / 10) + 0x30;
    _buffer[15] = (rtc.second_cur % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }

  /*
  // sd card
  if (force_refresh || sd_card.inserted_old != sd_card.inserted_cur) 
  {
    sd_card.inserted_old = sd_card.inserted_cur;
  }

  // calendar
  if (force_refresh || nextion_calendar_state_old != nextion_calendar_state_cur) {
    nextion_calendar_state_old = nextion_calendar_state_cur;
    if (nextion_calendar_state_cur == 1) {
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
    if (nextion_calendar_state_cur == 0) {
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // sensor
  if (force_refresh || sensor.connected_prev != sensor.connected_curr) 
  {
    sensor.connected_prev = sensor.connected_curr;
    if (sensor.connected_curr == 0) 
    {
      {
        uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      // rect
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    } else {
      {
        uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      // rect
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  if (force_refresh || sensor.ppb_prev != sensor.ppb_curr) 
  {
    sensor.ppb_prev = sensor.ppb_curr;
    if (sensor.ppb_curr == -1) 
    {
      uint8_t _buffer[] = {0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x2D, 0x2D, 0x2E, 0x2D, 0x2D, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    } 
    else 
    {
      uint8_t _buffer[] = {0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
      _buffer[9] = (sensor.ppb_curr % 10000 / 1000) + 0x30;
      _buffer[11] = (sensor.ppb_curr % 1000 / 100) + 0x30;
      _buffer[12] = (sensor.ppb_curr % 100 / 10) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }*/
}

///////////////////////////////////////////////////////////////////////
// ;yesterday
///////////////////////////////////////////////////////////////////////
void nextion_update_page_yesterday(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t cmd_page_home[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x61, 0x67, 0x65, 0x5F, 0x79, 0x65, 0x73, 0x74, 0x65, 0x72, 0x64, 0x61, 0x79, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(cmd_page_home) / sizeof(uint8_t); i++) 
    {
      Serial2.write(cmd_page_home[i]);
    }
  }
  if (force_refresh || yesterday.is_buff_updated) 
  {
    yesterday.is_buff_updated = false;
    for (uint8_t i = 0; i < YESTERDAY_BUFF_NUM; i++) 
    {
      if (yesterday.buff[i] != -1) 
      {
        if (i < 10) 
        {
          uint8_t _buffer[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x2D, 0x30, 0x30, 0x3A, 0x20, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
          _buffer[1] = (i) + 0x30;
          _buffer[9] = (i % 100 / 10) + 0x30;
          _buffer[10] = (i % 10 / 1) + 0x30;
          _buffer[13] = (yesterday.buff[i] % 100000 / 10000) + 0x30;
          _buffer[14] = (yesterday.buff[i] % 10000 / 1000) + 0x30;
          _buffer[16] = (yesterday.buff[i] % 1000 / 100) + 0x30;
          _buffer[17] = (yesterday.buff[i] % 100 / 10) + 0x30;
          _buffer[18] = (yesterday.buff[i] % 10 / 1) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        } 
        else 
        {
          uint8_t _buffer[] = {0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x2D, 0x30, 0x30, 0x3A, 0x20, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
          _buffer[1] = (i % 100 / 10) + 0x30;
          _buffer[2] = (i % 10 / 1) + 0x30;
          _buffer[10] = (i % 100 / 10) + 0x30;
          _buffer[11] = (i % 10 / 1) + 0x30;
          _buffer[14] = (yesterday.buff[i] % 100000 / 10000) + 0x30;
          _buffer[15] = (yesterday.buff[i] % 10000 / 1000) + 0x30;
          _buffer[17] = (yesterday.buff[i] % 1000 / 100) + 0x30;
          _buffer[18] = (yesterday.buff[i] % 100 / 10) + 0x30;
          _buffer[19] = (yesterday.buff[i] % 10 / 1) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        } 
      }
    }
  }
}
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* ;calendar */
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_page_calendar(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t cmd_page_home[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x61, 0x67, 0x65, 0x5F, 0x63, 0x61, 0x6C, 0x65, 0x6E, 0x64, 0x61, 0x72, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(cmd_page_home) / sizeof(uint8_t); i++) {
      Serial2.write(cmd_page_home[i]);
    }
    day_old = -1;
  }
  if (force_refresh || day_old != day_curr) {
    day_old = day_curr;
    if (day_curr == 1)  // Lunedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x75, 0x6E, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 2)  // Martedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x61, 0x72, 0x74, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 3)  // Mercoledi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x65, 0x72, 0x63, 0x6F, 0x6C, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 4)  // Giovedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x69, 0x6F, 0x76, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 5)  // Venerdi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x65, 0x6E, 0x65, 0x72, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 6)  // Sabato
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x61, 0x62, 0x61, 0x74, 0x6F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 0)  // Domenica
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x6F, 0x6D, 0x65, 0x6E, 0x69, 0x63, 0x61, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    }

    for (int timer_index = 0; timer_index < CALENDAR_TIMERS_NUM; timer_index++) {
      int32_t _seconds = calendar_days[day_curr][timer_index];
      int timer_index_display = timer_index + 1;  // OFFSET TO THE FIRST TEXT WITGET OF NEXTION TFT
      if (_seconds < 0) {
        if (timer_index_display < 10) {
          uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x5F, 0x5F, 0x3A, 0x5F, 0x5F, 0x22, 0xff, 0xff, 0xff };
          _buffer[1] = (timer_index_display % 10 / 1) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
            Serial2.write(_buffer[i]);
          }
        } else {
          uint8_t _buffer[] = { 0x74, 0x31, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x5F, 0x5F, 0x3A, 0x5F, 0x5F, 0x22, 0xff, 0xff, 0xff };
          _buffer[1] = (timer_index_display % 100 / 10) + 0x30;
          _buffer[2] = (timer_index_display % 10 / 1) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
            Serial2.write(_buffer[i]);
          }
        }
      } 
      else 
      {
        if (timer_index_display < 10) 
        {
          uint8_t _buffer[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x20, 0x58, 0x22, 0xff, 0xff, 0xff};
          _buffer[1] = (timer_index_display % 10 / 1) + 0x30;
          int hour = _seconds / 3600;
          int hour_1 = hour % 100 / 10;
          int hour_2 = hour % 10 / 1;
          int minute = _seconds % 3600 / 60;
          int minute_1 = minute % 100 / 10;
          int minute_2 = minute % 10 / 1;
          _buffer[8] = (hour_1) + 0x30;
          _buffer[9] = (hour_2) + 0x30;
          _buffer[11] = (minute_1) + 0x30;
          _buffer[12] = (minute_2) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        } 
        else 
        {
          uint8_t _buffer[] = {0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x20, 0x58, 0x22, 0xff, 0xff, 0xff};
          _buffer[1] = (timer_index_display % 100 / 10) + 0x30;
          _buffer[2] = (timer_index_display % 10 / 1) + 0x30;
          int hour = _seconds / 3600;
          int hour_1 = hour % 100 / 10;
          int hour_2 = hour % 10 / 1;
          int minute = _seconds % 3600 / 60;
          int minute_1 = minute % 100 / 10;
          int minute_2 = minute % 10 / 1;
          _buffer[9] = (hour_1) + 0x30;
          _buffer[10] = (hour_2) + 0x30;
          _buffer[12] = (minute_1) + 0x30;
          _buffer[13] = (minute_2) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        }
      }
    }
  }
}
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* PAGE CALENDAR ADD */
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_p_cal_add(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x61, 0x64, 0x64, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    day_old = -1;

    cycle_second_old = -1;
    cycle_seconds_tmp = 0;
  }
  if (force_refresh || day_old != day_curr) {
    day_old = day_curr;
    if (day_curr == 1)  // Lunedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x75, 0x6E, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 2)  // Martedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x61, 0x72, 0x74, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 3)  // Mercoledi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x65, 0x72, 0x63, 0x6F, 0x6C, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 4)  // Giovedi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x69, 0x6F, 0x76, 0x65, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 5)  // Venerdi
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x65, 0x6E, 0x65, 0x72, 0x64, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 6)  // Sabato
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x61, 0x62, 0x61, 0x74, 0x6F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    } else if (day_curr == 0)  // Domenica
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x6F, 0x6D, 0x65, 0x6E, 0x69, 0x63, 0x61, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || cycle_second_old != cycle_seconds_tmp) {
    cycle_second_old = cycle_seconds_tmp;
    uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    int hour = cycle_seconds_tmp / 3600;
    int hour_1 = hour % 100 / 10;
    int hour_2 = hour % 10 / 1;
    int minute = cycle_seconds_tmp % 3600 / 60;
    int minute_1 = minute % 100 / 10;
    int minute_2 = minute % 10 / 1;
    _buffer[8] = (hour_1) + 0x30;
    _buffer[9] = (hour_2) + 0x30;
    _buffer[11] = (minute_1) + 0x30;
    _buffer[12] = (minute_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
}
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* ;cycle */
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_page_cycle(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x61, 0x67, 0x65, 0x5F, 0x63, 0x79, 0x63, 0x6C, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    cycle.seconds_on_old = -1;
    cycle.seconds_on_tmp = cycle.seconds_on_cur;
    cycle.ppb_old = -1;
    cycle.ppb_tmp = cycle.ppb_cur;
    cycle.ppb_delta_old = -1;
    cycle.ppb_delta_tmp = cycle.ppb_delta_cur;
  }
  if (force_refresh || cycle.seconds_on_old != cycle.seconds_on_tmp) {
    cycle.seconds_on_old = cycle.seconds_on_tmp;
    uint8_t _buffer[] = {0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x45, 0x4D, 0x50, 0x4F, 0x20, 0x43, 0x49, 0x43, 0x4C, 0x4F, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x20, 0x6D, 0x69, 0x6E, 0x75, 0x74, 0x69, 0x22, 0xff, 0xff, 0xff};
    int minute = cycle.seconds_on_tmp / 60;
    int minute_1 = minute % 100 / 10;
    int minute_2 = minute % 10 / 1;
    _buffer[22] = (minute_1) + 0x30;
    _buffer[23] = (minute_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh || cycle.ppb_old != cycle.ppb_tmp) {
    cycle.ppb_old = cycle.ppb_tmp;
    uint8_t _buffer[] = {0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x50, 0x4D, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x54, 0x41, 0x52, 0x47, 0x45, 0x54, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x20, 0x70, 0x70, 0x6D, 0x22, 0xff, 0xff, 0xff};
    int ppm = cycle.ppb_tmp;
    int ppm_1 = ppm % 100000 / 10000;
    int ppm_2 = ppm % 10000 / 1000;
    int ppm_3 = ppm % 1000 / 100;
    int ppm_4 = ppm % 100 / 10;
    int ppm_5 = ppm % 10 / 1;
    _buffer[27] = (ppm_1) + 0x30;
    _buffer[28] = (ppm_2) + 0x30;
    _buffer[30] = (ppm_3) + 0x30;
    _buffer[31] = (ppm_4) + 0x30;
    _buffer[32] = (ppm_5) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh || cycle.ppb_delta_old != cycle.ppb_delta_tmp) {
    cycle.ppb_delta_old = cycle.ppb_delta_tmp;
    uint8_t _buffer[] = {0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x4F, 0x4C, 0x4C, 0x45, 0x52, 0x41, 0x4E, 0x5A, 0x41, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x2D, 0x20, 0x32, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff};
    int ppm_delta = cycle.ppb_delta_tmp;
    int ppm_delta_1 = ppm_delta % 100 / 10;
    int ppm_delta_2 = ppm_delta % 10 / 1;
    _buffer[27] = (ppm_delta_1) + 0x30;
    _buffer[28] = (ppm_delta_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
}
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* ;clock */
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_p_clk(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x73, 0x65, 0x74, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    // DATE
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x54, 0x41, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x20, 0x28, 0x61, 0x6E, 0x6E, 0x6F, 0x2F, 0x6D, 0x65, 0x73, 0x65, 0x2F, 0x67, 0x69, 0x6F, 0x72, 0x6E, 0x6F, 0x29, 0x22, 0xff, 0xff, 0xff };
      int year_1 = rtc.year_cur % 10000 / 1000;
      int year_2 = rtc.year_cur % 1000 / 100;
      int year_3 = rtc.year_cur % 100 / 10;
      int year_4 = rtc.year_cur % 10 / 1;
      _buffer[15] = (year_1) + 0x30;
      _buffer[16] = (year_2) + 0x30;
      _buffer[17] = (year_3) + 0x30;
      _buffer[18] = (year_4) + 0x30;
      int month_1 = rtc.month_cur % 100 / 10;
      int month_2 = rtc.month_cur % 10 / 1;
      _buffer[20] = (month_1) + 0x30;
      _buffer[21] = (month_2) + 0x30;
      int day_1 = rtc.day_cur % 100 / 10;
      int day_2 = rtc.day_cur % 10 / 1;
      _buffer[23] = (day_1) + 0x30;
      _buffer[24] = (day_2) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    }
    // TIME
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x45, 0x4D, 0x50, 0x4F, 0x20, 0x2D, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x20, 0x28, 0x6F, 0x72, 0x61, 0x3A, 0x6D, 0x69, 0x6E, 0x75, 0x74, 0x6F, 0x3A, 0x73, 0x65, 0x63, 0x6F, 0x6E, 0x64, 0x6F, 0x29, 0x22, 0xff, 0xff, 0xff };
      int hour = rtc.hour_cur;
      int hour_1 = hour % 100 / 10;
      int hour_2 = hour % 10 / 1;
      _buffer[16] = (hour_1) + 0x30;
      _buffer[17] = (hour_2) + 0x30;
      int minute = rtc.minute_cur;
      int minute_1 = minute % 100 / 10;
      int minute_2 = minute % 10 / 1;
      _buffer[19] = (minute_1) + 0x30;
      _buffer[20] = (minute_2) + 0x30;
      int second = rtc.second_cur;
      int second_1 = second % 100 / 10;
      int second_2 = second % 10 / 1;
      _buffer[22] = (second_1) + 0x30;
      _buffer[23] = (second_2) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* PAGE CLOCK DATE*/
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_p_clk_date(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x64, 0x61, 0x74, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    rtc.year_old = -1;
    rtc.year_tmp = rtc.year_cur;
    rtc.month_old = -1;
    rtc.month_tmp = rtc.month_cur;
    rtc.day_old = -1;
    rtc.day_tmp = rtc.day_cur;
  }
  if (force_refresh || rtc.year_old != rtc.year_tmp || rtc.month_old != rtc.month_tmp || rtc.day_old != rtc.day_tmp) {
    rtc.year_old = rtc.year_tmp;
    rtc.month_old = rtc.month_tmp;
    rtc.day_old = rtc.day_tmp;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    int year_1 = rtc.year_tmp % 10000 / 1000;
    int year_2 = rtc.year_tmp % 1000 / 100;
    int year_3 = rtc.year_tmp % 100 / 10;
    int year_4 = rtc.year_tmp % 10 / 1;
    _buffer[8] = (year_1) + 0x30;
    _buffer[9] = (year_2) + 0x30;
    _buffer[10] = (year_3) + 0x30;
    _buffer[11] = (year_4) + 0x30;
    int month_1 = rtc.month_tmp % 100 / 10;
    int month_2 = rtc.month_tmp % 10 / 1;
    _buffer[13] = (month_1) + 0x30;
    _buffer[14] = (month_2) + 0x30;
    int day_1 = rtc.day_tmp % 100 / 10;
    int day_2 = rtc.day_tmp % 10 / 1;
    _buffer[16] = (day_1) + 0x30;
    _buffer[17] = (day_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
}

/* ------------------------------------------------------------------------------------------------------------------------------------------- */
/* PAGE CLOCK TIME*/
/* ------------------------------------------------------------------------------------------------------------------------------------------- */
void nextion_update_p_clk_time(uint8_t force_refresh) {
  if (force_refresh) {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x74, 0x69, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
    rtc.second_old = -1;
    rtc.second_tmp = rtc.second_cur + (rtc.minute_cur * 60) + (rtc.hour_cur * 3600);
  }
  if (force_refresh || rtc.second_old != rtc.second_tmp) {
    rtc.second_old = rtc.second_tmp;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    int hour = rtc.second_tmp / 3600;
    int hour_1 = hour % 100 / 10;
    int hour_2 = hour % 10 / 1;
    int minute = rtc.second_tmp % 3600 / 60;
    int minute_1 = minute % 100 / 10;
    int minute_2 = minute % 10 / 1;
    int second = rtc.second_tmp % 3600 % 60 / 1;
    int second_1 = second % 100 / 10;
    int second_2 = second % 10 / 1;
    _buffer[8] = (hour_1) + 0x30;
    _buffer[9] = (hour_2) + 0x30;
    _buffer[11] = (minute_1) + 0x30;
    _buffer[12] = (minute_2) + 0x30;
    _buffer[14] = (second_1) + 0x30;
    _buffer[15] = (second_2) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) {
      Serial2.write(_buffer[i]);
    }
  }
}


///////////////////////////////////////////////////////
// ;forbidden
///////////////////////////////////////////////////////
void nextion_update_p_forbidden(uint8_t force_refresh) 
{
 if (force_refresh) 
 {
    uint8_t _buffer[] = {0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x66, 0x6F, 0x72, 0x62, 0x69, 0x64, 0x64, 0x65, 0x6E, 0xff, 0xff, 0xff};
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}

void nextion_manage() 
{
  listenNextion();
  updateNextion();
}