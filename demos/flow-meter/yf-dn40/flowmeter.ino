
void flowmeter_frequency_get()
{
  float t_millis_adj = (float)flowmeter.sampling_interval / (float)(millis() - flowmeter.sampling_millis);
  flowmeter.frequency_cur = t_millis_adj * flowmeter.pulses_count_one_sec;
}

void flowmeter_flow_litre_minute_get()
{
  flowmeter.flow_l_m_cur = flowmeter.frequency_cur / flowmeter.calibration_factor;
}

void flowmeter_flow_millilitre_second_get()
{
  flowmeter.flow_l_m_cur = flowmeter.frequency_cur / flowmeter.calibration_factor;
  flowmeter.flow_ml_s_cur = (flowmeter.flow_l_m_cur / 60) * 1000;
}

void flowmeter_flow_millilitre_total_get()
{
  flowmeter.flow_ml_tot += flowmeter.flow_ml_s_cur;
}

void flowmeter_flow_litre_minute_debug()
{
  Serial.print("Flow rate: ");
  Serial.print(int(flowmeter.flow_l_m_cur));
  Serial.print("L/min");
  Serial.print("\t");
}

void flowmeter_flow_millilitre_tot_debug()
{
  Serial.print("Millilitre Total: ");
  Serial.print(flowmeter.flow_ml_tot);
  Serial.print("mL / ");
}

void flowmeter_flow_litre_tot_debug()
{
  Serial.print("Litre Total: ");
  Serial.print(flowmeter.flow_ml_tot / 1000);
  Serial.print("L");
}


void flowmeter_debug()
{
  flowmeter_flow_litre_minute_debug();
  flowmeter_flow_millilitre_tot_debug();
  flowmeter_flow_litre_tot_debug();
  Serial.println();
}