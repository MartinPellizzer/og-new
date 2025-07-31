#define v010_1 36
#define v010_2 39
#define v010_3 34

#define relay_1 33
#define relay_2 25
#define relay_3 26
#define relay_4 13
#define relay_5 15
#define relay_6 5
#define relay_7 18
#define relay_8 19

#define button_1 23
#define button_2 35
#define button_3 32

uint32_t timer_cur = 0;
uint32_t timer_max = 30000;

void setup() 
{
  Serial.begin(9600);
  
  pinMode(v010_1, INPUT);
  pinMode(v010_2, INPUT);
  pinMode(v010_3, INPUT);
  
  pinMode(relay_1, OUTPUT);
  pinMode(relay_2, OUTPUT);
  pinMode(relay_3, OUTPUT);
  pinMode(relay_4, OUTPUT);
  pinMode(relay_5, OUTPUT);
  pinMode(relay_6, OUTPUT);
  pinMode(relay_7, OUTPUT);
  pinMode(relay_8, OUTPUT);

  pinMode(button_1, INPUT_PULLUP);
  pinMode(button_2, INPUT_PULLUP);
  pinMode(button_3, INPUT_PULLUP);
  
}
void loop() 
{
  int val = 0;

  val = analogRead(v010_1);
  Serial.print("PIN 34: ");
  Serial.println(val);

  val = analogRead(v010_2);
  Serial.print("PIN 35: ");
  Serial.println(val);

  val = analogRead(v010_3);
  Serial.print("PIN 32: ");
  Serial.println(val);

  Serial.print("BTN 1 - PIN 23: ");
  Serial.println(digitalRead(button_1));
  Serial.print("BTN 2 - PIN 35: ");
  Serial.println(digitalRead(button_2));
  Serial.print("BTN 3 - PIN 32: ");
  Serial.println(digitalRead(button_3));

  if (millis() - timer_cur > timer_max)
  {
    timer_cur = millis();
    digitalWrite(relay_1, !digitalRead(relay_1));
    digitalWrite(relay_2, !digitalRead(relay_2));
    digitalWrite(relay_3, !digitalRead(relay_3));
    digitalWrite(relay_4, !digitalRead(relay_4));
    digitalWrite(relay_5, !digitalRead(relay_5));
    digitalWrite(relay_6, !digitalRead(relay_6));
    digitalWrite(relay_7, !digitalRead(relay_7));
    digitalWrite(relay_8, !digitalRead(relay_8));
  }

  Serial.println();
  delay(500);
  
  /*
  int ppb = 10000;
  if (ppb > 9999)
  {
    ppb = 9999;
  }
  // send 0-10V
  uint8_t pwm_val = map(ppb, 0, 10000, 0, 255);
  analogWrite(ledPin, pwm_val);
  
  Serial.print(ppb);
  Serial.print(" - ");
  Serial.println(pwm_val);

  delay(500);
  */
}

