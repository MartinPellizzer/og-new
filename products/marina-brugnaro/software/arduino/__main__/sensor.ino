 unsigned char checksum(unsigned char *i, unsigned char ln) 
 {
  unsigned char j, tempq = 0;
  i += 1;
  for (j = 0; j < (ln - 2); j++) 
  {
    tempq += *i;
    i++;
  }
  tempq = (~tempq) + 1;
  return (tempq);
}

void sensor_input() 
{
  if (sensor.connected_curr == 1) 
  {
    if (millis() - sensor.connected_millis > 1000) 
    {
      sensor.connected_millis = millis();
      sensor.connected_seconds += 1;
      if (sensor.connected_seconds > 5) 
      {
        sensor.connected_curr = 0;
        sensor.ppb_curr = -1;
        sensor.ppb_prev = 0;
      }
    }
  }

  if (sensor_new_data) 
  {
    if (millis() - timer > 40) 
    {
      timer_no_signal = millis();
      i = 0;
      sensor_new_data = 0;
      sensor.ppb_curr = 0;
      if (checksum(buff, 9) == buff[8]) 
      {
        sensor.ppb_curr = buff[4] * 256 + buff[5];
        sensor.connected_millis = millis();
        sensor.connected_seconds = 0;
        sensor.connected_curr = 1;
      }
      clear_buffer(buff, BUFF_LEN);
    }
  }
  if (Sensor1.available() > 0) 
  {
    uint8_t c = Sensor1.read();
    buff[i] = c;
    i++;
    sensor_new_data = 1;
    timer = millis();
  }
}