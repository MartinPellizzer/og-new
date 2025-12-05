uint8_t valve_input_id[] = {0x30};
uint8_t flow_switch_id[] = {0x31};
uint8_t pressure_switch_id[] = {0x31, 0x32};
uint8_t valve_bypass_1_id[] = {0x32};
uint8_t valve_bypass_2_id[] = {0x31, 0x33};
uint8_t pump_booster_id[] = {0x35};
uint8_t pump_nano_id[] = {0x36};
uint8_t oxygen_concentrator_id[] = {0x37};
uint8_t ozone_generator_id[] = {0x38};
uint8_t solenoid_id[] = {0x39};

void nextion_update_page_home_valve_input() 
{
  if (valve_input.state_cur == 1) 
  { 
    uint8_t _buffer_color[] = { 0x74, valve_input_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, valve_input_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
  else 
  {
    uint8_t _buffer_color[] = { 0x74, valve_input_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, valve_input_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
}

void nextion_update_page_home_valve_bypass_1() 
{
  if (valve_bypass_1.state_cur == 1) 
  { 
    uint8_t _buffer_color[] = { 0x74, valve_bypass_1_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, valve_bypass_1_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
  else 
  {
    uint8_t _buffer_color[] = { 0x74, valve_bypass_1_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, valve_bypass_1_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
}

void nextion_update_page_home_valve_bypass_2() 
{
  if (valve_bypass_2.state_cur == 1) 
  { 
    uint8_t _buffer_color[] = { 0x74, valve_bypass_2_id[0], valve_bypass_2_id[1], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, valve_bypass_2_id[0], valve_bypass_2_id[1], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
  else 
  {
    uint8_t _buffer_color[] = { 0x74, valve_bypass_2_id[0], valve_bypass_2_id[1], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, valve_bypass_2_id[0], valve_bypass_2_id[1], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
}

void nextion_update_page_home_solenoid() 
{
  if (solenoid.state_cur == 1) 
  { 
    uint8_t _buffer_color[] = { 0x74, solenoid_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, solenoid_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
  else 
  {
    uint8_t _buffer_color[] = { 0x74, solenoid_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, solenoid_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
}

void nextion_update_page_home_flow_switch(uint8_t force_refresh) 
{
  
  if (force_refresh || flow_switch.nextion_refresh == 1) 
  {
    flow_switch.nextion_refresh = 0;
    if (flow_switch.state_cur == 1) 
    { 
      uint8_t _buffer_color[] = { 0x74, flow_switch_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
      uint8_t _buffer_value[] = { 0x74, flow_switch_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
    }
    else 
    {
      uint8_t _buffer_color[] = { 0x74, flow_switch_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
      uint8_t _buffer_value[] = { 0x74, flow_switch_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
      for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
    }
  }
}

void nextion_update_page_home_pressure_switch() 
{
  if (pressure_switch.state_cur == 1) 
  { 
    uint8_t _buffer_color[] = { 0x74, pressure_switch_id[0], pressure_switch_id[1], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, pressure_switch_id[0], pressure_switch_id[1], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
  else 
  {
    uint8_t _buffer_color[] = { 0x74, pressure_switch_id[0], pressure_switch_id[1], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
    uint8_t _buffer_value[] = { 0x74, pressure_switch_id[0], pressure_switch_id[1], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
    for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
  }
}

void nextion_update_page_home_pump_booster_on() 
{
  uint8_t _buffer_color[] = { 0x74, pump_booster_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, pump_booster_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}
void nextion_update_page_home_pump_booster_off() 
{
  uint8_t _buffer_color[] = { 0x74, pump_booster_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, pump_booster_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_pump_nano_on() 
{
  uint8_t _buffer_color[] = { 0x74, pump_nano_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, pump_nano_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}
void nextion_update_page_home_pump_nano_off() 
{
  uint8_t _buffer_color[] = { 0x74, pump_nano_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, pump_nano_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_oxygen_concentrator_on() 
{
  uint8_t _buffer_color[] = { 0x74, oxygen_concentrator_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, oxygen_concentrator_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}
void nextion_update_page_home_oxygen_concentrator_off() 
{
  uint8_t _buffer_color[] = { 0x74, oxygen_concentrator_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, oxygen_concentrator_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_ozone_generator_on() 
{
  uint8_t _buffer_color[] = { 0x74, ozone_generator_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, ozone_generator_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}
void nextion_update_page_home_ozone_generator_off() 
{
  uint8_t _buffer_color[] = { 0x74, ozone_generator_id[0], 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, ozone_generator_id[0], 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
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
  }

  if (force_refresh || oxygen_sensor.concentration_old != oxygen_sensor.concentration_cur) 
  {
    oxygen_sensor.concentration_old = oxygen_sensor.concentration_cur;
    uint8_t _buffer[] = { 0x74, 0x34, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x32, 0x30, 0x2E, 0x35, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff };  
    _buffer[8] = (oxygen_sensor.concentration_cur % 10000 / 1000) + 0x30;
    _buffer[9] = (oxygen_sensor.concentration_cur % 1000 / 100) + 0x30;
    _buffer[11] = (oxygen_sensor.concentration_cur % 100 / 10) + 0x30;
    _buffer[12] = (oxygen_sensor.concentration_cur % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }

  if (force_refresh || oxygen_sensor.flow_old != oxygen_sensor.flow_cur) 
  {
    oxygen_sensor.flow_old = oxygen_sensor.flow_cur;
    uint8_t _buffer[] = { 0x74, 0x31, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x32, 0x30, 0x2E, 0x35, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff };  
    _buffer[9] = (oxygen_sensor.flow_cur % 10000 / 1000) + 0x30;
    _buffer[10] = (oxygen_sensor.flow_cur % 1000 / 100) + 0x30;
    _buffer[12] = (oxygen_sensor.flow_cur % 100 / 10) + 0x30;
    _buffer[13] = (oxygen_sensor.flow_cur % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }

  if (force_refresh || oxygen_sensor.temperature_old != oxygen_sensor.temperature_cur) 
  {
    oxygen_sensor.temperature_old = oxygen_sensor.temperature_cur;
    uint8_t _buffer[] = { 0x74, 0x31, 0x31, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x32, 0x30, 0x2E, 0x35, 0x30, 0x25, 0x22, 0xff, 0xff, 0xff };  
    _buffer[9] = (oxygen_sensor.temperature_cur % 10000 / 1000) + 0x30;
    _buffer[10] = (oxygen_sensor.temperature_cur % 1000 / 100) + 0x30;
    _buffer[12] = (oxygen_sensor.temperature_cur % 100 / 10) + 0x30;
    _buffer[13] = (oxygen_sensor.temperature_cur % 10 / 1) + 0x30;
    for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
    {
      Serial2.write(_buffer[i]);
    }
  }

  if (force_refresh || valve_input.nextion_refresh == 1) 
  {
    valve_input.nextion_refresh = 0;
    nextion_update_page_home_valve_input();
  }

  if (force_refresh || valve_bypass_1.nextion_refresh == 1) 
  {    
    valve_bypass_1.nextion_refresh = 0;
    nextion_update_page_home_valve_bypass_1();
  }

  if (force_refresh || valve_bypass_2.nextion_refresh == 1) 
  {
    valve_bypass_2.nextion_refresh = 0;
    nextion_update_page_home_valve_bypass_2();
  }

  nextion_update_page_home_flow_switch(force_refresh);

  if (force_refresh || pressure_switch.nextion_refresh == 1) 
  {
    pressure_switch.nextion_refresh = 0;
    nextion_update_page_home_pressure_switch();
  }

  if (force_refresh || pump_booster.nextion_refresh == 1) 
  {
    pump_booster.nextion_refresh = 0;
    if (pump_booster.state_cur == 1) { nextion_update_page_home_pump_booster_on(); }
    else { nextion_update_page_home_pump_booster_off(); }
  }

  if (force_refresh || pump_nano.nextion_refresh == 1) 
  {
    pump_nano.nextion_refresh = 0;
    if (pump_nano.state_cur == 1) { nextion_update_page_home_pump_nano_on(); }
    else { nextion_update_page_home_pump_nano_off(); }
  }

  if (force_refresh || oxygen_concentrator.nextion_refresh == 1) 
  {
    oxygen_concentrator.nextion_refresh = 0;
    if (oxygen_concentrator.state_cur == 1) { nextion_update_page_home_oxygen_concentrator_on(); }
    else { nextion_update_page_home_oxygen_concentrator_off(); }
  }
  
  if (force_refresh || ozone_generator.nextion_refresh == 1) 
  {
    ozone_generator.nextion_refresh = 0;
    if (ozone_generator.state_cur == 1) { nextion_update_page_home_ozone_generator_on(); }
    else { nextion_update_page_home_ozone_generator_off(); }
  }
  
  if (force_refresh || solenoid.nextion_refresh == 1) 
  {
    solenoid.nextion_refresh = 0;
    nextion_update_page_home_solenoid();
  }
}


void nextion_update() 
{
  uint8_t force_refresh = 0;
  if (nextion.page_old != nextion.page_cur) 
  {
    nextion.page_old = nextion.page_cur;
    force_refresh = 1;
  }
  if (nextion.page_cur == 1)  nextion_update_page_home(force_refresh);
}