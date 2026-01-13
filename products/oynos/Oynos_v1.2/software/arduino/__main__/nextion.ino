// home
uint8_t cmd_p_home_on[BUFFER_SIZE] = { 101, 1, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_goto_settings[BUFFER_SIZE] = { 101, 1, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// power
uint8_t cmd_p_power_warn_no[BUFFER_SIZE] = { 101, 6, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_warn_yes[BUFFER_SIZE] = { 101, 6, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_back[BUFFER_SIZE] = { 101, 2, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_save[BUFFER_SIZE] = { 101, 2, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_up[BUFFER_SIZE] = { 101, 2, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_power_down[BUFFER_SIZE] = { 101, 2, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// calendar
uint8_t cmd_p_calendar_warn_no[BUFFER_SIZE] = { 101, 7, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_warn_yes[BUFFER_SIZE] = { 101, 7, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_goto_calendar[BUFFER_SIZE] = { 101, 1, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_back[BUFFER_SIZE] = { 101, 3, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_day_prev[BUFFER_SIZE] = { 101, 3, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_day_next[BUFFER_SIZE] = { 101, 3, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time0[BUFFER_SIZE] = { 101, 3, 40, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time1[BUFFER_SIZE] = { 101, 3, 32, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time2[BUFFER_SIZE] = { 101, 3, 33, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time3[BUFFER_SIZE] = { 101, 3, 34, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time4[BUFFER_SIZE] = { 101, 3, 35, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time5[BUFFER_SIZE] = { 101, 3, 36, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time6[BUFFER_SIZE] = { 101, 3, 37, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time7[BUFFER_SIZE] = { 101, 3, 38, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_time8[BUFFER_SIZE] = { 101, 3, 39, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_back[BUFFER_SIZE] = { 101, 8, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_save[BUFFER_SIZE] = { 101, 8, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_from_hour_up[BUFFER_SIZE] = { 101, 8, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_from_hour_down[BUFFER_SIZE] = { 101, 8, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_from_minute_up[BUFFER_SIZE] = { 101, 8, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_from_minute_down[BUFFER_SIZE] = { 101, 8, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_to_hour_up[BUFFER_SIZE] = { 101, 8, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_to_hour_down[BUFFER_SIZE] = { 101, 8, 12, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_to_minute_up[BUFFER_SIZE] = { 101, 8, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_to_minute_down[BUFFER_SIZE] = { 101, 8, 13, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_err_ok[BUFFER_SIZE] = { 101, 10, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_add_err2_ok[BUFFER_SIZE] = { 101, 11, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_del_no[BUFFER_SIZE] = { 101, 9, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_del_yes[BUFFER_SIZE] = { 101, 9, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// clock
uint8_t cmd_p_calendar_clock_no[BUFFER_SIZE] = { 101, 12, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_calendar_clock_yes[BUFFER_SIZE] = { 101, 12, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_back[BUFFER_SIZE] = { 101, 4, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date[BUFFER_SIZE] = { 101, 4, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time[BUFFER_SIZE] = { 101, 4, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_back[BUFFER_SIZE] = { 101, 13, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_save[BUFFER_SIZE] = { 101, 13, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_year_up[BUFFER_SIZE] = { 101, 13, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_year_down[BUFFER_SIZE] = { 101, 13, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_month_up[BUFFER_SIZE] = { 101, 13, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_month_down[BUFFER_SIZE] = { 101, 13, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_day_up[BUFFER_SIZE] = { 101, 13, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_date_day_down[BUFFER_SIZE] = { 101, 13, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_back[BUFFER_SIZE] = { 101, 14, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_save[BUFFER_SIZE] = { 101, 14, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_hour_up[BUFFER_SIZE] = { 101, 14, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_hour_down[BUFFER_SIZE] = { 101, 14, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_minute_up[BUFFER_SIZE] = { 101, 14, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_minute_down[BUFFER_SIZE] = { 101, 14, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_second_up[BUFFER_SIZE] = { 101, 14, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_clock_time_second_down[BUFFER_SIZE] = { 101, 14, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// settings
uint8_t cmd_p_set_back[BUFFER_SIZE] = { 101, 15, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_goto_ozone_power[BUFFER_SIZE] = { 101, 15, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_goto_calendar_onoff[BUFFER_SIZE] = { 101, 15, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_goto_calendar[BUFFER_SIZE] = { 101, 15, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_goto_clock[BUFFER_SIZE] = { 101, 15, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_goto_power_type[BUFFER_SIZE] = { 101, 15, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_goto_ozone_sensor_alarm[BUFFER_SIZE] = { 101, 15, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_goto_sensor_temperature[BUFFER_SIZE] = { 101, 15, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_goto_cycle_custom[BUFFER_SIZE] = { 101, 15, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// settings list
uint8_t cmd_p_set_list_back[BUFFER_SIZE] = { 101, 17, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_save[BUFFER_SIZE] = { 101, 17, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_item1_right[BUFFER_SIZE] = { 101, 17, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_item1_left[BUFFER_SIZE] = { 101, 17, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_item2_right[BUFFER_SIZE] = { 101, 17, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_item2_left[BUFFER_SIZE] = { 101, 17, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// settings list 3
uint8_t cmd_p_set_list_3_back[BUFFER_SIZE] = { 101, 20, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_3_save[BUFFER_SIZE] = { 101, 20, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_3_item1_right[BUFFER_SIZE] = { 101, 20, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_3_item1_left[BUFFER_SIZE] = { 101, 20, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_3_item2_right[BUFFER_SIZE] = { 101, 20, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_3_item2_left[BUFFER_SIZE] = { 101, 20, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_3_item3_right[BUFFER_SIZE] = { 101, 20, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_3_item3_left[BUFFER_SIZE] = { 101, 20, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// calendar onoff
uint8_t cmd_p_set_calendar_onoff_back[BUFFER_SIZE] = { 101, 16, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_calendar_onoff_save[BUFFER_SIZE] = { 101, 16, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_calendar_onoff_up[BUFFER_SIZE] = { 101, 16, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_calendar_onoff_down[BUFFER_SIZE] = { 101, 16, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// alarm
uint8_t cmd_p_alarm_ok[BUFFER_SIZE] = { 101, 18, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

//password
uint8_t cmd_p_password_ok[BUFFER_SIZE] = { 101, 19, 14, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_back[BUFFER_SIZE] = { 101, 19, 13, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_0[BUFFER_SIZE] = { 101, 19, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_1[BUFFER_SIZE] = { 101, 19, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_2[BUFFER_SIZE] = { 101, 19, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_3[BUFFER_SIZE] = { 101, 19, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_4[BUFFER_SIZE] = { 101, 19, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_5[BUFFER_SIZE] = { 101, 19, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_6[BUFFER_SIZE] = { 101, 19, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_7[BUFFER_SIZE] = { 101, 19, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_8[BUFFER_SIZE] = { 101, 19, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_9[BUFFER_SIZE] = { 101, 19, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_del[BUFFER_SIZE] = { 101, 19, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_password_clr[BUFFER_SIZE] = { 101, 19, 12, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

// settings list 4
uint8_t cmd_p_set_list_4_back[BUFFER_SIZE] = { 101, 21, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_save[BUFFER_SIZE] = { 101, 21, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_item1_left[BUFFER_SIZE] = { 101, 21, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_item1_right[BUFFER_SIZE] = { 101, 21, 12, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_item2_left[BUFFER_SIZE] = { 101, 21, 13, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_item2_right[BUFFER_SIZE] = { 101, 21, 14, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_item3_left[BUFFER_SIZE] = { 101, 21, 15, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_item3_right[BUFFER_SIZE] = { 101, 21, 16, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_item4_left[BUFFER_SIZE] = { 101, 21, 17, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_set_list_4_item4_right[BUFFER_SIZE] = { 101, 21, 18, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

bool nextion_array_compare(uint8_t *a, uint8_t *b) 
{
  for (uint8_t i = 0; i < BUFFER_SIZE; i++) 
  {
    if (a[i] != b[i]) 
    {
      return false;
    }
  }
  return true;
}

void nextion_debug_serial() 
{
  for (int i = 0; i < BUFFER_SIZE; i++) 
  {
    Serial.print(nextion.inputs_buff[i]);
    Serial.print(" ");
  }
  Serial.println();
}

void nextion_clear_buffer() 
{
  for (int i = 0; i < BUFFER_SIZE; i++) 
  {
    nextion.inputs_buff[i] = 0;
  }
}

void nextion_inputs() 
{
  if (Serial2.available()) 
  {
    nextion.bytestream_receiving = 1;
    nextion.inputs_buff[nextion.bytestream_buff_index] = Serial2.read();
    if (nextion.bytestream_buff_index < BUFFER_SIZE) 
    {
      nextion.bytestream_buff_index++;
    }
    nextion.bytestream_millis = millis();
  }
  if (nextion.bytestream_receiving == 1) 
  {
    if ((millis() - nextion.bytestream_millis) > 10) 
    {
      nextion.bytestream_receiving = 0;
      nextion.bytestream_buff_index = 0;
      nextion_eval_serial();
      nextion_debug_serial();
      nextion_clear_buffer();
    }
  }
}

void nextion_input_p_home()
{
  if (is_on_cur == 0)
  {
    if (nextion_array_compare(cmd_p_home_goto_settings, nextion.inputs_buff)) nextion.page_cur = P_PASSWORD;
  }
  {
    if (nextion_array_compare(cmd_p_home_on, nextion.inputs_buff))
    {
      if (is_on_cur == 1) is_on_cur = 0;
      else if (is_on_cur == 0) 
      {
        is_on_cur = 1;
        cycle.custom_cycles_init_state = 1;
      }
    }
  }
} 

void nextion_input_p_password()
{
  if (nextion_array_compare(cmd_p_password_ok, nextion.inputs_buff)) 
  {
    // valid password?
    int8_t valid_password = 1;
    for (int i = 0; i < PASSWORD_DIGITS_NUM; i++)
    {
      if (password.digits_cur[i] != password.digits_password[i])
      {
        valid_password = 0;
        password.password_errata_cur = 1;
        break;
      }
    }
    if (valid_password)
    {
      nextion.page_cur = P_SET;
      password.password_errata_cur = 0;
      // clear password
      for (int i = 0; i < PASSWORD_DIGITS_NUM; i++)
      {
        password.digits_cur[i] = -1;
      }
      password.digit_counter = 0;
    }
  }
  if (nextion_array_compare(cmd_p_password_back, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_HOME;
    password.password_errata_cur = 0;
    // clear password
    for (int i = 0; i < PASSWORD_DIGITS_NUM; i++)
    {
      password.digits_cur[i] = -1;
    }
    password.digit_counter = 0;
  }
  if (nextion_array_compare(cmd_p_password_0, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 0;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_1, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 1;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_2, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 2;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_3, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 3;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_4, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 4;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_5, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 5;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_6, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 6;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_7, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 7;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_8, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 8;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_9, nextion.inputs_buff)) 
  {
    if (password.digit_counter < PASSWORD_DIGITS_NUM)
    {
      password.digits_cur[password.digit_counter] = 9;
      password.digit_counter += 1;
    }
  }
  if (nextion_array_compare(cmd_p_password_del, nextion.inputs_buff)) 
  {
    if (password.digit_counter > 0)
    {
      password.digit_counter -= 1;
      password.digits_cur[password.digit_counter] = -1;
    }
  }
  if (nextion_array_compare(cmd_p_password_clr, nextion.inputs_buff)) 
  { 
    for (int i = 0; i < PASSWORD_DIGITS_NUM; i++)
    {
      password.digits_cur[i] = -1;
    }
    password.digit_counter = 0;
  }
}

void nextion_input_p_set()
{
  if (nextion_array_compare(cmd_p_set_back, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_HOME;
  }
  else if (nextion_array_compare(cmd_p_set_goto_ozone_power, nextion.inputs_buff))
  {
    nextion.page_cur = P_POWER;
  }
  else if (nextion_array_compare(cmd_p_set_goto_calendar_onoff, nextion.inputs_buff))
  {
    nextion.page_cur = P_CAL_EN;
  }
  else if (nextion_array_compare(cmd_p_set_goto_calendar, nextion.inputs_buff))
  {
    nextion.page_cur = P_CAL_TIME;
  }
  else if (nextion_array_compare(cmd_p_set_goto_clock, nextion.inputs_buff))
  {
    nextion.page_cur = P_CLK;
  }
  else if (nextion_array_compare(cmd_p_set_goto_power_type, nextion.inputs_buff))
  {
    nextion.page_cur = P_EXT;
  }
  else if (nextion_array_compare(cmd_p_set_goto_ozone_sensor_alarm, nextion.inputs_buff))
  {
    nextion.page_cur = P_SENSOR_ALARM;
  }
  else if (nextion_array_compare(cmd_p_set_goto_sensor_temperature, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_TEMPERATURE;
  }
  else if (nextion_array_compare(cmd_p_set_goto_cycle_custom, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_CYCLE_CUSTOM;
  }
}

void nextion_input_p_power()
{
  if (nextion_array_compare(cmd_p_power_back, nextion.inputs_buff)) 
  {
    power.power_tmp = power.power_cur;
    nextion.page_cur = P_SET;
  }
  if (nextion_array_compare(cmd_p_power_save, nextion.inputs_buff)) 
  {
    power.power_cur = power.power_tmp;
    nextion.page_cur = P_SET;
    EEPROM.write(10, power.power_cur);
    EEPROM.commit();
  }
  if (nextion_array_compare(cmd_p_power_up, nextion.inputs_buff)) 
  {
    power.power_tmp += 1;
    if (power.power_tmp > 2) power.power_tmp = 2;
  }
  if (nextion_array_compare(cmd_p_power_down, nextion.inputs_buff)) 
  {
    power.power_tmp -= 1;
    if (power.power_tmp < 0) power.power_tmp = 0;
  }
}

void nextion_input_p_cal_en()
{
  if (nextion_array_compare(cmd_p_set_calendar_onoff_back, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
  }
  else if (nextion_array_compare(cmd_p_set_calendar_onoff_save, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
    calendar_onoff_cur = calendar_onoff_tmp;
    eeprom_write_uint16(CALENDAR_ENABLED, calendar_onoff_cur);
  }
  else if (nextion_array_compare(cmd_p_set_calendar_onoff_up, nextion.inputs_buff)) 
  {
    calendar_onoff_tmp = 1;
  }
  else if (nextion_array_compare(cmd_p_set_calendar_onoff_down, nextion.inputs_buff)) 
  {
    calendar_onoff_tmp = 0;
  }
}

void nextion_input_p_cal_time()
{
  if (nextion_array_compare(cmd_p_calendar_back, nextion.inputs_buff)) nextion.page_cur = P_SET;
  if (nextion_array_compare(cmd_p_calendar_day_prev, nextion.inputs_buff))
  {
    day_of_week_cur -= 1;
    if (day_of_week_cur < 0) day_of_week_cur = 6;
  }
  if (nextion_array_compare(cmd_p_calendar_day_next, nextion.inputs_buff))
  {
    day_of_week_cur += 1;
    if (day_of_week_cur > 6) day_of_week_cur = 0;
  }
  if (nextion_array_compare(cmd_p_calendar_time0, nextion.inputs_buff))
  {
    cycle_i = 0;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
  if (nextion_array_compare(cmd_p_calendar_time1, nextion.inputs_buff))
  {
    cycle_i = 1;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
  if (nextion_array_compare(cmd_p_calendar_time2, nextion.inputs_buff))
  {
    cycle_i = 2;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
  if (nextion_array_compare(cmd_p_calendar_time3, nextion.inputs_buff))
  {
    cycle_i = 3;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
  if (nextion_array_compare(cmd_p_calendar_time4, nextion.inputs_buff))
  {
    cycle_i = 4;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
  if (nextion_array_compare(cmd_p_calendar_time5, nextion.inputs_buff))
  {
    cycle_i = 5;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
  if (nextion_array_compare(cmd_p_calendar_time6, nextion.inputs_buff))
  {
    cycle_i = 6;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
  if (nextion_array_compare(cmd_p_calendar_time7, nextion.inputs_buff))
  {
    cycle_i = 7;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
  if (nextion_array_compare(cmd_p_calendar_time8, nextion.inputs_buff))
  {
    cycle_i = 8;
    int32_t time_val = calendar_times[day_of_week_cur][cycle_i][0];
    if (time_val == -1)
    {
      nextion.page_cur = P_CAL_ADD;
    }
    else
    {
      nextion.page_cur = P_CAL_DEL;
    }
  }
}

void nextion_input_p_cal_add()
{
  if (nextion_array_compare(cmd_p_calendar_add_back, nextion.inputs_buff)) nextion.page_cur = P_CAL_TIME;
  if (nextion_array_compare(cmd_p_calendar_add_save, nextion.inputs_buff)) 
  {
    // ;jump
    int32_t seconds_from = (hour_from_tmp * 3600) + (minute_from_tmp * 60);
    int32_t seconds_to = (hour_to_tmp * 3600) + (minute_to_tmp * 60);

    bool is_time_valid = true;
    if (seconds_from >= seconds_to)
    {
      nextion.page_cur = P_CAL_ADD_ERR_NEG;
      is_time_valid = false;
    }
    for (int i = 0; i < CALENDAR_TIMERS_NUM; i++)
    {
      int32_t seconds_from_old = calendar_times[day_of_week_cur][i][0];
      int32_t seconds_to_old = calendar_times[day_of_week_cur][i][1];
      if (seconds_from >= seconds_from_old && seconds_from <= seconds_to_old)
      {
        nextion.page_cur = P_CAL_ADD_ERR_OVR;
        is_time_valid = false;
        break;
      }
      if (seconds_to >= seconds_from_old && seconds_to <= seconds_to_old)
      {
        nextion.page_cur = P_CAL_ADD_ERR_OVR;
        is_time_valid = false;
        break;
      }
      if (seconds_from <= seconds_from_old && seconds_to >= seconds_to_old)
      {
        nextion.page_cur = P_CAL_ADD_ERR_OVR;
        is_time_valid = false;
        break;
      }
    }

    if (is_time_valid)
    {
      calendar_times[day_of_week_cur][cycle_i][0] = seconds_from;
      calendar_times[day_of_week_cur][cycle_i][1] = seconds_to;
      Serial.print("CYCLE_I: ");
      Serial.println(cycle_i);
      nextion.page_cur = P_CAL_TIME;

      int address_1 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 0;
      int val = hour_from_tmp;
      EEPROM.write(address_1, val);
      EEPROM.commit();
      int address_2 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 1;
      val = minute_from_tmp;
      EEPROM.write(address_2, val);
      EEPROM.commit();
      int address_3 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 2;
      val = hour_to_tmp;
      EEPROM.write(address_3, val);
      EEPROM.commit();
      int address_4 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 3;
      val = minute_to_tmp;
      EEPROM.write(address_4, val);
      EEPROM.commit();
    }
  }
  if (nextion_array_compare(cmd_p_calendar_add_from_hour_up, nextion.inputs_buff)) 
  {
    hour_from_tmp += 1;
    if (hour_from_tmp > 23) hour_from_tmp = 0;
  }
  if (nextion_array_compare(cmd_p_calendar_add_from_hour_down, nextion.inputs_buff)) 
  {
    hour_from_tmp -= 1;
    if (hour_from_tmp < 0) hour_from_tmp = 23;
  }
  if (nextion_array_compare(cmd_p_calendar_add_from_minute_up, nextion.inputs_buff)) 
  {
    minute_from_tmp += 1;
    if (minute_from_tmp > 59) minute_from_tmp = 0;
  }
  if (nextion_array_compare(cmd_p_calendar_add_from_minute_down, nextion.inputs_buff)) 
  {
    minute_from_tmp -= 1;
    if (minute_from_tmp < 0) minute_from_tmp = 59;
  }
  if (nextion_array_compare(cmd_p_calendar_add_to_hour_up, nextion.inputs_buff)) 
  {
    hour_to_tmp += 1;
    if (hour_to_tmp > 23) hour_to_tmp = 0;
  }
  if (nextion_array_compare(cmd_p_calendar_add_to_hour_down, nextion.inputs_buff)) 
  {
    hour_to_tmp -= 1;
    if (hour_to_tmp < 0) hour_to_tmp = 23;
  }
  if (nextion_array_compare(cmd_p_calendar_add_to_minute_up, nextion.inputs_buff)) 
  {
    minute_to_tmp += 1;
    if (minute_to_tmp > 59) minute_to_tmp = 0;
  }
  if (nextion_array_compare(cmd_p_calendar_add_to_minute_down, nextion.inputs_buff)) 
  {
    minute_to_tmp -= 1;
    if (minute_to_tmp < 0) minute_to_tmp = 59;
  }
}

void nextion_input_p_cal_del()
{
  if (nextion_array_compare(cmd_p_calendar_del_no, nextion.inputs_buff)) nextion.page_cur = P_CAL_TIME;
  if (nextion_array_compare(cmd_p_calendar_del_yes, nextion.inputs_buff))
  {
    int32_t seconds_from = -1;
    int32_t seconds_to = -1;
    calendar_times[day_of_week_cur][cycle_i][0] = seconds_from;
    calendar_times[day_of_week_cur][cycle_i][1] = seconds_to;
    nextion.page_cur = P_CAL_TIME;

    int address_1 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 0;
    int val = 255;
    EEPROM.write(address_1, val);
    EEPROM.commit();
    int address_2 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 1;
    val = 255;
    EEPROM.write(address_2, val);
    EEPROM.commit();
    int address_3 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 2;
    val = 255;
    EEPROM.write(address_3, val);
    EEPROM.commit();
    int address_4 = 100 + (day_of_week_cur*100) + (cycle_i*10) + 3;
    val = 255;
    EEPROM.write(address_4, val);
    EEPROM.commit();
  }
}

void nextion_input_p_cal_add_err_neg()
{
  if (nextion_array_compare(cmd_p_calendar_add_err_ok, nextion.inputs_buff)) nextion.page_cur = P_CAL_ADD;
}

void nextion_input_p_cal_add_err_ovr()
{
  if (nextion_array_compare(cmd_p_calendar_add_err2_ok, nextion.inputs_buff)) nextion.page_cur = P_CAL_ADD;
}

void nextion_input_p_clk()
{
  if (nextion_array_compare(cmd_p_clock_back, nextion.inputs_buff)) nextion.page_cur = P_SET;
  if (nextion_array_compare(cmd_p_clock_date, nextion.inputs_buff))
  {
    nextion.page_cur = P_CLK_DATE;
    rtc.year_tmp = rtc.year_cur;
    rtc.month_tmp = rtc.month_cur;
    rtc.day_tmp = rtc.day_cur;
  }
  if (nextion_array_compare(cmd_p_clock_time, nextion.inputs_buff)) nextion.page_cur = P_CLK_TIME;
}

void nextion_input_p_clk_date()
{
  if (nextion_array_compare(cmd_p_clock_date_back, nextion.inputs_buff)) nextion.page_cur = P_CLK;
  if (nextion_array_compare(cmd_p_clock_date_save, nextion.inputs_buff)) 
  {
    rtc.year_cur = rtc.year_tmp;
    rtc.month_cur = rtc.month_tmp;
    rtc.day_cur = rtc.day_tmp;
    rtc_lib.adjust(DateTime(rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur, rtc.second_cur));
    nextion.page_cur = P_CLK;
  }
  if (nextion_array_compare(cmd_p_clock_date_year_up, nextion.inputs_buff))
  {
    rtc.year_tmp += 1;
  }
  if (nextion_array_compare(cmd_p_clock_date_year_down, nextion.inputs_buff))
  {
    rtc.year_tmp -= 1;
    if (rtc.year_tmp < 2020)
    {
      rtc.year_tmp = 2020;
    }
  }
  if (nextion_array_compare(cmd_p_clock_date_month_up, nextion.inputs_buff))
  {
    rtc.month_tmp += 1;
    if (rtc.month_tmp > 12)
    {
      rtc.month_tmp = 12;
    }
  }
  if (nextion_array_compare(cmd_p_clock_date_month_down, nextion.inputs_buff))
  {
    rtc.month_tmp -= 1;
    if (rtc.month_tmp < 1)
    {
      rtc.month_tmp = 1;
    }
  }
  if (nextion_array_compare(cmd_p_clock_date_day_up, nextion.inputs_buff))
  {
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
  if (nextion_array_compare(cmd_p_clock_date_day_down, nextion.inputs_buff))
  {
    rtc.day_tmp -= 1;
    if (rtc.day_tmp < 1)
    {
      rtc.day_tmp = 1;
    }
  }
}

void nextion_input_p_clk_time()
{
  if (nextion_array_compare(cmd_p_clock_time_back, nextion.inputs_buff)) nextion.page_cur = P_CLK;
  if (nextion_array_compare(cmd_p_clock_time_save, nextion.inputs_buff)) 
  {
    rtc.hour_cur = rtc.hour_tmp;
    rtc.minute_cur = rtc.minute_tmp;
    rtc.second_cur = rtc.second_tmp;
    rtc_lib.adjust(DateTime(rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur, rtc.second_cur));
    nextion.page_cur = P_CLK;
  }
  if (nextion_array_compare(cmd_p_clock_time_hour_up, nextion.inputs_buff))
  {
    rtc.hour_tmp += 1;
    if (rtc.hour_tmp > 23)
    {
      rtc.hour_tmp = 23;
    }
  }
  if (nextion_array_compare(cmd_p_clock_time_hour_down, nextion.inputs_buff))
  {
    rtc.hour_tmp -= 1;
    if (rtc.hour_tmp < 0)
    {
      rtc.hour_tmp = 0;
    }
  }
  if (nextion_array_compare(cmd_p_clock_time_minute_up, nextion.inputs_buff))
  {
    rtc.minute_tmp += 1;
    if (rtc.minute_tmp > 59)
    {
      rtc.minute_tmp = 59;
    }
  }
  if (nextion_array_compare(cmd_p_clock_time_minute_down, nextion.inputs_buff))
  {
    rtc.minute_tmp -= 1;
    if (rtc.minute_tmp < 0)
    {
      rtc.minute_tmp = 0;
    }
  }
  if (nextion_array_compare(cmd_p_clock_time_second_up, nextion.inputs_buff))
  {
    rtc.second_tmp += 1;
    if (rtc.second_tmp > 59)
    {
      rtc.second_tmp = 59;
    }
  }
  if (nextion_array_compare(cmd_p_clock_time_second_down, nextion.inputs_buff))
  {
    rtc.second_tmp -= 1;
    if (rtc.second_tmp < 0)
    {
      rtc.second_tmp = 0;
    }
  }
}

void nextion_input_p_ext()
{
  if (nextion_array_compare(cmd_p_set_calendar_onoff_back, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
  }
  else if (nextion_array_compare(cmd_p_set_calendar_onoff_save, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
    external_input.is_abilitated_cur = external_input.is_abilitated_tmp;
    eeprom_write_uint16(EXTERNAL_INPUT, external_input.is_abilitated_cur);
  }
  else if (nextion_array_compare(cmd_p_set_calendar_onoff_up, nextion.inputs_buff)) 
  {
    external_input.is_abilitated_tmp = 1;
  }
  else if (nextion_array_compare(cmd_p_set_calendar_onoff_down, nextion.inputs_buff)) 
  {
    external_input.is_abilitated_tmp = 0;
  }
}

void nextion_input_p_sensor_alarm()
{
  if (nextion_array_compare(cmd_p_set_list_3_back, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
  }
  else if (nextion_array_compare(cmd_p_set_list_3_save, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
    o3_sensor_alarm.enable_cur = o3_sensor_alarm.enable_tmp;
    o3_sensor_alarm.ppb_alarm_cur = o3_sensor_alarm.ppb_alarm_tmp;
    o3_sensor_alarm.alarm_timer_minutes_cur = o3_sensor_alarm.alarm_timer_minutes_tmp;
    eeprom_write_uint16(SENSOR_OZONE_ALARM_ENABLE, o3_sensor_alarm.enable_cur);
    eeprom_write_uint16(ALARM_PPB, o3_sensor_alarm.ppb_alarm_cur);
    eeprom_write_uint16(ALARM_TIMER_MINUTES, o3_sensor_alarm.alarm_timer_minutes_cur);
  }
  else if (nextion_array_compare(cmd_p_set_list_3_item1_right, nextion.inputs_buff)) 
  {
    if (o3_sensor_alarm.enable_tmp == 0)
    {
      o3_sensor_alarm.enable_tmp = 1;
    }
    else
    {
      o3_sensor_alarm.enable_tmp = 0;
    }
  }
  else if (nextion_array_compare(cmd_p_set_list_3_item1_left, nextion.inputs_buff)) 
  {
    if (o3_sensor_alarm.enable_tmp == 0)
    {
      o3_sensor_alarm.enable_tmp = 1;
    }
    else
    {
      o3_sensor_alarm.enable_tmp = 0;
    }
  }
  else if (nextion_array_compare(cmd_p_set_list_3_item2_right, nextion.inputs_buff)) 
  {
    if (o3_sensor_alarm.ppb_alarm_tmp < 9900)
    {
      o3_sensor_alarm.ppb_alarm_tmp += 100;
    }
  }
  else if (nextion_array_compare(cmd_p_set_list_3_item2_left, nextion.inputs_buff)) 
  {
    if (o3_sensor_alarm.ppb_alarm_tmp > 100)
    {
      o3_sensor_alarm.ppb_alarm_tmp -= 100;
    }
  }
  else if (nextion_array_compare(cmd_p_set_list_3_item3_right, nextion.inputs_buff)) 
  {
    if (o3_sensor_alarm.alarm_timer_minutes_tmp < 10)
    {
      o3_sensor_alarm.alarm_timer_minutes_tmp += 1;
    }
  }
  else if (nextion_array_compare(cmd_p_set_list_3_item3_left, nextion.inputs_buff)) 
  {
    if (o3_sensor_alarm.alarm_timer_minutes_tmp > 1)
    {
      o3_sensor_alarm.alarm_timer_minutes_tmp -= 1;
    }
  }
}

void nextion_input_p_ozone_alarm()
{
  if (nextion_array_compare(cmd_p_alarm_ok, nextion.inputs_buff)) 
  {
    nextion.page_cur = 1;
    // o3_sensor_alarm.is_alarm_cur = 0;
    o3_sensor_alarm.alarm_millis_cur = millis();
  }
}

void nextion_input_p_temperature_alarm()
{
  if (nextion_array_compare(cmd_p_alarm_ok, nextion.inputs_buff)) 
  {
    nextion.page_cur = 1;
    // o3_sensor_alarm.is_alarm_cur = 0;
    // o3_sensor_alarm.alarm_millis_cur = millis();
  }
}

void nextion_input_p_temperature()
{
  if (nextion_array_compare(cmd_p_set_list_back, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
  }
  else if (nextion_array_compare(cmd_p_set_list_save, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
    sensor_temperature.enable_cur = sensor_temperature.enable_tmp;
    sensor_temperature.alarm_seconds_cur = sensor_temperature.alarm_seconds_tmp;
    eeprom_write_uint16(SENSOR_TEMPERATURE_ENABLE, sensor_temperature.enable_cur);
    eeprom_write_uint16(SENSOR_TEMPERATURE_SECONDS, sensor_temperature.alarm_seconds_cur);
  }
  else if (nextion_array_compare(cmd_p_set_list_item1_right, nextion.inputs_buff)) 
  {
    if (sensor_temperature.enable_tmp == 0)
    {
      sensor_temperature.enable_tmp = 1;
    }
    else
    {
      sensor_temperature.enable_tmp = 0;
    }
  }
  else if (nextion_array_compare(cmd_p_set_list_item1_left, nextion.inputs_buff)) 
  {
    if (sensor_temperature.enable_tmp == 0)
    {
      sensor_temperature.enable_tmp = 1;
    }
    else
    {
      sensor_temperature.enable_tmp = 0;
    }
  }
  else if (nextion_array_compare(cmd_p_set_list_item2_right, nextion.inputs_buff)) 
  {
    sensor_temperature.alarm_seconds_tmp += 5;
    if (sensor_temperature.alarm_seconds_tmp > 60)
    {
      sensor_temperature.alarm_seconds_tmp = 60;
    }
  }
  else if (nextion_array_compare(cmd_p_set_list_item2_left, nextion.inputs_buff)) 
  {
    sensor_temperature.alarm_seconds_tmp -= 5;
    if (sensor_temperature.alarm_seconds_tmp < 5)
    {
      sensor_temperature.alarm_seconds_tmp = 5;
    }
  }
}

void nextion_input_p_cycle_custom()
{
  if (nextion_array_compare(cmd_p_set_list_4_back, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
  }
  else if (nextion_array_compare(cmd_p_set_list_4_save, nextion.inputs_buff)) 
  {
    nextion.page_cur = P_SET;
    cycle.custom_state_cur = cycle.custom_state_tmp;
    cycle.custom_minutes_working_cur = cycle.custom_minutes_working_tmp;
    cycle.custom_minutes_resting_cur = cycle.custom_minutes_resting_tmp;
    cycle.custom_cycles_num_cur = cycle.custom_cycles_num_tmp;
    eeprom_write_uint16(CUSTOM_STATE_CUR, cycle.custom_state_cur);
  }
  else if (nextion_array_compare(cmd_p_set_list_4_item1_left, nextion.inputs_buff)) 
  {
    cycle.custom_state_tmp = !cycle.custom_state_tmp;
  }
  else if (nextion_array_compare(cmd_p_set_list_4_item1_right, nextion.inputs_buff)) 
  {
    cycle.custom_state_tmp = !cycle.custom_state_tmp;
  }
  else if (nextion_array_compare(cmd_p_set_list_4_item2_left, nextion.inputs_buff)) 
  {
    cycle.custom_minutes_working_tmp -= 1;
    if (cycle.custom_minutes_working_tmp < 1) cycle.custom_minutes_working_tmp = 1;
  }
  else if (nextion_array_compare(cmd_p_set_list_4_item2_right, nextion.inputs_buff)) 
  {
    cycle.custom_minutes_working_tmp += 1;
    if (cycle.custom_minutes_working_tmp > 60) cycle.custom_minutes_working_tmp = 60;
  }
  else if (nextion_array_compare(cmd_p_set_list_4_item3_left, nextion.inputs_buff)) 
  {
    cycle.custom_minutes_resting_tmp -= 1;
    if (cycle.custom_minutes_resting_tmp < 1) cycle.custom_minutes_resting_tmp = 1;
  }
  else if (nextion_array_compare(cmd_p_set_list_4_item3_right, nextion.inputs_buff)) 
  {
    cycle.custom_minutes_resting_tmp += 1;
    if (cycle.custom_minutes_resting_tmp > 60) cycle.custom_minutes_resting_tmp = 60;
  }
  else if (nextion_array_compare(cmd_p_set_list_4_item4_left, nextion.inputs_buff)) 
  {
    cycle.custom_cycles_num_tmp -= 1;
    if (cycle.custom_cycles_num_tmp < 1) cycle.custom_cycles_num_tmp = 1;
  }
  else if (nextion_array_compare(cmd_p_set_list_4_item4_right, nextion.inputs_buff)) 
  {
    cycle.custom_cycles_num_tmp += 1;
    if (cycle.custom_cycles_num_tmp > 60) cycle.custom_cycles_num_tmp = 60;
  }
}

void nextion_eval_serial() 
{
  /**/ if (nextion.page_cur == P_HOME)              nextion_input_p_home();
  else if (nextion.page_cur == P_PASSWORD)          nextion_input_p_password();
  else if (nextion.page_cur == P_SET)               nextion_input_p_set();
  else if (nextion.page_cur == P_POWER)             nextion_input_p_power();
  else if (nextion.page_cur == P_CAL_EN)            nextion_input_p_cal_en();
  else if (nextion.page_cur == P_CAL_TIME)          nextion_input_p_cal_time();
  else if (nextion.page_cur == P_CAL_ADD)           nextion_input_p_cal_add();
  else if (nextion.page_cur == P_CAL_DEL)           nextion_input_p_cal_del();
  else if (nextion.page_cur == P_CAL_ADD_ERR_NEG)   nextion_input_p_cal_add_err_neg();
  else if (nextion.page_cur == P_CAL_ADD_ERR_OVR)   nextion_input_p_cal_add_err_ovr();
  else if (nextion.page_cur == P_CLK)               nextion_input_p_clk();
  else if (nextion.page_cur == P_CLK_DATE)          nextion_input_p_clk_date();
  else if (nextion.page_cur == P_CLK_TIME)          nextion_input_p_clk_time();
  else if (nextion.page_cur == P_EXT)               nextion_input_p_ext();
  else if (nextion.page_cur == P_SENSOR_ALARM)      nextion_input_p_sensor_alarm();
  else if (nextion.page_cur == P_OZONE_ALARM)       nextion_input_p_ozone_alarm();
  else if (nextion.page_cur == P_TEMPERATURE_ALARM) nextion_input_p_temperature_alarm();
  else if (nextion.page_cur == P_TEMPERATURE)       nextion_input_p_temperature();
  else if (nextion.page_cur == P_CYCLE_CUSTOM)      nextion_input_p_cycle_custom();
}

void nextion_update() 
{
  uint8_t force_refresh = 0;
  if (nextion.page_old != nextion.page_cur) 
  {
    nextion.page_old = nextion.page_cur;
    force_refresh = 1;
  }
  /**/ if (nextion.page_cur == P_HOME)              nextion_update_page_home(force_refresh);
  else if (nextion.page_cur == P_PASSWORD)          nextion_update_page_password(force_refresh);
  else if (nextion.page_cur == P_SET)               nextion_update_page_set(force_refresh);
  else if (nextion.page_cur == P_POWER)             nextion_update_page_power(force_refresh);
  else if (nextion.page_cur == P_CAL_EN)            nextion_update_page_calendar_onoff(force_refresh);
  else if (nextion.page_cur == P_CAL_TIME)          nextion_update_page_calendar(force_refresh);
  else if (nextion.page_cur == P_CAL_ADD)           nextion_update_page_calendar_add(force_refresh);
  else if (nextion.page_cur == P_CAL_DEL)           nextion_update_page_calendar_del(force_refresh);
  else if (nextion.page_cur == P_CAL_ADD_ERR_NEG)   nextion_update_page_calendar_add_err(force_refresh);
  else if (nextion.page_cur == P_CAL_ADD_ERR_OVR)   nextion_update_page_calendar_add_err2(force_refresh);
  else if (nextion.page_cur == P_CLK)               nextion_update_page_clock(force_refresh);
  else if (nextion.page_cur == P_CLK_DATE)          nextion_update_page_clock_date(force_refresh);
  else if (nextion.page_cur == P_CLK_TIME)          nextion_update_page_clock_time(force_refresh);
  else if (nextion.page_cur == P_EXT)               nextion_update_page_power_type(force_refresh);
  else if (nextion.page_cur == P_SENSOR_ALARM)      nextion_update_page_ozone_sensor_alarm(force_refresh);
  else if (nextion.page_cur == P_OZONE_ALARM)       nextion_update_page_ozone_alarm(force_refresh);
  else if (nextion.page_cur == P_TEMPERATURE_ALARM) nextion_update_page_temperature_alarm(force_refresh);
  else if (nextion.page_cur == P_TEMPERATURE)       nextion_update_page_sensor_temperature(force_refresh);
  else if (nextion.page_cur == P_CYCLE_CUSTOM)      nextion_update_page_cycle_custom(force_refresh);
}

////////////////////////////////////////////////////////
// ;home
////////////////////////////////////////////////////////
void nextion_update_page_home(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x68, 0x6F, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
    sensor.ppb_old = -2;
  }
  
  if (force_refresh || is_on_old != is_on_cur) 
  {
    is_on_old = is_on_cur;
    {
      if (is_on_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x38, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x37, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // calendar on off
  if (force_refresh || calendar_onoff_old != calendar_onoff_cur) 
  {
    calendar_onoff_old = calendar_onoff_cur;
    if (calendar_onoff_cur == 0)
    {
      {
        uint8_t _buffer[] = { 0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
    else
    {
      {
        uint8_t _buffer[] = { 0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // avvio esterno?
  if (force_refresh || external_input.is_abilitated_tmp != external_input.is_abilitated_cur) 
  {
    external_input.is_abilitated_tmp = external_input.is_abilitated_cur;
    if (external_input.is_abilitated_cur == 1)
    {
      {
        uint8_t _buffer[] = { 0x74, 0x34, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x49, 0x4E, 0x54, 0x45, 0x52, 0x2E, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
    else
    {
      {
        uint8_t _buffer[] = { 0x74, 0x34, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x45, 0x53, 0x54, 0x45, 0x52, 0x2E, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  
  // ozone sensor internal alarm
  if (force_refresh || o3_sensor_alarm.ppb_old != o3_sensor_alarm.ppb_cur) 
  {
    o3_sensor_alarm.ppb_old = o3_sensor_alarm.ppb_cur; 
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[9] = (o3_sensor_alarm.ppb_cur % 10000 / 1000) + 0x30;
      _buffer[11] = (o3_sensor_alarm.ppb_cur % 1000 / 100) + 0x30;
      _buffer[12] = (o3_sensor_alarm.ppb_cur % 100 / 10) + 0x30;
      _buffer[13] = (0) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  
  // ozone sensor external
  if (force_refresh || sensor.ppb_old != sensor.ppb_cur) 
  {
    sensor.ppb_old = sensor.ppb_cur;
    {
      if (sensor.is_connected == 1)
      {
        uint8_t _buffer[] = { 0x74, 0x35, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x2E, 0x30, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
        _buffer[9] = (sensor.ppb_cur % 10000 / 1000) + 0x30;
        _buffer[11] = (sensor.ppb_cur % 1000 / 100) + 0x30;
        _buffer[12] = (sensor.ppb_cur % 100 / 10) + 0x30;
        _buffer[13] = (sensor.ppb_cur % 10 / 1) + 0x30;
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else 
      {
        uint8_t _buffer[] = { 0x74, 0x35, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x2D, 0x2D, 0x2E, 0x2D, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }

  // clock
  if (force_refresh || rtc.second_old != rtc.second_cur) 
  {
    rtc.second_old = rtc.second_cur;      
    uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x55, 0x4E, 0x20, 0x30, 0x37, 0x2F, 0x30, 0x31, 0x2F, 0x32, 0x30, 0x32, 0x30, 0x20, 0x2D, 0x20, 0x31, 0x30, 0x3A, 0x33, 0x30, 0x3A, 0x33, 0x30, 0x22, 0xff, 0xff, 0xff };
    if (rtc.day_week_cur == 0)
    {
      _buffer[8] = 0x44;
      _buffer[9] = 0x4F;
      _buffer[10] = 0x4D;
    }
    else if (rtc.day_week_cur == 1)
    {
      _buffer[8] = 0x4C;
      _buffer[9] = 0x55;
      _buffer[10] = 0x4E;
    }
    else if (rtc.day_week_cur == 2)
    {
      _buffer[8] = 0x4D;
      _buffer[9] = 0x41;
      _buffer[10] = 0x52;
    }
    else if (rtc.day_week_cur == 3)
    {
      _buffer[8] = 0x4D;
      _buffer[9] = 0x45;
      _buffer[10] = 0x52;
    }
    else if (rtc.day_week_cur == 4)
    {
      _buffer[8] = 0x47;
      _buffer[9] = 0x49;
      _buffer[10] = 0x4F;
    }
    else if (rtc.day_week_cur == 5)
    {
      _buffer[8] = 0x56;
      _buffer[9] = 0x45;
      _buffer[10] = 0x4E;
    }
    else if (rtc.day_week_cur == 6)
    {
      _buffer[8] = 0x53;
      _buffer[9] = 0x41;
      _buffer[10] = 0x42;
    }
    
    _buffer[12] = (rtc.day_cur % 100 / 10) + 0x30;
    _buffer[13] = (rtc.day_cur % 10 / 1) + 0x30;
    _buffer[15] = (rtc.month_cur % 100 / 10) + 0x30;
    _buffer[16] = (rtc.month_cur % 10 / 1) + 0x30;
    _buffer[18] = (rtc.year_cur % 10000 / 1000) + 0x30;
    _buffer[19] = (rtc.year_cur % 1000 / 100) + 0x30;
    _buffer[20] = (rtc.year_cur % 100 / 10) + 0x30;
    _buffer[21] = (rtc.year_cur % 10 / 1) + 0x30;

    _buffer[25] = (rtc.hour_cur % 100 / 10) + 0x30;
    _buffer[26] = (rtc.hour_cur % 10 / 1) + 0x30;
    _buffer[28] = (rtc.minute_cur % 100 / 10) + 0x30;
    _buffer[29] = (rtc.minute_cur % 10 / 1) + 0x30;
    _buffer[31] = (rtc.second_cur % 100 / 10) + 0x30;
    _buffer[32] = (rtc.second_cur % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // power
  // if (force_refresh || power.power_old != power.power_cur) 
  // {
  //   power.power_old = power.power_cur;
  //   {
  //     uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
  //     for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
  //     {
  //       _buffer[8] = (power.power_cur) + 0x30;
  //       Serial2.write(_buffer[i]);
  //     }
  //   }
  // }
  if (force_refresh || power.power_old != power.power_cur)
  {
    power.power_old = power.power_cur;
    if (power.power_cur == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x31, 0x30, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (power.power_cur == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x32, 0x30, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (power.power_cur == 2)
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x31, 0x30, 0x78, 0x32, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}


////////////////////////////////////////////////////////
// ;power
////////////////////////////////////////////////////////
void nextion_update_page_power_warn(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x70, 0x6F, 0x77, 0x65, 0x72, 0x5F, 0x77, 0x61, 0x72, 0x6E, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_power(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x70, 0x6F, 0x77, 0x65, 0x72, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
    power.power_tmp = power.power_cur;
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        _buffer[8] = (power.power_tmp) + 0x30;
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || power.power_old != power.power_tmp)
  {
    power.power_old = power.power_tmp;
    if (power.power_tmp == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x31, 0x30, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (power.power_tmp == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x32, 0x30, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (power.power_tmp == 2)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x31, 0x30, 0x78, 0x32, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

////////////////////////////////////////////////////////
// ;calendar
////////////////////////////////////////////////////////
void nextion_update_page_calendar_warn(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x77, 0x61, 0x72, 0x6E, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_calendar(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x65, 0x6E, 0x64, 0x61, 0x72, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // DAY
  if (force_refresh || day_of_week_old != day_of_week_cur)
  {
    day_of_week_old = day_of_week_cur;
    if (day_of_week_cur == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x4F, 0x4D, 0x45, 0x4E, 0x49, 0x43, 0x41, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x55, 0x4E, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 2)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x41, 0x52, 0x54, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 3)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x45, 0x52, 0x43, 0x4F, 0x4C, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 4)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x49, 0x4F, 0x56, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 5)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x45, 0x4E, 0x45, 0x52, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 6)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x41, 0x42, 0x41, 0x54, 0x4F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    
    // calendar times
    for (int i = 0; i < CALENDAR_TIMERS_NUM; i++)
    {
      if (calendar_times[day_of_week_cur][i][0] != -1 && calendar_times[day_of_week_cur][i][1] != -1)
      {
        // icon (+, -)
        {
          int _index = i;
          uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x30, 0xff, 0xff, 0xff };
          _buffer[1] = (_index) + 0x30;
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        }
        // text
        {
          int _index = 2*i + 1;
          if (_index < 10)
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index) + 0x30;
            int32_t _second = calendar_times[day_of_week_cur][i][0];
            int32_t _hour = _second / 3600; 
            int32_t _minute = _second % 3600 / 60; 
            _buffer[11] = (_hour % 100 / 10) + 0x30;
            _buffer[12] = (_hour % 10 / 1) + 0x30;
            _buffer[14] = (_minute % 100 / 10) + 0x30;
            _buffer[15] = (_minute % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
          else
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index % 100 / 10) + 0x30;
            _buffer[2] = (_index % 10 / 1) + 0x30;
            int32_t _second = calendar_times[day_of_week_cur][i][0];
            int32_t _hour = _second / 3600; 
            int32_t _minute = _second % 3600 / 60; 
            _buffer[12] = (_hour % 100 / 10) + 0x30;
            _buffer[13] = (_hour % 10 / 1) + 0x30;
            _buffer[15] = (_minute % 100 / 10) + 0x30;
            _buffer[16] = (_minute % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
        }
        {
          int _index = 2*i + 2;
          if (_index < 10)
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index) + 0x30;
            int32_t _second = calendar_times[day_of_week_cur][i][1];
            int32_t _hour = _second / 3600; 
            int32_t _minute = _second % 3600 / 60; 
            _buffer[10] = (_hour % 100 / 10) + 0x30;
            _buffer[11] = (_hour % 10 / 1) + 0x30;
            _buffer[13] = (_minute % 100 / 10) + 0x30;
            _buffer[14] = (_minute % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
          else
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index % 100 / 10) + 0x30;
            _buffer[2] = (_index % 10 / 1) + 0x30;
            int32_t _second = calendar_times[day_of_week_cur][i][1];
            int32_t _hour = _second / 3600; 
            int32_t _minute = _second % 3600 / 60; 
            _buffer[11] = (_hour % 100 / 10) + 0x30;
            _buffer[12] = (_hour % 10 / 1) + 0x30;
            _buffer[14] = (_minute % 100 / 10) + 0x30;
            _buffer[15] = (_minute % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
        }
      }
      // not time
      else
      {
        {
          int _index = 2*i + 1;
          if (_index < 10)
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
          else
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index % 100 / 10) + 0x30;
            _buffer[2] = (_index % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
        }
        {
          int _index = 2*i + 2;
          if (_index < 10)
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
          else
          {
            uint8_t _buffer[] = { 0x74, 0x30, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x2D, 0x2D, 0x3A, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff };
            _buffer[1] = (_index % 100 / 10) + 0x30;
            _buffer[2] = (_index % 10 / 1) + 0x30;
            for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
            {
              Serial2.write(_buffer[i]);
            }
          }
        }
      }
    }
  }
}
void nextion_update_page_calendar_add(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x61, 0x64, 0x64, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // DAY
  if (force_refresh || day_of_week_old != day_of_week_cur)
  {
    day_of_week_old = day_of_week_cur;
    if (day_of_week_cur == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x4F, 0x4D, 0x45, 0x4E, 0x49, 0x43, 0x41, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4C, 0x55, 0x4E, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 2)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x41, 0x52, 0x54, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 3)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x45, 0x52, 0x43, 0x4F, 0x4C, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 4)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x47, 0x49, 0x4F, 0x56, 0x45, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 5)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x56, 0x45, 0x4E, 0x45, 0x52, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (day_of_week_cur == 6)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x41, 0x42, 0x41, 0x54, 0x4F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || hour_from_old != hour_from_tmp || minute_from_old != minute_from_tmp)
  {
    hour_from_old = hour_from_tmp;
    minute_from_old = minute_from_tmp;
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[11] = (hour_from_tmp % 100 / 10) + 0x30;
      _buffer[12] = (hour_from_tmp % 10 / 1) + 0x30;
      _buffer[14] = (minute_from_tmp % 100 / 10) + 0x30;
      _buffer[15] = (minute_from_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || hour_to_old != hour_to_tmp || minute_to_old != minute_to_tmp)
  {
    hour_to_old = hour_to_tmp;
    minute_to_old = minute_to_tmp;
    {
      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x20, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[10] = (hour_to_tmp % 100 / 10) + 0x30;
      _buffer[11] = (hour_to_tmp % 10 / 1) + 0x30;
      _buffer[13] = (minute_to_tmp % 100 / 10) + 0x30;
      _buffer[14] = (minute_to_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}
void nextion_update_page_calendar_add_err(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x61, 0x64, 0x64, 0x5F, 0x65, 0x72, 0x72, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_calendar_add_err2(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x61, 0x64, 0x64, 0x5F, 0x65, 0x72, 0x72, 0x32, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_calendar_del(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x61, 0x6C, 0x5F, 0x64, 0x65, 0x6C, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_clock_warn(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x77, 0x61, 0x72, 0x6E, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_clock(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6F, 0x63, 0x6B, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x44, 0x41, 0x54, 0x41, 0x20, 0x28, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x2F, 0x30, 0x30, 0x30, 0x30, 0x29, 0x22, 0xff, 0xff, 0xff };
      _buffer[14] = (rtc.day_cur % 100 / 10) + 0x30;
      _buffer[15] = (rtc.day_cur % 10 / 1) + 0x30;
      _buffer[17] = (rtc.month_cur % 100 / 10) + 0x30;
      _buffer[18] = (rtc.month_cur % 10 / 1) + 0x30;
      _buffer[20] = (rtc.year_cur % 10000 / 1000) + 0x30;
      _buffer[21] = (rtc.year_cur % 1000 / 100) + 0x30;
      _buffer[22] = (rtc.year_cur % 100 / 10) + 0x30;
      _buffer[23] = (rtc.year_cur % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x45, 0x4D, 0x50, 0x4F, 0x20, 0x28, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x29, 0x22, 0xff, 0xff, 0xff };
      _buffer[15] = (rtc.hour_cur % 100 / 10) + 0x30;
      _buffer[16] = (rtc.hour_cur % 10 / 1) + 0x30;
      _buffer[18] = (rtc.minute_cur % 100 / 10) + 0x30;
      _buffer[19] = (rtc.minute_cur % 10 / 1) + 0x30;
      _buffer[21] = (rtc.second_cur % 100 / 10) + 0x30;
      _buffer[22] = (rtc.second_cur % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}
void nextion_update_page_clock_date(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x64, 0x61, 0x74, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  if (force_refresh || rtc.year_old != rtc.year_tmp || rtc.month_old != rtc.month_tmp || rtc.day_old != rtc.day_tmp) 
  {
    rtc.year_old = rtc.year_tmp;
    rtc.month_old = rtc.month_tmp;
    rtc.day_old = rtc.day_tmp;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x31, 0x2F, 0x30, 0x31, 0x2F, 0x32, 0x30, 0x32, 0x30, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (rtc.day_tmp % 100 / 10) + 0x30;
    _buffer[9] = (rtc.day_tmp % 10 / 1) + 0x30;
    _buffer[11] = (rtc.month_tmp % 100 / 10) + 0x30;
    _buffer[12] = (rtc.month_tmp % 10 / 1) + 0x30;
    _buffer[14] = (rtc.year_tmp % 10000 / 1000) + 0x30;
    _buffer[15] = (rtc.year_tmp % 1000 / 100) + 0x30;
    _buffer[16] = (rtc.year_tmp % 100 / 10) + 0x30;
    _buffer[17] = (rtc.year_tmp % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}
void nextion_update_page_clock_time(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x63, 0x6C, 0x6B, 0x5F, 0x74, 0x69, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
  // sensor
  if (force_refresh || rtc.hour_old != rtc.hour_tmp || rtc.minute_old != rtc.minute_tmp || rtc.second_old != rtc.second_tmp) 
  {
    rtc.hour_old = rtc.hour_tmp;
    rtc.minute_old = rtc.minute_tmp;
    rtc.second_old = rtc.second_tmp;
    uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x3A, 0x30, 0x30, 0x22, 0xff, 0xff, 0xff };
    _buffer[8] = (rtc.hour_tmp % 100 / 10) + 0x30;
    _buffer[9] = (rtc.hour_tmp % 10 / 1) + 0x30;
    _buffer[11] = (rtc.minute_tmp % 100 / 10) + 0x30;
    _buffer[12] = (rtc.minute_tmp % 10 / 1) + 0x30;
    _buffer[14] = (rtc.second_tmp % 100 / 10) + 0x30;
    _buffer[15] = (rtc.second_tmp % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}

void nextion_update_page_analytics(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x61, 0x6E, 0x61, 0x6C, 0x79, 0x74, 0x69, 0x63, 0x73, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}

void nextion_update_page_set(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x73, 0x65, 0x74, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}

void nextion_update_page_calendar_onoff(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x73, 0x65, 0x74, 0x5F, 0x64, 0x61, 0x74, 0x61, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x55, 0x53, 0x41, 0x20, 0x43, 0x41, 0x4C, 0x45, 0x4E, 0x44, 0x41, 0x52, 0x49, 0x4F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    calendar_onoff_tmp = calendar_onoff_cur;
    if (calendar_onoff_tmp == 1)
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
    else
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  if (force_refresh || calendar_onoff_old != calendar_onoff_tmp)
  {
    calendar_onoff_old = calendar_onoff_tmp;
    if (calendar_onoff_tmp == 1)
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
    else
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
}

void nextion_update_page_power_type(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x73, 0x65, 0x74, 0x5F, 0x64, 0x61, 0x74, 0x61, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x45, 0x54, 0x4F, 0x44, 0x4F, 0x20, 0x41, 0x43, 0x43, 0x45, 0x4E, 0x53, 0x49, 0x4F, 0x4E, 0x45, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    external_input.is_abilitated_tmp = external_input.is_abilitated_cur;
    if (external_input.is_abilitated_tmp == 1)
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x49, 0x4E, 0x54, 0x45, 0x52, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
    else
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x45, 0x53, 0x54, 0x45, 0x52, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  if (force_refresh || external_input.is_abilitated_old != external_input.is_abilitated_tmp)
  {
    external_input.is_abilitated_old = external_input.is_abilitated_tmp;
    if (external_input.is_abilitated_tmp == 1)
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x49, 0x4E, 0x54, 0x45, 0x52, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
    else
    {
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x45, 0x53, 0x54, 0x45, 0x52, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
}

void nextion_update_page_ozone_sensor_alarm(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x73, 0x65, 0x74, 0x5F, 0x6C, 0x69, 0x73, 0x74, 0x5F, 0x33, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    o3_sensor_alarm.enable_tmp = o3_sensor_alarm.enable_cur;
    o3_sensor_alarm.ppb_alarm_tmp = o3_sensor_alarm.ppb_alarm_cur;
    o3_sensor_alarm.alarm_timer_minutes_tmp = o3_sensor_alarm.alarm_timer_minutes_cur;
    {
      //uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x41, 0x4C, 0x4C, 0x41, 0x52, 0x4D, 0x45, 0x3A, 0x20, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };

      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x41, 0x4C, 0x4C, 0x41, 0x52, 0x4D, 0x45, 0x3A, 0x20, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0X74, 0X31, 0X2E, 0X74, 0X78, 0X74, 0X3D, 0X22, 0X53, 0X45, 0X4E, 0X53, 0X4F, 0X52, 0X45, 0X20, 0X4F, 0X5A, 0X4F, 0X4E, 0X4F, 0X20, 0X41, 0X4C, 0X4C, 0X41, 0X52, 0X4D, 0X45, 0X20, 0X50, 0X50, 0X4D, 0X3A, 0X20, 0X30, 0X30, 0X2E, 0X31, 0X30, 0X30, 0X22, 0Xff, 0Xff, 0Xff };
      _buffer[36] = (o3_sensor_alarm.ppb_alarm_tmp % 10000 / 1000) + 0x30;
      _buffer[38] = (o3_sensor_alarm.ppb_alarm_tmp % 1000 / 100) + 0x30;
      _buffer[39] = (o3_sensor_alarm.ppb_alarm_tmp % 100 / 10) + 0x30;
      _buffer[40] = (o3_sensor_alarm.ppb_alarm_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x41, 0x4C, 0x4C, 0x41, 0x52, 0x4D, 0x45, 0x20, 0x54, 0x49, 0x4D, 0x45, 0x52, 0x20, 0x4D, 0x49, 0x4E, 0x55, 0x54, 0x49, 0x3A, 0x20, 0x30, 0x31, 0x22, 0xff, 0xff, 0xff };
      _buffer[44] = (o3_sensor_alarm.alarm_timer_minutes_tmp % 100 / 10) + 0x30;
      _buffer[45] = (o3_sensor_alarm.alarm_timer_minutes_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || o3_sensor_alarm.enable_old != o3_sensor_alarm.enable_tmp)
  {
    o3_sensor_alarm.enable_old = o3_sensor_alarm.enable_tmp;
    if (o3_sensor_alarm.enable_tmp == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x4F, 0x33, 0x20, 0x41, 0x4C, 0x4C, 0x41, 0x52, 0x4D, 0x45, 0x20, 0x50, 0x45, 0x52, 0x20, 0x54, 0x45, 0x53, 0x54, 0x3A, 0x20, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (o3_sensor_alarm.enable_tmp == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x4F, 0x33, 0x20, 0x41, 0x4C, 0x4C, 0x41, 0x52, 0x4D, 0x45, 0x20, 0x50, 0x45, 0x52, 0x20, 0x54, 0x45, 0x53, 0x54, 0x3A, 0x20, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x41, 0x4C, 0x4C, 0x41, 0x52, 0x4D, 0x45, 0x3A, 0x20, 0x45, 0x52, 0x52, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || o3_sensor_alarm.ppb_alarm_old != o3_sensor_alarm.ppb_alarm_tmp)
  {
    o3_sensor_alarm.ppb_alarm_old = o3_sensor_alarm.ppb_alarm_tmp;
    {
      uint8_t _buffer[] = { 0X74, 0X31, 0X2E, 0X74, 0X78, 0X74, 0X3D, 0X22, 0X53, 0X45, 0X4E, 0X53, 0X4F, 0X52, 0X45, 0X20, 0X4F, 0X5A, 0X4F, 0X4E, 0X4F, 0X20, 0X41, 0X4C, 0X4C, 0X41, 0X52, 0X4D, 0X45, 0X20, 0X50, 0X50, 0X4D, 0X3A, 0X20, 0X30, 0X30, 0X2E, 0X31, 0X30, 0X30, 0X22, 0Xff, 0Xff, 0Xff };
      _buffer[36] = (o3_sensor_alarm.ppb_alarm_tmp % 10000 / 1000) + 0x30;
      _buffer[38] = (o3_sensor_alarm.ppb_alarm_tmp % 1000 / 100) + 0x30;
      _buffer[39] = (o3_sensor_alarm.ppb_alarm_tmp % 100 / 10) + 0x30;
      _buffer[40] = (o3_sensor_alarm.ppb_alarm_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || o3_sensor_alarm.alarm_timer_minutes_old != o3_sensor_alarm.alarm_timer_minutes_tmp)
  {
    o3_sensor_alarm.alarm_timer_minutes_old = o3_sensor_alarm.alarm_timer_minutes_tmp;
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x20, 0x41, 0x4C, 0x4C, 0x41, 0x52, 0x4D, 0x45, 0x20, 0x54, 0x49, 0x4D, 0x45, 0x52, 0x20, 0x4D, 0x49, 0x4E, 0x55, 0x54, 0x49, 0x3A, 0x20, 0x30, 0x31, 0x22, 0xff, 0xff, 0xff };
      _buffer[44] = (o3_sensor_alarm.alarm_timer_minutes_tmp % 100 / 10) + 0x30;
      _buffer[45] = (o3_sensor_alarm.alarm_timer_minutes_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}


void nextion_update_page_ozone_alarm(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x61, 0x6C, 0x61, 0x72, 0x6D, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x45, 0x52, 0x44, 0x49, 0x54, 0x41, 0x20, 0x4F, 0x5A, 0x4F, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

void nextion_update_page_temperature_alarm(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x61, 0x6C, 0x61, 0x72, 0x6D, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x45, 0x4D, 0x50, 0x45, 0x52, 0x41, 0x54, 0x55, 0x52, 0x41, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

void nextion_update_page_password(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x70, 0x61, 0x73, 0x73, 0x77, 0x6F, 0x72, 0x64, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  
  // 0
  if (force_refresh || password.digits_old[0] != password.digits_cur[0])
  {
    password.digits_old[0] = password.digits_cur[0];
    if (password.digits_cur[0] >= 0)
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (password.digits_cur[0] % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x20, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // 1
  if (force_refresh || password.digits_old[1] != password.digits_cur[1])
  {
    password.digits_old[1] = password.digits_cur[1];
    if (password.digits_cur[1] >= 0)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (password.digits_cur[1] % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x20, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // 2
  if (force_refresh || password.digits_old[2] != password.digits_cur[2])
  {
    password.digits_old[2] = password.digits_cur[2];
    if (password.digits_cur[2] >= 0)
    {
      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (password.digits_cur[2] % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x20, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // 3
  if (force_refresh || password.digits_old[3] != password.digits_cur[3])
  {
    password.digits_old[3] = password.digits_cur[3];
    if (password.digits_cur[3] >= 0)
    {
      uint8_t _buffer[] = { 0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (password.digits_cur[3] % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x20, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // 4
  if (force_refresh || password.digits_old[4] != password.digits_cur[4])
  {
    password.digits_old[4] = password.digits_cur[4];
    if (password.digits_cur[4] >= 0)
    {
      uint8_t _buffer[] = { 0x74, 0x34, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (password.digits_cur[4] % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x34, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x20, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // 5
  if (force_refresh || password.digits_old[5] != password.digits_cur[5])
  {
    password.digits_old[5] = password.digits_cur[5];
    if (password.digits_cur[5] >= 0)
    {
      uint8_t _buffer[] = { 0x74, 0x35, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (password.digits_cur[5] % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x35, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x20, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // 6
  if (force_refresh || password.digits_old[6] != password.digits_cur[6])
  {
    password.digits_old[6] = password.digits_cur[6];
    if (password.digits_cur[6] >= 0)
    {
      uint8_t _buffer[] = { 0x74, 0x36, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (password.digits_cur[6] % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x36, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x20, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // 7
  if (force_refresh || password.digits_old[7] != password.digits_cur[7])
  {
    password.digits_old[7] = password.digits_cur[7];
    if (password.digits_cur[7] >= 0)
    {
      uint8_t _buffer[] = { 0x74, 0x37, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (password.digits_cur[7] % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x37, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x20, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  // password errata
  if (force_refresh || password.password_errata_old != password.password_errata_cur)
  {
    password.password_errata_old = password.password_errata_cur;
    if (password.password_errata_cur == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x38, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x50, 0x41, 0x53, 0x53, 0x57, 0x4F, 0x52, 0x44, 0x20, 0x45, 0x52, 0x52, 0x41, 0x54, 0x41, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}
void nextion_update_page_sensor_temperature(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    {
      uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x73, 0x65, 0x74, 0x5F, 0x6C, 0x69, 0x73, 0x74, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x54, 0x45, 0x4D, 0x50, 0x45, 0x52, 0x41, 0x54, 0x55, 0x52, 0x41, 0x3A, 0x20, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x49, 0x4D, 0x45, 0x52, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x54, 0x45, 0x4D, 0x50, 0x45, 0x52, 0x41, 0x54, 0x55, 0x52, 0x41, 0x3A, 0x20, 0x36, 0x30, 0x20, 0x53, 0x45, 0x43, 0x4F, 0x4E, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    sensor_temperature.enable_tmp = sensor_temperature.enable_cur;
    sensor_temperature.alarm_seconds_tmp = sensor_temperature.alarm_seconds_cur;
  }
  if (force_refresh || sensor_temperature.enable_old != sensor_temperature.enable_tmp)
  {
    sensor_temperature.enable_old = sensor_temperature.enable_tmp;
    if (sensor_temperature.enable_tmp == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x54, 0x45, 0x4D, 0x50, 0x45, 0x52, 0x41, 0x54, 0x55, 0x52, 0x41, 0x3A, 0x20, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else if (sensor_temperature.enable_tmp == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x54, 0x45, 0x4D, 0x50, 0x45, 0x52, 0x41, 0x54, 0x55, 0x52, 0x41, 0x3A, 0x20, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x42, 0x49, 0x4C, 0x49, 0x54, 0x41, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x54, 0x45, 0x4D, 0x50, 0x45, 0x52, 0x41, 0x54, 0x55, 0x52, 0x41, 0x3A, 0x20, 0x45, 0x52, 0x52, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || sensor_temperature.alarm_seconds_old != sensor_temperature.alarm_seconds_tmp)
  {
    sensor_temperature.alarm_seconds_old = sensor_temperature.alarm_seconds_tmp;
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x49, 0x4D, 0x45, 0x52, 0x20, 0x53, 0x45, 0x4E, 0x53, 0x4F, 0x52, 0x45, 0x20, 0x54, 0x45, 0x4D, 0x50, 0x45, 0x52, 0x41, 0x54, 0x55, 0x52, 0x41, 0x3A, 0x20, 0x36, 0x30, 0x20, 0x53, 0x45, 0x43, 0x4F, 0x4E, 0x44, 0x49, 0x22, 0xff, 0xff, 0xff };
      _buffer[35] = (sensor_temperature.alarm_seconds_tmp % 100 / 10) + 0x30;
      _buffer[36] = (sensor_temperature.alarm_seconds_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

// PAGE: cycle custom
void nextion_update_page_cycle_custom(uint8_t force_refresh) 
{
  if (force_refresh)
  {
    // page
    {
      uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x73, 0x65, 0x74, 0x5F, 0x6C, 0x69, 0x73, 0x74, 0x5F, 0x34, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    // options
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x41, 0x62, 0x69, 0x6C, 0x69, 0x74, 0x61, 0x20, 0x43, 0x69, 0x63, 0x6C, 0x6F, 0x20, 0x50, 0x65, 0x72, 0x73, 0x6F, 0x6E, 0x61, 0x6C, 0x69, 0x7A, 0x7A, 0x61, 0x74, 0x6F, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x65, 0x6D, 0x70, 0x6F, 0x20, 0x4C, 0x61, 0x76, 0x6F, 0x72, 0x6F, 0x20, 0x28, 0x4D, 0x69, 0x6E, 0x75, 0x74, 0x69, 0x29, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x34, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x54, 0x65, 0x6D, 0x70, 0x6F, 0x20, 0x50, 0x61, 0x75, 0x73, 0x61, 0x20, 0x28, 0x4D, 0x69, 0x6E, 0x75, 0x74, 0x69, 0x29, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x74, 0x36, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x75, 0x6D, 0x65, 0x72, 0x6F, 0x20, 0x43, 0x69, 0x63, 0x6C, 0x69, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    // arrows
    {
      uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x37, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x70, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x38, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x70, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x37, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x70, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x38, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x70, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x37, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x70, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x38, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x70, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x37, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    {
      uint8_t _buffer[] = { 0x70, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x38, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++)
      {
        Serial2.write(_buffer[i]);
      }
    }
    cycle.custom_state_tmp = cycle.custom_state_cur;
    cycle.custom_minutes_working_tmp = cycle.custom_minutes_working_cur;
    cycle.custom_minutes_resting_tmp = cycle.custom_minutes_resting_cur;
    cycle.custom_cycles_num_tmp = cycle.custom_cycles_num_cur;
  }
  if (force_refresh || cycle.custom_state_old != cycle.custom_state_tmp)
  {
    cycle.custom_state_old = cycle.custom_state_tmp;
    if (cycle.custom_state_tmp == 0)
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || cycle.custom_minutes_working_old != cycle.custom_minutes_working_tmp)
  {
    cycle.custom_minutes_working_old = cycle.custom_minutes_working_tmp;
    if (cycle.custom_minutes_working_tmp < 10)
    {
      uint8_t _buffer[] = { 0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x20, 0x4D, 0x69, 0x6E, 0x75, 0x74, 0x69, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (cycle.custom_minutes_working_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x33, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x31, 0x30, 0x20, 0x4D, 0x69, 0x6E, 0x75, 0x74, 0x69, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (cycle.custom_minutes_working_tmp % 100 / 10) + 0x30;
      _buffer[9] = (cycle.custom_minutes_working_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || cycle.custom_minutes_resting_old != cycle.custom_minutes_resting_tmp)
  {
    cycle.custom_minutes_resting_old = cycle.custom_minutes_resting_tmp;
    if (cycle.custom_minutes_resting_tmp < 10)
    {
      uint8_t _buffer[] = { 0x74, 0x35, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x20, 0x4D, 0x69, 0x6E, 0x75, 0x74, 0x69, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (cycle.custom_minutes_resting_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x35, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x31, 0x30, 0x20, 0x4D, 0x69, 0x6E, 0x75, 0x74, 0x69, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (cycle.custom_minutes_resting_tmp % 100 / 10) + 0x30;
      _buffer[9] = (cycle.custom_minutes_resting_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
  if (force_refresh || cycle.custom_cycles_num_old != cycle.custom_cycles_num_tmp)
  {
    cycle.custom_cycles_num_old = cycle.custom_cycles_num_tmp;
    if (cycle.custom_cycles_num_tmp < 10)
    {
      uint8_t _buffer[] = { 0x74, 0x37, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (cycle.custom_cycles_num_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x37, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x31, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (cycle.custom_cycles_num_tmp % 100 / 10) + 0x30;
      _buffer[9] = (cycle.custom_cycles_num_tmp % 10 / 1) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

void nextion_manager()
{
  nextion_inputs();
  nextion_update();
}