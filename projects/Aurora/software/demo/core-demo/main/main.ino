#define HEARTBEAT_PIN 13

void setup() 
{
  Serial.begin(9600);
  pinMode(HEARTBEAT_PIN, OUTPUT);
  digitalWrite(HEARTBEAT_PIN, LOW);
}

void loop()
{
  delay(1000);
  digitalWrite(HEARTBEAT_PIN, HIGH);
  delay(1000);
  digitalWrite(HEARTBEAT_PIN, LOW);
}

