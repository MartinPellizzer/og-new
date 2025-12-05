
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


uint8_t power_id = 0x30;
uint8_t flow_switch_id = 0x31;
uint8_t valve_bypass_id = 0x32;
uint8_t oxygen_sensor_id = 0x34;
uint8_t pump_booster_id = 0x35;
uint8_t pump_nano_id = 0x36;
uint8_t oxygen_concentrator_id = 0x37;
uint8_t ozone_generator_id = 0x38;

void nextion_update_page_home_power_on() 
{
  uint8_t _buffer_color[] = { 0x74, power_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, power_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_power_off() 
{
  uint8_t _buffer_color[] = { 0x74, power_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, power_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_pump_booster_on() 
{
  uint8_t _buffer_color[] = { 0x74, pump_booster_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, pump_booster_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_pump_booster_off() 
{
  uint8_t _buffer_color[] = { 0x74, pump_booster_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, pump_booster_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_pump_nano_on() 
{
  uint8_t _buffer_color[] = { 0x74, pump_nano_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, pump_nano_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_pump_nano_off() 
{
  uint8_t _buffer_color[] = { 0x74, pump_nano_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, pump_nano_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_flow_switch_on() 
{
  uint8_t _buffer_color[] = { 0x74, flow_switch_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, flow_switch_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}
void nextion_update_page_home_flow_switch_off() 
{
  uint8_t _buffer_color[] = { 0x74, flow_switch_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, flow_switch_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_valve_bypass_on() 
{
  uint8_t _buffer_color[] = { 0x74, valve_bypass_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, valve_bypass_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}
void nextion_update_page_home_valve_bypass_off() 
{
  uint8_t _buffer_color[] = { 0x74, valve_bypass_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, valve_bypass_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_oxygen_concentrator_on() 
{
  uint8_t _buffer_color[] = { 0x74, oxygen_concentrator_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, oxygen_concentrator_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}
void nextion_update_page_home_oxygen_concentrator_off() 
{
  uint8_t _buffer_color[] = { 0x74, oxygen_concentrator_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, oxygen_concentrator_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

void nextion_update_page_home_ozone_generator_on() 
{
  uint8_t _buffer_color[] = { 0x74, ozone_generator_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x33, 0x38, 0x35, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, ozone_generator_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}
void nextion_update_page_home_ozone_generator_off() 
{
  uint8_t _buffer_color[] = { 0x74, ozone_generator_id, 0x2E, 0x70, 0x63, 0x6F, 0x3D, 0x35, 0x35, 0x35, 0x38, 0x38, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_color) / sizeof(uint8_t); i++) { Serial2.write(_buffer_color[i]); }
  uint8_t _buffer_value[] = { 0x74, ozone_generator_id, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4F, 0x46, 0x46, 0x22, 0xff, 0xff, 0xff };
  for (uint8_t i = 0; i < sizeof(_buffer_value) / sizeof(uint8_t); i++) { Serial2.write(_buffer_value[i]); }
}

////////////////////////////////////////////////////////
// ;home
////////////////////////////////////////////////////////
void nextion_update_page_home(uint8_t force_refresh) 
{
  if (force_refresh) 
  {
  }
  
  if (force_refresh || power.nextion_refresh == 1) 
  {
    power.nextion_refresh = 0;
    if (power.state_cur == 1) { nextion_update_page_home_power_on(); }
  //   else { nextion_update_page_home_power_off(); }
  }

  // if (force_refresh || pump_booster.state_old != pump_booster.state_cur) 
  // {
  //   pump_booster.state_old = pump_booster.state_cur;
  //   if (pump_booster.state_cur == 1) { nextion_update_page_home_pump_booster_on(); }
  //   else { nextion_update_page_home_pump_booster_off(); }
  // }

  // if (force_refresh || pump_nano.state_old != pump_nano.state_cur) 
  // {
  //   pump_nano.state_old = pump_nano.state_cur;
  //   if (pump_nano.state_cur == 1) { nextion_update_page_home_pump_nano_on(); }
  //   else { nextion_update_page_home_pump_nano_off(); }
  // }

  // if (force_refresh || flow_switch.nextion_refresh == 1) 
  // {
  //   flow_switch.nextion_refresh = 0;
  //   if (flow_switch.state_cur == 0) { nextion_update_page_home_flow_switch_on(); }
  //   else { nextion_update_page_home_flow_switch_off(); }
  // }

  // if (force_refresh || valve_bypass.nextion_refresh == 1) 
  // {
  //   valve_bypass.nextion_refresh = 0;
  //   if (valve_bypass.state_cur == 1) { nextion_update_page_home_valve_bypass_on(); }
  //   else { nextion_update_page_home_valve_bypass_off(); }
  // }

  // if (force_refresh || oxygen_concentrator.nextion_refresh == 1) 
  // {
  //   oxygen_concentrator.nextion_refresh = 0;
  //   if (oxygen_concentrator.state_cur == 1) { nextion_update_page_home_oxygen_concentrator_on(); }
  //   else { nextion_update_page_home_oxygen_concentrator_off(); }
  // }

  // if (force_refresh || ozone_generator.nextion_refresh == 1) 
  // {
  //   ozone_generator.nextion_refresh = 0;
  //   if (ozone_generator.state_cur == 1) { nextion_update_page_home_ozone_generator_on(); }
  //   else { nextion_update_page_home_ozone_generator_off(); }
  // }
}
