typedef struct flowmeter_t 
{
  const uint8_t gpio = 27;
  volatile uint16_t pulses_count = 0;
  uint16_t pulses_count_one_sec = 0;
  float calibration_factor = 0.45;
  float frequency_cur = 0;
  float flow_l_m_cur = 0;
  float flow_ml_s_cur = 0;
  float flow_ml_tot = 0;
} flowmeter_t;
flowmeter_t flowmeter;

long currentMillis = 0;
long previousMillis = 0;
int interval = 1000;

void IRAM_ATTR pulse_counter()
{
  flowmeter.pulses_count++;
}

void setup()
{
  Serial.begin(9600);

  pinMode(flowmeter.gpio, INPUT_PULLUP);

  previousMillis = 0;

  attachInterrupt(digitalPinToInterrupt(flowmeter.gpio), pulse_counter, FALLING);
}

void loop()
{
  currentMillis = millis();
  if (currentMillis - previousMillis > interval) 
  {
    flowmeter.pulses_count_one_sec = flowmeter.pulses_count;
    flowmeter.pulses_count = 0;

    frequency_calc(flowmeter.pulses_count_one_sec, interval);
    flow_l_m_calc(flowmeter.frequency_cur);
    flow_ml_s_calc(flowmeter.frequency_cur);
    flow_ml_tot_calc();

    previousMillis = millis();
    
    // Print the flow rate for this second in litres / minute
    Serial.print("Flow rate: ");
    Serial.print(int(flowmeter.flow_l_m_cur));  // Print the integer part of the variable
    Serial.print("L/min");
    Serial.print("\t");       // Print tab space

    // Print the cumulative total of litres flowed since starting
    Serial.print("Output Liquid Quantity: ");
    Serial.print(flowmeter.flow_ml_tot);
    Serial.print("mL / ");
    Serial.print(flowmeter.flow_ml_tot / 1000);
    Serial.println("L");
  }
}