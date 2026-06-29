
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

void nextion_eval_serial() 
{
}

void nextion_update() 
{
  uint8_t force_refresh = 0;
  if (nextion.page_old != nextion.page_cur) 
  {
    nextion.page_old = nextion.page_cur;
    force_refresh = 1;
  }
  /**/ if (nextion.page_cur == P_HOME)                        nextion_update_page_home(force_refresh);
}

////////////////////////////////////////////////////////
// ;home
////////////////////////////////////////////////////////
void nextion_update_page_home(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x68, 0x6F, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }
}

void nextion_manager()
{
  nextion_inputs();
  nextion_update();
}