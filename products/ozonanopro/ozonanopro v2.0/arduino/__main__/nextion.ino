uint8_t cmd_p_home_onoff[BUFFER_SIZE] = { 101, 1, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_vi[BUFFER_SIZE] = { 101, 1, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_vo[BUFFER_SIZE] = { 101, 1, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_vb[BUFFER_SIZE] = { 101, 1, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_pb[BUFFER_SIZE] = { 101, 1, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_pn[BUFFER_SIZE] = { 101, 1, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_m[BUFFER_SIZE] = { 101, 1, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_p[BUFFER_SIZE] = { 101, 1, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

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
  if (nextion_array_compare(cmd_p_home_onoff, nextion.inputs_buff))
  {
    if (cycle.state_onoff_cur == 0) cycle.state_onoff_cur = 1;
    else cycle.state_onoff_cur = 0;
  }
  // manual mode
  if (cycle.mode_cur == 0)
  {
    if (nextion_array_compare(cmd_p_home_vi, nextion.inputs_buff))
    {
      if (cycle.state_onoff_cur == 1)
      {
        cycle.state_vi_cur = !cycle.state_vi_cur;
      }
    }
    if (nextion_array_compare(cmd_p_home_vo, nextion.inputs_buff))
    {
      if (cycle.state_onoff_cur == 1)
      {
        cycle.state_vo_cur = !cycle.state_vo_cur;
      }
    }
    if (nextion_array_compare(cmd_p_home_vb, nextion.inputs_buff))
    {
      if (cycle.state_onoff_cur == 1)
      {
        cycle.state_vb_cur = !cycle.state_vb_cur;
      }
    }
    if (nextion_array_compare(cmd_p_home_pb, nextion.inputs_buff))
    {
      if (cycle.state_onoff_cur == 1)
      {
        cycle.state_pb_cur = !cycle.state_pb_cur;
      }
    }
    if (nextion_array_compare(cmd_p_home_pn, nextion.inputs_buff))
    {
      if (cycle.state_onoff_cur == 1)
      {
        cycle.state_pn_cur = !cycle.state_pn_cur;
      }
    }
  }
  if (nextion_array_compare(cmd_p_home_m, nextion.inputs_buff))
  {
    cycle.mode_cur = 0;
    cycle.state_onoff_cur = 0;
  }
  if (nextion_array_compare(cmd_p_home_p, nextion.inputs_buff))
  {
    cycle.mode_cur = 1;
    cycle.state_onoff_cur = 0;
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
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x68, 0x6F, 0x6D, 0x65, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
    cycle.state_onoff_old = -2;
    cycle.state_vi_old = -2;
    cycle.state_vo_old = -2;
    cycle.state_vb_old = -2;
    cycle.state_pb_old = -2;
    cycle.state_pn_old = -2;
  }
  // onoff
  if (force_refresh || cycle.state_onoff_old != cycle.state_onoff_cur) 
  {
    cycle.state_onoff_old = cycle.state_onoff_cur;
    {
      if (cycle.state_onoff_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // vi
  if (force_refresh || cycle.state_vi_old != cycle.state_vi_cur) 
  {
    cycle.state_vi_old = cycle.state_vi_cur;
    {
      if (cycle.state_vi_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x35, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // vo
  if (force_refresh || cycle.state_vo_old != cycle.state_vo_cur) 
  {
    cycle.state_vo_old = cycle.state_vo_cur;
    {
      if (cycle.state_vo_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x37, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x32, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x36, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // vb
  if (force_refresh || cycle.state_vb_old != cycle.state_vb_cur) 
  {
    cycle.state_vb_old = cycle.state_vb_cur;
    {
      if (cycle.state_vb_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x39, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x33, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x38, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // pb
  if (force_refresh || cycle.state_pb_old != cycle.state_pb_cur) 
  {
    cycle.state_pb_old = cycle.state_pb_cur;
    {
      if (cycle.state_pb_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x34, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x30, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // pn
  if (force_refresh || cycle.state_pn_old != cycle.state_pn_cur) 
  {
    cycle.state_pn_old = cycle.state_pn_cur;
    {
      if (cycle.state_pn_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x33, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x35, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // m
  if (force_refresh || cycle.mode_old != cycle.mode_cur) 
  {
    cycle.mode_old = cycle.mode_cur;
    {
      if (cycle.mode_cur == 0)
      {
        {
          uint8_t _buffer[] = { 0x70, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x35, 0xff, 0xff, 0xff };
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        }
        {
          uint8_t _buffer[] = { 0x70, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x36, 0xff, 0xff, 0xff };
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        }
      }
      else
      {
        {
          uint8_t _buffer[] = { 0x70, 0x36, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x34, 0xff, 0xff, 0xff };
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        }
        {
          uint8_t _buffer[] = { 0x70, 0x37, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x37, 0xff, 0xff, 0xff };
          for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
          {
            Serial2.write(_buffer[i]);
          }
        }
      }
    }
  }
  
  if (force_refresh || pressure_switch.nextion_refresh == 1) 
  {
    pressure_switch.nextion_refresh = 0;
    if (pressure_switch.state_cur == 1)
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x31, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
    else
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
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