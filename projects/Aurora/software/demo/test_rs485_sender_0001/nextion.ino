uint8_t cmd_p_home_1[BUFFER_SIZE] = { 101, 0, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_2[BUFFER_SIZE] = { 101, 0, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_3[BUFFER_SIZE] = { 101, 0, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_4[BUFFER_SIZE] = { 101, 0, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_5[BUFFER_SIZE] = { 101, 0, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_6[BUFFER_SIZE] = { 101, 0, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

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
    Serial2.println("here");
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
  if (nextion_array_compare(cmd_p_home_1, nextion.inputs_buff))
  {
    buildModbusWriteCoil(0x01);
  }
  if (nextion_array_compare(cmd_p_home_2, nextion.inputs_buff))
  {
    buildModbusWriteCoil(0x02);
  }
  if (nextion_array_compare(cmd_p_home_3, nextion.inputs_buff))
  {
    buildModbusWriteCoil(0x03);
  }
  if (nextion_array_compare(cmd_p_home_4, nextion.inputs_buff))
  {
    buildModbusWriteCoil(0x04);
  }
  if (nextion_array_compare(cmd_p_home_5, nextion.inputs_buff))
  {
    buildModbusWriteCoil(0x05);
  }
  if (nextion_array_compare(cmd_p_home_6, nextion.inputs_buff))
  {
    buildModbusWriteCoil(0x06);
  }
}

void nextion_eval_serial() 
{
  /**/ if (nextion.page_cur == P_HOME)              nextion_input_p_home();
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
}

void nextion_update_page_home(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    // {
    //   uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x68, 0x6F, 0x6D, 0x65, 0xff, 0xff, 0xff };
    //   for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    //   {
    //     Serial2.write(_buffer[i]);
    //   }
    // }
  }
  
  if (force_refresh || module.online_old != module.online_cur) 
  {
    module.online_old = module.online_cur;
    // if (module.online_cur == 0)
    // {
    //   uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x30, 0xff, 0xff, 0xff };
    //   for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    //   {
    //     Serial2.write(_buffer[i]);
    //   }
    // }
    // else
    {
      Serial.println("11111");
      uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0xff, 0xff, 0xff };
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