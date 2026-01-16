uint8_t cmd_p_home_onoff[BUFFER_SIZE] = { 101, 1, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_vi[BUFFER_SIZE] = { 101, 1, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_vo[BUFFER_SIZE] = { 101, 1, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_vb[BUFFER_SIZE] = { 101, 1, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_pb[BUFFER_SIZE] = { 101, 1, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_pn[BUFFER_SIZE] = { 101, 1, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_m[BUFFER_SIZE] = { 101, 1, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_p[BUFFER_SIZE] = { 101, 1, 9, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_settings[BUFFER_SIZE] = { 101, 1, 10, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_o2[BUFFER_SIZE] = { 101, 1, 11, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_o3[BUFFER_SIZE] = { 101, 1, 12, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_home_so[BUFFER_SIZE] = { 101, 1, 13, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

uint8_t cmd_p_settings_save[BUFFER_SIZE] = { 101, 2, 1, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_settings_back[BUFFER_SIZE] = { 101, 2, 2, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_settings_vi_left[BUFFER_SIZE] = { 101, 2, 3, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_settings_vi_right[BUFFER_SIZE] = { 101, 2, 4, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_settings_vo_left[BUFFER_SIZE] = { 101, 2, 5, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_settings_vo_right[BUFFER_SIZE] = { 101, 2, 6, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_settings_vb_left[BUFFER_SIZE] = { 101, 2, 7, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
uint8_t cmd_p_settings_vb_right[BUFFER_SIZE] = { 101, 2, 8, 1, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

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
    if (cycle.state_onoff_cur == 0) 
    {
      cycle.state_onoff_cur = 1;
      cycle.state_cur = 0;
      cycle.ozone_millis_cur = millis();
    }
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
    if (nextion_array_compare(cmd_p_home_o2, nextion.inputs_buff))
    {
      if (cycle.state_onoff_cur == 1)
      {
        cycle.state_o2_cur = !cycle.state_o2_cur;
      }
    }
    if (nextion_array_compare(cmd_p_home_o3, nextion.inputs_buff))
    {
      if (cycle.state_onoff_cur == 1)
      {
        cycle.state_o3_cur = !cycle.state_o3_cur;
      }
    }
    if (nextion_array_compare(cmd_p_home_so, nextion.inputs_buff))
    {
      if (cycle.state_onoff_cur == 1)
      {
        cycle.state_so_cur = !cycle.state_so_cur;
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
  if (nextion_array_compare(cmd_p_home_settings, nextion.inputs_buff))
  {
    nextion.page_cur = P_SETTINGS;
    cycle.state_onoff_cur = 0;
  }
}

void nextion_input_p_settings()
{
  if (nextion_array_compare(cmd_p_settings_save, nextion.inputs_buff))
  {
    nextion.page_cur = P_HOME;
    cycle.state_vi_ncno_cur = cycle.state_vi_ncno_tmp;
    cycle.state_vo_ncno_cur = cycle.state_vo_ncno_tmp;
    cycle.state_vb_ncno_cur = cycle.state_vb_ncno_tmp;
  }
  if (nextion_array_compare(cmd_p_settings_back, nextion.inputs_buff))
  {
    nextion.page_cur = P_HOME;
  }
  if (nextion_array_compare(cmd_p_settings_vi_left, nextion.inputs_buff))
  {
    cycle.state_vi_ncno_tmp = !cycle.state_vi_ncno_tmp;
  }
  if (nextion_array_compare(cmd_p_settings_vi_right, nextion.inputs_buff))
  {
    cycle.state_vi_ncno_tmp = !cycle.state_vi_ncno_tmp;
  }
  if (nextion_array_compare(cmd_p_settings_vo_left, nextion.inputs_buff))
  {
    cycle.state_vo_ncno_tmp = !cycle.state_vo_ncno_tmp;
  }
  if (nextion_array_compare(cmd_p_settings_vo_right, nextion.inputs_buff))
  {
    cycle.state_vo_ncno_tmp = !cycle.state_vo_ncno_tmp;
  }
  if (nextion_array_compare(cmd_p_settings_vb_left, nextion.inputs_buff))
  {
    cycle.state_vb_ncno_tmp = !cycle.state_vb_ncno_tmp;
  }
  if (nextion_array_compare(cmd_p_settings_vb_right, nextion.inputs_buff))
  {
    cycle.state_vb_ncno_tmp = !cycle.state_vb_ncno_tmp;
  }
}

void nextion_eval_serial()
{
  /**/ if (nextion.page_cur == P_HOME)                  nextion_input_p_home();
  else if (nextion.page_cur == P_SETTINGS)              nextion_input_p_settings();
}

void nextion_update()
{
  uint8_t force_refresh = 0;
  if (nextion.page_old != nextion.page_cur) 
  {
    nextion.page_old = nextion.page_cur;
    force_refresh = 1;
  }
  /**/ if (nextion.page_cur == P_HOME)                  nextion_update_page_home(force_refresh);
  else if (nextion.page_cur == P_SETTINGS)              nextion_update_page_settings(force_refresh);
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
    if (cycle.state_vi_ncno_cur == 0)
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
    else
    {
      if (cycle.state_vi_cur == 0)
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
    if (cycle.state_vi_ncno_cur == 0)
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
    else
    {
      if (cycle.state_vo_cur == 0)
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
    if (cycle.state_vb_ncno_cur == 0)
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
    else
    {
      if (cycle.state_vb_cur == 0)
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
  // o2
  if (force_refresh || cycle.state_o2_old != cycle.state_o2_cur) 
  {
    cycle.state_o2_old = cycle.state_o2_cur;
    {
      if (cycle.state_o2_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x30, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x38, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x31, 0x39, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // o3
  if (force_refresh || cycle.state_o3_old != cycle.state_o3_cur) 
  {
    cycle.state_o3_old = cycle.state_o3_cur;
    {
      if (cycle.state_o3_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x32, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x39, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x31, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  // so
  if (force_refresh || cycle.state_so_old != cycle.state_so_cur) 
  {
    cycle.state_so_old = cycle.state_so_cur;
    {
      if (cycle.state_so_cur == 1)
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x34, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x70, 0x31, 0x30, 0x2E, 0x70, 0x69, 0x63, 0x3D, 0x32, 0x33, 0xff, 0xff, 0xff };
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

void nextion_update_page_settings(uint8_t force_refresh)
{
  if (force_refresh) 
  {
    uint8_t _buffer[] = { 0x70, 0x61, 0x67, 0x65, 0x20, 0x70, 0x5F, 0x73, 0x65, 0x74, 0x5F, 0x6C, 0x69, 0x73, 0x74, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
    cycle.state_vi_ncno_tmp = cycle.state_vi_ncno_cur;
    cycle.state_vi_ncno_old = -2;
    cycle.state_vo_ncno_tmp = cycle.state_vo_ncno_cur;
    cycle.state_vo_ncno_old = -2;
    cycle.state_vb_ncno_tmp = cycle.state_vb_ncno_cur;
    cycle.state_vb_ncno_old = -2;
  }
  if (force_refresh || cycle.state_vi_ncno_old != cycle.state_vi_ncno_tmp) 
  {
    cycle.state_vi_ncno_old = cycle.state_vi_ncno_tmp;
    {
      if (cycle.state_vi_ncno_tmp == 0)
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x43, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  if (force_refresh || cycle.state_vo_ncno_old != cycle.state_vo_ncno_tmp) 
  {
    cycle.state_vo_ncno_old = cycle.state_vo_ncno_tmp;
    {
      if (cycle.state_vo_ncno_tmp == 0)
      {
        uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x43, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x74, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
  if (force_refresh || cycle.state_vb_ncno_old != cycle.state_vb_ncno_tmp) 
  {
    cycle.state_vb_ncno_old = cycle.state_vb_ncno_tmp;
    {
      if (cycle.state_vb_ncno_tmp == 0)
      {
        uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x43, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      else
      {
        uint8_t _buffer[] = { 0x74, 0x32, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4E, 0x4F, 0x22, 0xff, 0xff, 0xff };
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
}

void nextion_manager()
{
  nextion_inputs();
  nextion_update();
}
