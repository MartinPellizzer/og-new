
#define COMPRESSOR_GPIO 5
#define OZONE_GENERATOR_GPIO 18

int32_t cycle_millis = 0;
int32_t cycle_state = 0;

void setup() 
{
  Serial.begin(9600);

  pinMode(COMPRESSOR_GPIO, OUTPUT);
  digitalWrite(COMPRESSOR_GPIO, LOW);
  pinMode(OZONE_GENERATOR_GPIO, OUTPUT);
  digitalWrite(OZONE_GENERATOR_GPIO, LOW);
}

void loop() 
{
  if (cycle_state == 0)
  {
    Serial.println("CICLE 1");
    digitalWrite(COMPRESSOR_GPIO, HIGH);
    cycle_state = 1;
  }
  
  if (cycle_state == 1)
  {
    if (millis() - cycle_millis > 10000)
    {
      Serial.println("CICLE 2");
      cycle_millis = millis();
      digitalWrite(COMPRESSOR_GPIO, LOW);
      digitalWrite(OZONE_GENERATOR_GPIO, HIGH);
      cycle_state = 2;
    }
  }
  
  if (cycle_state == 2)
  {
    if (millis() - cycle_millis > 10000)
    {
      Serial.println("CICLE 3");
      cycle_millis = millis();
      digitalWrite(OZONE_GENERATOR_GPIO, LOW);
      cycle_state = 3;
    }
  }
}