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