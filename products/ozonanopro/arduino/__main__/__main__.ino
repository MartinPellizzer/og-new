#define pin_flow 15
#define pin_valve 5
#define pin_pump 18
#define pin_nano 19
#define pin_ozone 23

int flow_state_old = -1;
int flow_state_cur = -1;

int cycle_state = -1;

uint32_t cycle_millis = 0;

void cycle_starting()
{
  if (cycle_state == 0)
  {
    if (millis() - cycle_millis > 1000)
    {
      cycle_state = 1;
      digitalWrite(pin_pump, HIGH);
      digitalWrite(pin_valve, HIGH);
      cycle_millis = millis();
    }
  }
  if (cycle_state == 1)
  {
    if (millis() - cycle_millis > 3000)
    {
      cycle_state = 2;
      digitalWrite(pin_nano, HIGH);
      cycle_millis = millis();
    }
  }
  if (cycle_state == 2)
  {
    if (millis() - cycle_millis > 3000)
    {
      cycle_state = 3;
      digitalWrite(pin_ozone, HIGH);
      cycle_millis = millis();
    }
  }
  // if (cycle_state == 3)
  // {
  //   if (millis() - cycle_millis > 3000)
  //   {
  //     cycle_state = -1;
  //     digitalWrite(pin_pump, LOW);
  //     digitalWrite(pin_nano, LOW);
  //     digitalWrite(pin_ozone, LOW);
  //     cycle_millis = millis();
  //   }
  // }
}

void cycle_terminating()
{
  if (cycle_state == 100)
  {
    if (millis() - cycle_millis > 1000)
    {
      cycle_state = -1;
      digitalWrite(pin_valve, LOW);
      digitalWrite(pin_pump, LOW);
      digitalWrite(pin_nano, LOW);
      digitalWrite(pin_ozone, LOW);
      cycle_millis = millis();
    }
  }
}

void cycle_manager()
{
  cycle_starting();
  cycle_terminating();
}

void setup()
{
  Serial.begin(9600);
  pinMode(pin_flow, INPUT_PULLUP);
  pinMode(pin_pump, OUTPUT);
  pinMode(pin_nano, OUTPUT);
  pinMode(pin_ozone, OUTPUT);
  pinMode(pin_valve, OUTPUT);
}

void loop()
{
  int flow_state_cur = digitalRead(pin_flow);

  if (flow_state_old != flow_state_cur)
  {
    flow_state_old = flow_state_cur;
    if (flow_state_cur == 0)
    {
      cycle_state = 0;
      cycle_millis = millis();
    }
    else
    {
      cycle_state = 100;
      cycle_millis = millis();
    }
  }
  
  cycle_manager();
}