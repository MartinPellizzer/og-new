typedef struct current_sensor_t {
  uint8_t adc_gpio = 26;
  uint8_t voltage_calibration_button_gpio = 2;
  uint16_t adc_cur = 0;
  uint32_t samples_count = 0;
  uint32_t samples_tot = 0;
  uint32_t samples_millis = 0;
  uint32_t samples_timer = 500;
  uint8_t data_received = 0;
  float voltage_raw_cur = 0;
  float voltage_calibrated_cur = 0;
  float voltage_calibration_val  = 0;
  float current_cur = 0;
  uint8_t calibrated = 0;
} current_sensor_t;
current_sensor_t current_sensor = {};

void setup() 
{
  Serial.begin(9600);
  pinMode(current_sensor.voltage_calibration_button_gpio, INPUT_PULLUP);
}

void voltage_raw_get()
{
  current_sensor.voltage_raw_cur = ((float)current_sensor.adc_cur * 3.3)/4096.0f;
}

void voltage_calibrated_get()
{
  voltage_raw_get();
  current_sensor.voltage_calibrated_cur = current_sensor.voltage_raw_cur - current_sensor.voltage_calibration_val;
}

void voltage_calibration_val_get()
{
  voltage_raw_get();
  current_sensor.voltage_calibration_val = current_sensor.voltage_raw_cur;
}

void voltage_calibration_val_get_button()
{
  if (digitalRead(current_sensor.voltage_calibration_button_gpio) == 0)
  {
    voltage_calibration_val_get();
  }
}

void voltage_calibration_val_get_auto()
{
  int adc = analogRead(current_sensor.adc_gpio);
  current_sensor.samples_tot += adc;
  current_sensor.samples_count += 1;
  if (millis() - current_sensor.samples_millis > 3000) 
  {
    current_sensor.samples_millis = millis();
    current_sensor.adc_cur = current_sensor.samples_tot/current_sensor.samples_count;
    voltage_calibration_val_get();
    current_sensor.calibrated = 1;
    current_sensor.samples_tot = 0;
    current_sensor.samples_count = 0;
    current_sensor.data_received = 1;
  }
}

void adc_get()
{
  int adc = analogRead(current_sensor.adc_gpio);
  current_sensor.samples_tot += adc;
  current_sensor.samples_count += 1;
  if (millis() - current_sensor.samples_millis > current_sensor.samples_timer) 
  {
    current_sensor.samples_millis = millis();
    current_sensor.adc_cur = current_sensor.samples_tot/current_sensor.samples_count;
    current_sensor.samples_tot = 0;
    current_sensor.samples_count = 0;
    current_sensor.data_received = 1;
  }
}

void current_sensor_manager()
{
  voltage_calibration_val_get_button();
  voltage_calibration_val_get_auto();
  if (current_sensor.calibrated == 1)
  {
    adc_get();
    if (current_sensor.data_received == 1)
    {
      current_sensor.data_received = 0;
      voltage_calibrated_get();
      current_sensor.current_cur = current_sensor.voltage_calibrated_cur/0.100f;
      Serial.print("ADC: ");
      Serial.print(current_sensor.adc_cur);
      Serial.print("   -->   ");
      Serial.print("VOLTAGE: ");
      Serial.print(current_sensor.voltage_calibrated_cur, 3);
      Serial.print(" / ");
      Serial.print("CURRENT: ");
      Serial.println(current_sensor.current_cur);
    }
  }
}

void loop() 
{
  current_sensor_manager();
}
