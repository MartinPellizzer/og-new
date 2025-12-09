

void vi_on()
{
  if (cycle.state_vi_ncno_cur == 0) cycle.state_vi_cur = 1;
  else cycle.state_vi_cur = 0;
  digitalWrite(RO_VI, cycle.state_vi_cur);
}

void vi_off()
{
  if (cycle.state_vi_ncno_cur == 0) cycle.state_vi_cur = 0;
  else cycle.state_vi_cur = 1;
  digitalWrite(RO_VI, cycle.state_vi_cur);
}

void vo_on()
{
  if (cycle.state_vo_ncno_cur == 0) cycle.state_vo_cur = 1;
  else cycle.state_vo_cur = 0;
  digitalWrite(RO_VO, cycle.state_vo_cur);
}

void vo_off()
{
  if (cycle.state_vo_ncno_cur == 0) cycle.state_vo_cur = 0;
  else cycle.state_vo_cur = 1;
  digitalWrite(RO_VO, cycle.state_vo_cur);
}

void vb_on()
{
  if (cycle.state_vb_ncno_cur == 0) cycle.state_vb_cur = 1;
  else cycle.state_vb_cur = 0;
  digitalWrite(RO_VB, cycle.state_vb_cur);
}

void vb_off()
{
  if (cycle.state_vb_ncno_cur == 0) cycle.state_vb_cur = 0;
  else cycle.state_vb_cur = 1;
  digitalWrite(RO_VB, cycle.state_vb_cur);
}

void pb_on()
{
  if (cycle.state_pb_ncno_cur == 0) cycle.state_pb_cur = 1;
  else cycle.state_pb_cur = 0;
  digitalWrite(RO_PB, cycle.state_pb_cur);
}

void pb_off()
{
  if (cycle.state_pb_ncno_cur == 0) cycle.state_pb_cur = 0;
  else cycle.state_pb_cur = 1;
  digitalWrite(RO_PB, cycle.state_pb_cur);
}

void pn_on()
{
  if (cycle.state_pn_ncno_cur == 0) cycle.state_pn_cur = 1;
  else cycle.state_pn_cur = 0;
  digitalWrite(RO_PN, cycle.state_pn_cur);
}

void pn_off()
{
  if (cycle.state_pn_ncno_cur == 0) cycle.state_pn_cur = 0;
  else cycle.state_pn_cur = 1;
  digitalWrite(RO_PN, cycle.state_pn_cur);
}

void cycle_mode_pressostato()
{
  if (cycle.state_cur == 0)
  {  
    // pressure down
    if (cycle.pressure_switch_state_cur == 0)
    {
      vi_on();
      vo_on();
      vb_off();
      pb_on();
      pn_on();
    }
    // pressure up
    else
    {
      vi_off();
      vo_off();
      vb_on();
      pb_on();
      pn_on();
      
      cycle.bypass_millis_cur = millis();
      cycle.state_cur = 1;
    }
  }
  else if (cycle.state_cur == 1)
  {
    // pressure down
    if (cycle.pressure_switch_state_cur == 0)
    {
      vi_on();
      vo_on();
      vb_off();
      pb_on();
      pn_on();
      
      cycle.state_cur = 0;
    }
    // pressure up
    else
    {
      vi_off();
      vo_off();
      vb_on();
      pb_on();
      pn_on();
      
      if (millis() - cycle.bypass_millis_cur > cycle.bypass_timer_cur) 
      {
        cycle.state_cur = 2;
      }
    }
  }
  else if (cycle.state_cur == 2)
  {
    // pressure down
    if (cycle.pressure_switch_state_cur == 0)
    {
        cycle.state_cur = 0;
    }
    // pressure up
    else
    {
      vi_on();
      vo_on();
      vb_off();
      pb_off();
      pn_off();
    }
  }
  else
  {
    Serial.println("INVALID STATE");
  }
}

void cycle_mode_manual()
{
  digitalWrite(RO_VI, cycle.state_vi_cur);
  digitalWrite(RO_VO, cycle.state_vo_cur);
  digitalWrite(RO_VB, cycle.state_vb_cur);
  digitalWrite(RO_PB, cycle.state_pb_cur);
  digitalWrite(RO_PN, cycle.state_pn_cur);
}

void cycle_off()
{
      vi_off();
      vo_off();
      vb_off();
      pb_off();
      pn_off();
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