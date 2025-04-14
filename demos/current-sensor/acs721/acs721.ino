void setup() 
{
  Serial.begin(9600);
}

uint32_t millis_cur = 0;
uint32_t samples_count = 0;
uint32_t samples_tot = 0;


void loop() 
{
  int adc = analogRead(26);
  samples_tot += adc;
  samples_count += 1;
  
  if (millis() - millis_cur > 500) 
  {
    millis_cur = millis();
    Serial.println(samples_tot/samples_count);
    samples_tot = 0;
    samples_count = 0;
  }

}
