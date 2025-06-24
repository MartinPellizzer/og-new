void setup() 
{
  pinMode(15, OUTPUT);
  digitalWrite(15, 0);
}

void loop() 
{
  delay(1000);
  digitalWrite(15, 1);
  delay(1000);
  digitalWrite(15, 0);
}
