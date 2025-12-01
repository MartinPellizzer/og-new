void yesterday_update() 
{
  if (yesterday.hour_old != rtc.hour_cur) 
  {
    yesterday.hour_old = rtc.hour_cur;
    for (int i = YESTERDAY_BUFF_NUM - 1; i >= 0; i--)
    {
      yesterday.buff[i+1] = yesterday.buff[i];
    }
    yesterday.buff[0] = sensor.ppb_curr;
    yesterday.is_buff_updated = true;
  }
}
