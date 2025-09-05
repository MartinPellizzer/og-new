#define LED_PIN 5

void setup() 
{
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() 
{
  analogWrite(LED_PIN, 255);

}

