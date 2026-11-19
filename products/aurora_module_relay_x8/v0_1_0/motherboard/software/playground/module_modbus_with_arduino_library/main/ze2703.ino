unsigned char FucCheckSum(unsigned char *i, unsigned char ln)
{
  unsigned char j, tempq = 0;
  i += 1;
  for (j = 0; j < (ln - 2); j++)
  {
    tempq += *i;
    i++;
  }
  tempq = (~tempq) + 1; return (tempq);
}

int16_t ze27o3_ppb_get() 
{
  int16_t ppb = sensor.buff[4] * 256 + sensor.buff[5];
  return ppb;
}

void ze27o3_listen()
{
  if (Serial2.available() > 0)
  {
    uint8_t c = Serial2.read();
    sensor.buff[sensor.buff_i] = c;
    sensor.buff_i += 1;
    sensor.buff_ready = 1;
    sensor.buff_timer = millis();
  }
}

int8_t ze27o3_ready()
{
  if (sensor.buff_ready && millis() - sensor.buff_timer > 40)
  {
    return 1;
  }
  return 0;
}

void ze27o3_debug()
{
    int16_t ppb = ze27o3_ppb_get();
    Serial.print("PPB: ");
    Serial.println(ppb);

    Serial.print("BUFF: ");
    for(int i = 0; i < SENSOR_BUFF_LEN; i++)
    {
      Serial.print(sensor.buff[i]);
      Serial.print(", ");
    }
    Serial.println();
    Serial.println();
}

uint8_t ze27o3_checksum_valid() 
{
  if (FucCheckSum(sensor.buff, SENSOR_BUFF_LEN) == sensor.buff[SENSOR_BUFF_LEN-1]) 
  {
    return 1;
  }
  return 0;
}
