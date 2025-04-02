#define PUMP_VALVE_GPIO 5
#define PUMP_BOOSTER_GPIO 18
#define PUMP_NANO_GPIO 19
#define NA_GPIO 23
#define FLOW_SWITCH_GPIO 25
#define PRESSURE_SWITCH_GPIO 26
#define VALVE_BYPASS_1_GPIO 2
#define VALVE_BYPASS_2_GPIO 13

void setup() 
{
  pinMode(PUMP_VALVE_GPIO, OUTPUT);
  digitalWrite(PUMP_VALVE_GPIO, 0);
  pinMode(PUMP_BOOSTER_GPIO, OUTPUT);
  digitalWrite(PUMP_BOOSTER_GPIO, 0);
  pinMode(PUMP_NANO_GPIO, OUTPUT);
  digitalWrite(PUMP_NANO_GPIO, 0);
  pinMode(NA_GPIO, OUTPUT);
  digitalWrite(NA_GPIO, 0);
  pinMode(FLOW_SWITCH_GPIO, OUTPUT);
  digitalWrite(FLOW_SWITCH_GPIO, 0);
  pinMode(PRESSURE_SWITCH_GPIO, OUTPUT);
  digitalWrite(PRESSURE_SWITCH_GPIO, 0);
  pinMode(VALVE_BYPASS_1_GPIO, OUTPUT);
  digitalWrite(VALVE_BYPASS_1_GPIO, 0);
  pinMode(VALVE_BYPASS_2_GPIO, OUTPUT);
  digitalWrite(VALVE_BYPASS_2_GPIO, 0);
}

void loop() 
{
  digitalWrite(PUMP_VALVE_GPIO, 1);
  digitalWrite(PUMP_BOOSTER_GPIO, 1);
  digitalWrite(PUMP_NANO_GPIO, 1);
  digitalWrite(NA_GPIO, 1);
  digitalWrite(FLOW_SWITCH_GPIO, 1);
  digitalWrite(PRESSURE_SWITCH_GPIO, 1);
  digitalWrite(VALVE_BYPASS_1_GPIO, 1);
  digitalWrite(VALVE_BYPASS_2_GPIO, 1);
  delay(30000);
  digitalWrite(PUMP_VALVE_GPIO, 0);
  digitalWrite(PUMP_BOOSTER_GPIO, 0);
  digitalWrite(PUMP_NANO_GPIO, 0);
  digitalWrite(NA_GPIO, 0);
  digitalWrite(FLOW_SWITCH_GPIO, 0);
  digitalWrite(PRESSURE_SWITCH_GPIO, 0);
  digitalWrite(VALVE_BYPASS_1_GPIO, 0);
  digitalWrite(VALVE_BYPASS_2_GPIO, 0);
  delay(5000);
}
