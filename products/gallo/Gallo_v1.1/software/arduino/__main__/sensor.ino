
void clear_buffer(uint8_t buff[], uint8_t len) 
{
  for (int i = 0; i < len; i++) buff[i] = 0;
}

void sensor_update() 
{
  // check if sensor is connected, otherwise update state/val
  if (sensor.is_connected == 1) 
  {
    if (millis() - sensor_connected_millis > 1000) 
    {
      sensor_connected_millis = millis();
      sensor_connected_seconds += 1;
      if (sensor_connected_seconds > 5)
      {
        sensor.is_connected = 0;
        sensor.ppb_old = -2;
        sensor.ppb_cur = -1;
      }
    }
  }

  if (sensor_new_data) 
  {
    if (millis() - timer > 40) 
    {
      for (int i = 0; i < BUFF_LEN; i++)
      {
        Serial.print(buff[i]);
        Serial.print(", ");
      }
      Serial.println();

      timer_no_signal = millis();
      i = 0;
      sensor_new_data = 0;
      sensor.ppb_cur = 0;
      if (checksum(buff, 9) == buff[8]) 
      {
        sensor.ppb_cur = buff[4] * 256 + buff[5];
        sensor_connected_millis = millis();
        sensor_connected_seconds = 0;
        sensor.is_connected = 1;
        Serial.println(sensor.ppb_cur);
      }
      clear_buffer(buff, BUFF_LEN);
    }
  }
  if (Sensor1.available() > 0) 
  {
    uint8_t c = Sensor1.read();
    //Serial.println(c);
    buff[i] = c;
    i++;
    sensor_new_data = 1;
    timer = millis();
  }
}

unsigned char checksum(unsigned char *i, unsigned char ln) {
  unsigned char j, tempq = 0;
  i += 1;
  for (j = 0; j < (ln - 2); j++) {
    tempq += *i;
    i++;
  }
  tempq = (~tempq) + 1;
  return (tempq);
}

void sensor_ozone_alarm_manager()
{
  if (millis() - o3_sensor_alarm.millis1_cur > 100) 
  {
    o3_sensor_alarm.millis1_cur = millis();
    o3_sensor_alarm.readings_sum += analogRead(S1_010V);
    o3_sensor_alarm.readings_counter += 1;
  }
  if (millis() - o3_sensor_alarm.millis2_cur > 1000) 
  {
    o3_sensor_alarm.millis2_cur = millis();
    uint32_t result = o3_sensor_alarm.readings_sum / o3_sensor_alarm.readings_counter;
    // TODO: check
    uint16_t ppb = map(result, 0, 255, 0, 10000);
    o3_sensor_alarm.ppb_cur = ppb;
    // Serial.print("PPB: ");
    // Serial.println(ppb);
    o3_sensor_alarm.readings_sum = 0;
    o3_sensor_alarm.readings_counter = 0;
  }

  // manage alarm
  if (o3_sensor_alarm.ppb_cur >= o3_sensor_alarm.ppb_alarm_cur)
  {
    o3_sensor_alarm.is_over_max_cur = 1;
  }
  else
  {
    o3_sensor_alarm.is_over_max_cur = 0;
  }
  if (o3_sensor_alarm.is_over_max_cur == 0)
  {
    o3_sensor_alarm.alarm_millis_cur = millis();
  }
  // if (o3_sensor_alarm.is_over_max_old != o3_sensor_alarm.is_over_max_cur)
  // {
  //   o3_sensor_alarm.is_over_max_old = o3_sensor_alarm.is_over_max_cur;
  // }
  uint32_t alarm_timer_millis_cur = (uint32_t)o3_sensor_alarm.alarm_timer_minutes_cur * 60 * 1000;
  // uint32_t alarm_timer_millis_cur = 5000;
  if (millis() - o3_sensor_alarm.alarm_millis_cur >= alarm_timer_millis_cur) 
  {
    // Serial.println("ALARM!!!");
    o3_sensor_alarm.is_alarm_cur = 1;
  }

  if (o3_sensor_alarm.is_alarm_old != o3_sensor_alarm.is_alarm_cur)
  {
    o3_sensor_alarm.is_alarm_old = o3_sensor_alarm.is_alarm_cur;
    if (o3_sensor_alarm.is_alarm_cur == 1)
    {
      nextion.page_cur = 80;
    }
  }
}