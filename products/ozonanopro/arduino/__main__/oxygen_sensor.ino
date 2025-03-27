// TODO
// unsigned char checksum(unsigned char *i, unsigned char ln) {
//   unsigned char j, tempq = 0;
//   i += 1;
//   for (j = 0; j < (ln - 2); j++) {
//     tempq += *i;
//     i++;
//   }
//   tempq = (~tempq) + 1;
//   return (tempq);
// }

void clear_buffer(uint8_t buff[], uint8_t len) 
{
  for (int i = 0; i < len; i++) buff[i] = 0;
}

void oxygen_sensor_input()
{
  if (oxygen_sensor_serial.available() > 0) 
  {
    if (oxygen_sensor.receiver_buff_index < OXYGEN_SENSOR_BUFF_LEN)
    {
      uint8_t c = oxygen_sensor_serial.read();
      oxygen_sensor.receiver_buff[oxygen_sensor.receiver_buff_index] = c;
      oxygen_sensor.receiver_buff_index++;
      oxygen_sensor.bytestream_receiving = 1;
      oxygen_sensor.receiver_timer = millis();
    }
  }
  
  if (oxygen_sensor.bytestream_receiving) 
  {
    if (millis() - oxygen_sensor.receiver_timer > 40) 
    {
      oxygen_sensor.receiver_timer_no_signal = millis();
      oxygen_sensor.receiver_buff_index = 0;
      oxygen_sensor.bytestream_receiving = 0;
      oxygen_sensor.concentration_cur = 0;
      oxygen_sensor.bytestream_received = 1;
    }
  }
} 

void oxygen_sensor_check_connection() 
{
  if (oxygen_sensor.is_connected == 1) 
  {
    if (millis() - oxygen_sensor.connected_millis > 1000) 
    {
      oxygen_sensor.connected_millis = millis();
      oxygen_sensor.connected_seconds += 1;
      if (oxygen_sensor.connected_seconds > 5)
      {
        oxygen_sensor.is_connected = 0;
        oxygen_sensor.concentration_old = -2;
        oxygen_sensor.concentration_cur = -1;
        oxygen_sensor.flow_old = -2;
        oxygen_sensor.flow_cur = -1;
        oxygen_sensor.temperature_old = -2;
        oxygen_sensor.temperature_cur = -1;
      }
    }
  }
}

float oxygen_sensor_calc_concentration()
{
  float res = float(oxygen_sensor.receiver_buff[3]*256+oxygen_sensor.receiver_buff[4])/10;
  return res;
}

float oxygen_sensor_calc_flow()
{
  float res = float(oxygen_sensor.receiver_buff[5]*256+oxygen_sensor.receiver_buff[6])/10;
  return res;
}

float oxygen_sensor_calc_temperature()
{
  float res = float(oxygen_sensor.receiver_buff[7]*256+oxygen_sensor.receiver_buff[8])/10;
  return res;
}

void oxygen_sensor_debug_concentration_raw(float val)
{
  Serial.print("concentration: ");
  Serial.print(val, 2);
  Serial.print(" Vol %");
  Serial.println();
}

void oxygen_sensor_debug_flow_raw(float val)
{
  Serial.print("flow: ");
  Serial.print(val, 2);
  Serial.print(" L/min");
  Serial.println();
}

void oxygen_sensor_debug_temperature_raw(float val)
{
  Serial.print("temperature: ");
  Serial.print(val, 2);
  Serial.print(" °C");
  Serial.println();
}

void oxygen_sensor_update() 
{
  if (oxygen_sensor.bytestream_received) 
  {
    oxygen_sensor.bytestream_received = 0;
    for(int k = 0; k < 12; k++)
    {
      Serial.print(oxygen_sensor.receiver_buff[k]);
      Serial.print(", ");
    }
    Serial.println();

    float concentration = oxygen_sensor_calc_concentration();
    oxygen_sensor_debug_concentration_raw(concentration);

    float flow = oxygen_sensor_calc_flow();
    oxygen_sensor_debug_flow_raw(flow);

    float temperature = oxygen_sensor_calc_temperature();
    oxygen_sensor_debug_temperature_raw(temperature);

    //if (checksum(oxygen_sensor.receiver_buff, 9) == oxygen_sensor.receiver_buff[8]) 
    {
      uint16_t concentration_x100 = concentration*100;
      oxygen_sensor.concentration_cur = concentration_x100;
      uint16_t flow_x100 = flow*100;
      oxygen_sensor.flow_cur = flow_x100;
      uint16_t temperature_x100 = temperature*100;
      oxygen_sensor.temperature_cur = temperature_x100;

      oxygen_sensor.connected_millis = millis();
      oxygen_sensor.connected_seconds = 0;
      oxygen_sensor.is_connected = 1;
      // Serial.println(oxygen_sensor.concentration_cur);
      // Serial.println(oxygen_sensor.flow_cur);
      // Serial.println(oxygen_sensor.temperature_cur);
    }
    clear_buffer(oxygen_sensor.receiver_buff, OXYGEN_SENSOR_BUFF_LEN);
  }
}

void oxygen_sensor_manager()
{
  oxygen_sensor_input();
  oxygen_sensor_update();
}

