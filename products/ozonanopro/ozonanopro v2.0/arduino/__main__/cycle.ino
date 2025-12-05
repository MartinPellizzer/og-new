void cycle_mode_pressostato()
{
  if (cycle.state_cur == 0)
  {  
    // pressure down
    if (cycle.pressure_switch_state_cur == 0)
    {
      cycle.state_vi_cur = 1;
      cycle.state_vo_cur = 1;
      cycle.state_vb_cur = 0;
      cycle.state_pb_cur = 1;
      cycle.state_pn_cur = 1;
      digitalWrite(RO_VI, cycle.state_vi_cur);
      digitalWrite(RO_VO, cycle.state_vo_cur);
      digitalWrite(RO_VB, cycle.state_vb_cur);
      digitalWrite(RO_PB, cycle.state_pb_cur);
      digitalWrite(RO_PN, cycle.state_pn_cur);
    }
    // pressure up
    else
    {
      cycle.state_vi_cur = 0;
      cycle.state_vo_cur = 0;
      cycle.state_vb_cur = 1;
      cycle.state_pb_cur = 1;
      cycle.state_pn_cur = 1;
      digitalWrite(RO_VI, cycle.state_vi_cur);
      digitalWrite(RO_VO, cycle.state_vo_cur);
      digitalWrite(RO_VB, cycle.state_vb_cur);
      digitalWrite(RO_PB, cycle.state_pb_cur);
      digitalWrite(RO_PN, cycle.state_pn_cur);
      
      cycle.bypass_millis_cur = millis();
      cycle.state_cur = 1;
    }
  }
  else if (cycle.state_cur == 1)
  {
    // pressure down
    if (cycle.pressure_switch_state_cur == 0)
    {
      cycle.state_vi_cur = 1;
      cycle.state_vo_cur = 1;
      cycle.state_vb_cur = 0;
      cycle.state_pb_cur = 1;
      cycle.state_pn_cur = 1;
      digitalWrite(RO_VI, cycle.state_vi_cur);
      digitalWrite(RO_VO, cycle.state_vo_cur);
      digitalWrite(RO_VB, cycle.state_vb_cur);
      digitalWrite(RO_PB, cycle.state_pb_cur);
      digitalWrite(RO_PN, cycle.state_pn_cur);
      
      cycle.state_cur = 0;
    }
    // pressure up
    else
    {
      cycle.state_vi_cur = 0;
      cycle.state_vo_cur = 0;
      cycle.state_vb_cur = 1;
      cycle.state_pb_cur = 1;
      cycle.state_pn_cur = 1;
      digitalWrite(RO_VI, cycle.state_vi_cur);
      digitalWrite(RO_VO, cycle.state_vo_cur);
      digitalWrite(RO_VB, cycle.state_vb_cur);
      digitalWrite(RO_PB, cycle.state_pb_cur);
      digitalWrite(RO_PN, cycle.state_pn_cur);
      
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
      cycle.state_vi_cur = 1;
      cycle.state_vo_cur = 1;
      cycle.state_vb_cur = 0;
      cycle.state_pb_cur = 0;
      cycle.state_pn_cur = 0;
      digitalWrite(RO_VI, cycle.state_vi_cur);
      digitalWrite(RO_VO, cycle.state_vo_cur);
      digitalWrite(RO_VB, cycle.state_vb_cur);
      digitalWrite(RO_PB, cycle.state_pb_cur);
      digitalWrite(RO_PN, cycle.state_pn_cur);
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

void cycle_manager()
{
  if (cycle.mode_cur == 0) cycle_mode_manual();
  else if (cycle.mode_cur == 1) cycle_mode_pressostato();
}