 unsigned char sensor_checksum(unsigned char *i, unsigned char ln) 
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

  if (sensor.new_data) 
  {
    if (millis() - sensor.timer > 40) 
    {
      sensor.timer = millis();
      sensor.buff_index = 0;
      sensor.new_data = 0;
      sensor.ppb_curr = 0;
      if (sensor_checksum(sensor.buff, 9) == sensor.buff[8]) 
      {
        sensor.ppb_curr = sensor.buff[4] * 256 + sensor.buff[5];
        sensor.connected_millis = millis();
        sensor.connected_seconds = 0;
        sensor.connected_curr = 1;
      }
      clear_buffer(sensor.buff, BUFF_LEN);
    }
  }
  if (Sensor1.available() > 0) 
  {
    uint8_t c = Sensor1.read();
    sensor.buff[sensor.buff_index] = c;
    sensor.buff_index++;
    sensor.new_data = 1;
    sensor.timer = millis();
  }
}