
void rtc_manager() {
  now_curr = rtc_lib.now();
  rtc.second_cur = now_curr.second();
  rtc.minute_cur = now_curr.minute();
  rtc.hour_cur = now_curr.hour();
  rtc.day_week = now_curr.dayOfTheWeek();

  rtc.year_cur = now_curr.year();
  rtc.month_cur = now_curr.month();
  rtc.day_cur = now_curr.day();
}