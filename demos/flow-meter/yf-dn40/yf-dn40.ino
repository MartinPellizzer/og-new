typedef struct flowmeter_t 
{
  const uint8_t gpio = 27;
  volatile uint16_t pulses_count = 0;
  uint16_t pulses_count_one_sec = 0;
  uint32_t sampling_millis = 0;
  uint32_t sampling_interval = 1000;
  float calibration_factor = 0.45;
  float frequency_cur = 0;
  float flow_l_m_cur = 0;
  float flow_ml_s_cur = 0;
  float flow_ml_tot = 0;
} flowmeter_t;
flowmeter_t flowmeter;

void flowmeter_manager()
{
  if (millis() - flowmeter.sampling_millis > flowmeter.sampling_interval) 
  {
    flowmeter.pulses_count_one_sec = flowmeter.pulses_count;
    flowmeter.pulses_count = 0;

    flowmeter_frequency_get();
    flowmeter_flow_litre_minute_get();
    flowmeter_flow_millilitre_second_get();
    flowmeter_flow_millilitre_total_get();

    flowmeter.sampling_millis = millis();
    flowmeter_debug();
  }
}

void IRAM_ATTR pulse_counter()
{
  flowmeter.pulses_count++;
}

void setup()
{
  Serial.begin(9600);
  pinMode(flowmeter.gpio, INPUT_PULLUP);

  flowmeter.sampling_millis = 0;
  attachInterrupt(digitalPinToInterrupt(flowmeter.gpio), pulse_counter, RISING);
}

void loop()
{
  flowmeter_manager();
}