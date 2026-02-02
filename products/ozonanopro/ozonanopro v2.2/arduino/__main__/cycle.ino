void vi_on()
{
  cycle.state_vi_cur = 1;
  digitalWrite(RO_VI, cycle.state_vi_cur);
}

void vi_off()
{
  cycle.state_vi_cur = 0;
  digitalWrite(RO_VI, cycle.state_vi_cur);
}

void vo_on()
{
  cycle.state_vo_cur = 1;
  digitalWrite(RO_VO, cycle.state_vo_cur);
}

void vo_off()
{
  cycle.state_vo_cur = 0;
  digitalWrite(RO_VO, cycle.state_vo_cur);
}

void vb_on()
{
  cycle.state_vb_cur = 1;
  digitalWrite(RO_VB, cycle.state_vb_cur);
}

void vb_off()
{
  cycle.state_vb_cur = 0;
  digitalWrite(RO_VB, cycle.state_vb_cur);
}

void pb_on()
{
  cycle.state_pb_cur = 1;
  digitalWrite(RO_PB, cycle.state_pb_cur);
}

void pb_off()
{
  cycle.state_pb_cur = 0;
  digitalWrite(RO_PB, cycle.state_pb_cur);
}

void pn_on()
{
  cycle.state_pn_cur = 1;
  digitalWrite(RO_PN, cycle.state_pn_cur);
}

void pn_off()
{
  cycle.state_pn_cur = 0;
  digitalWrite(RO_PN, cycle.state_pn_cur);
}

void o2_on()
{
  cycle.state_o2_cur = 1;
  digitalWrite(RO_O2, cycle.state_o2_cur);
}

void o2_off()
{
  cycle.state_o2_cur = 0;
  digitalWrite(RO_O2, cycle.state_o2_cur);
}

void o3_on()
{
  cycle.state_o3_cur = 1;
  digitalWrite(RO_O3, cycle.state_o3_cur);
}

void o3_off()
{
  cycle.state_o3_cur = 0;
  digitalWrite(RO_O3, cycle.state_o3_cur);
}

void so_on()
{
  cycle.state_so_cur = 1;
  digitalWrite(RO_SO, cycle.state_so_cur);
}

void so_off()
{
  cycle.state_so_cur = 0;
  digitalWrite(RO_SO, cycle.state_so_cur);
}

// cycle.state_cur: 0 -> splashing nanobubble water (before producing ozone)
// cycle.state_cur: 1 -> splashing nanobubble water with ozone
// cycle.state_cur: 2 -> nanobubble water bypass
// cycle.state_cur: 3 -> stop after bypass timeout

int pistol_pressed()
{
  if (cycle.pressure_switch_state_cur == 0) return 1;
  else return 0;
}

int pistol_released()
{
  if (cycle.pressure_switch_state_cur == 1) return 1;
  else return 0;
}

void output_water()
{
  vi_on();
  vo_on();
  vb_off();
  pb_on();
  pn_on();
  o2_off();
  o3_off();
  so_off();
}

void output_water_ozone()
{
  vi_on();
  vo_on();
  vb_off();
  pb_on();
  pn_on();
  o2_on();
  o3_on();
  so_on();
}

void bypass_water()
{
  vi_off();
  vo_off();
  vb_on();
  pb_on();
  pn_on();
  o2_off();
  o3_off();
  so_off();
}

void pause_water()
{
  vi_on();
  vo_on();
  vb_off();
  pb_off();
  pn_off();
  o2_off();
  o3_off();
  so_off();
}

int state_water()
{
  if (cycle.state_cur == 0) return 1;
  else return 0;
}

void cycle_mode_pressostato()
{
  // STARTING STATE
  if (state_water())
  {  
    if (pistol_pressed())
    {
      output_water();
      
      // PISTOL TRIGGER PRESSED FOR X SECONDS...
      if (millis() - cycle.ozone_millis_cur > cycle.ozone_timer_cur) 
      {
        // GOTO STATE: OUTPUT WATER + OZONE 
        cycle.state_cur = 1;
      }
    }
    else if (pistol_released())
    {
      bypass_water();
      
      // GOTO STATE: BYPASS
      cycle.bypass_millis_cur = millis();
      cycle.state_cur = 2;
    }
  }
  // STATE WATER + OZONE
  else if (cycle.state_cur == 1)
  {  
    if (pistol_pressed())
    {
      output_water_ozone();
    }
    else if (pistol_released())
    {
      bypass_water();
      
      // GOTO STATE: BYPASS
      cycle.bypass_millis_cur = millis();
      cycle.state_cur = 2;
    }
  }
  // STATE BYPASS
  else if (cycle.state_cur == 2) // nanobubble water bypass
  {
    if (pistol_pressed())
    {
      output_water();
      
      // GOTO STATE: STARTING STATE
      cycle.ozone_millis_cur = millis();
      cycle.state_cur = 0;
    }
    else if (pistol_released())
    {
      bypass_water();
      
      // PISTOL TRIGGER RELEASED FOR X SECONDS...
      if (millis() - cycle.bypass_millis_cur > cycle.bypass_timer_cur) 
      {
        // GOTO STATE: PAUSE
        cycle.state_cur = 3;
      }
    }
  }
  // STATE PAUSE
  else if (cycle.state_cur == 3)
  {
    if (pistol_pressed())
    {
      // GOTO STATE: STARTING STATE
        cycle.ozone_millis_cur = millis();
        cycle.state_cur = 0;
    }
    else if (pistol_released())
    {
      pause_water();
    }
  }
  // STATE INVALID
  else
  {
    Serial.println("INVALID STATE");
  }
  
  if (millis() - debug_millis_cur > 1000) 
  {
    debug_millis_cur = millis();
    Serial.print("state_cur: ");
    Serial.println(cycle.state_cur);
    // Serial.print("pressure_switch_state_cur: ");
    // Serial.println(cycle.pressure_switch_state_cur);
    // Serial.print("ozone_millis_cur: ");
    // Serial.println(cycle.ozone_millis_cur);
    // Serial.print("ozone_timer_cur: ");
    // Serial.println(cycle.ozone_timer_cur);
    // Serial.print("ozone_timeout: ");
    // Serial.println(millis() - cycle.ozone_millis_cur);
    // if (millis() - cycle.ozone_millis_cur > cycle.ozone_timer_cur) 
    // {
    //   Serial.println("here");
    // }
  }
}

void cycle_mode_manual()
{
  digitalWrite(RO_VI, cycle.state_vi_cur);
  digitalWrite(RO_VO, cycle.state_vo_cur);
  digitalWrite(RO_VB, cycle.state_vb_cur);
  digitalWrite(RO_PB, cycle.state_pb_cur);
  digitalWrite(RO_PN, cycle.state_pn_cur);
  digitalWrite(RO_O2, cycle.state_o2_cur);
  digitalWrite(RO_O3, cycle.state_o3_cur);
  digitalWrite(RO_SO, cycle.state_so_cur);
}

void cycle_off()
{
  vi_off();
  vo_off();
  vb_off();
  pb_off();
  pn_off();
  o2_off();
  o3_off();
  so_off();
}

void cycle_manager()
{
  if (cycle.state_onoff_cur == 1)
  {
    if (cycle.mode_cur == 0) cycle_mode_manual();
    else if (cycle.mode_cur == 1) cycle_mode_pressostato();
  }
  else
  {
    cycle_off();
  }
}