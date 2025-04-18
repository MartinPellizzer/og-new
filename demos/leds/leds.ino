void setup() 
{
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  digitalWrite(2, 0);
  digitalWrite(4, 0);
  digitalWrite(5, 0);

}

void loop() 
{
  digitalWrite(2, 1);
  digitalWrite(4, 0);
  digitalWrite(5, 0);
  delay(500);
  digitalWrite(2, 0);
  digitalWrite(4, 1);
  digitalWrite(5, 0);
  delay(500);
  digitalWrite(2, 0);
  digitalWrite(4, 0);
  digitalWrite(5, 1);
  delay(500);

}
