

void frequency_calc(uint32_t n_pulses, uint32_t t_millis)
{
  float t_millis_adj = (float)t_millis / (float)(millis() - previousMillis);
  flowmeter.frequency_cur = t_millis_adj * n_pulses;
}

void flow_l_m_calc(float frequency)
{
  flowmeter.flow_l_m_cur = frequency / flowmeter.calibration_factor;
}

void flow_ml_s_calc(float frequency)
{
  flowmeter.flow_l_m_cur = frequency / flowmeter.calibration_factor;
  flowmeter.flow_ml_s_cur = (flowmeter.flow_l_m_cur / 60) * 1000;
}

void flow_ml_tot_calc()
{
  flowmeter.flow_ml_tot += flowmeter.flow_ml_s_cur;
}