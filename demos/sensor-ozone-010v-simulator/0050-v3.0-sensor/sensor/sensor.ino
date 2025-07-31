#define ledPin 4

void setup() 
{
  Serial.begin(9600);
  
  pinMode(ledPin, INPUT);
}
void loop() 
{
  
  Serial.println(analogRead(ledPin));

  delay(100);
}

