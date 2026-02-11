void rtc_manager() 
{
  now_cur = rtc_lib.now();
  rtc.second_cur = now_cur.second();
  rtc.minute_cur = now_cur.minute();
  rtc.hour_cur = now_cur.hour();
  rtc.day_week_cur = now_cur.dayOfTheWeek();

  rtc.year_cur = now_cur.year();
  rtc.month_cur = now_cur.month();
  rtc.day_cur = now_cur.day();

  sd_card.second_cur = now_cur.second();
  sd_card.buff_minute_cur = now_cur.minute();
  sd_card.buff_hour_cur = now_cur.hour();

}