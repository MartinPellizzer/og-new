#define pin 9

void setup() 
{
  Serial.begin(9600);
  pinMode(pin, OUTPUT);
}

void loop() 
{
  for (int i = 0; i <= 255; i++)
  {
    analogWrite(pin, i);
    delay(15);
    Serial.println(i);
  }
  for (int i = 255; i >= 0; i--)
  {
    analogWrite(pin, i);
    delay(15);
    Serial.println(i);
  }
  // analogWrite(pin, 0);
  // delay(500);
  // Serial.println(0);
  // analogWrite(pin, 64);
  // delay(500);
  // Serial.println(64);
  // analogWrite(pin, 128);
  // delay(500);
  // Serial.println(128);
  // analogWrite(pin, 180);
  // delay(500);
  // Serial.println(180);
  // analogWrite(pin, 255);
  // delay(500);
  // Serial.println(255);
}
