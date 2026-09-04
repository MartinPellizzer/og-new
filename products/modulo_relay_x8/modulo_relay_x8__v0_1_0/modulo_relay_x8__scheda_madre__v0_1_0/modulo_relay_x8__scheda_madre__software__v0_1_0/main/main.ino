
void setup() 
{
  Serial.begin(9600);
  pinMode(25, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(13, OUTPUT);
  // pinMode(15, OUTPUT);
  // pinMode(5, OUTPUT);
  pinMode(32, OUTPUT);
  pinMode(33, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(27, OUTPUT);
  pinMode(35, INPUT);
  // digitalWrite(25, HIGH);
  // delay(10000);
}

void loop() 
{
  // digitalWrite(32, !digitalRead(32));
  // delay(1000);
  // digitalWrite(33, !digitalRead(33));
  // delay(1000);
  // digitalWrite(25, !digitalRead(25));
  // delay(1000);
  // digitalWrite(26, !digitalRead(26));
  // delay(1000);
  // digitalWrite(13, !digitalRead(13));
  // delay(1000);
  // // digitalWrite(15, !digitalRead(15));
  // // delay(1000);
  // // digitalWrite(5, !digitalRead(5));
  // // delay(1000);
  // digitalWrite(18, !digitalRead(18));
  // delay(1000);
  // digitalWrite(19, !digitalRead(19));
  // delay(1000);
  // digitalWrite(23, !digitalRead(23));
  // delay(1000);
  // digitalWrite(27, !digitalRead(27));
  // delay(1000);
  // digitalWrite(27, !digitalRead(27));
  // delay(1000);
  if (digitalRead(35) == 0)
  {
    digitalWrite(27, 0);
  }
  else
  {
    digitalWrite(27, 1);
  }

}

