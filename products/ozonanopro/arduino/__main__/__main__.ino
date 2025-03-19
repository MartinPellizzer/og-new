#define pin_flow 15
#define pin_nanobubble_pump 5
#define pin_booster_pump 18
#define pin_oxygen_concentrator 19
#define pin_ozone_generator 23

int cycle_state = -1;

uint32_t cycle_millis = 0;


///////////////////////////////////////////////////////////////////////
// ;nextion
///////////////////////////////////////////////////////////////////////
const uint8_t BUFFER_SIZE = 20;
typedef struct nextion_t {  
  uint8_t inputs_buff[BUFFER_SIZE];
  uint8_t bytestream_receiving = 0;
  uint32_t bytestream_millis = 0;
  uint32_t bytestream_buff_index = 0;
  int16_t page_old = -1;
  int16_t page_cur = 0;
} nextion_t;
nextion_t nextion = {};

typedef struct power_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} power_t;
power_t power = {};

typedef struct pump_booster_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
} pump_booster_t;
pump_booster_t pump_booster = {};

typedef struct pump_nano_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
} pump_nano_t;
pump_nano_t pump_nano = {};

typedef struct flow_switch_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} flow_switch_t;
flow_switch_t flow_switch = {};

typedef struct valve_bypass_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} valve_bypass_t;
valve_bypass_t valve_bypass = {};

typedef struct oxygen_concentrator_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} oxygen_concentrator_t;
oxygen_concentrator_t oxygen_concentrator = {};

typedef struct ozone_generator_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} ozone_generator_t;
ozone_generator_t ozone_generator = {};

void cycle_starting()
{
  if (cycle_state == 0)
  {
    if (millis() - cycle_millis > 1000)
    {
      cycle_state = 1;
      pump_booster.state_cur = 1;
      pump_nano.state_cur = 1;
      digitalWrite(pin_booster_pump, HIGH);
      digitalWrite(pin_nanobubble_pump, HIGH);
      cycle_millis = millis();
    }
  }
  if (cycle_state == 1)
  {
    if (millis() - cycle_millis > 3000)
    {
      cycle_state = 2;
      oxygen_concentrator.state_cur = 1;
      oxygen_concentrator.nextion_refresh = 1;
      digitalWrite(pin_oxygen_concentrator, HIGH);
      cycle_millis = millis();
    }
  }
  if (cycle_state == 2)
  {
    if (millis() - cycle_millis > 3000)
    {
      cycle_state = 3;
      ozone_generator.state_cur = 1;
      ozone_generator.nextion_refresh = 1;
      digitalWrite(pin_ozone_generator, HIGH);
      cycle_millis = millis();
    }
  }
  // if (cycle_state == 3)
  // {
  //   if (millis() - cycle_millis > 3000)
  //   {
  //     cycle_state = -1;
  //     digitalWrite(pin_booster_pump, LOW);
  //     digitalWrite(pin_oxygen_concentrator, LOW);
  //     digitalWrite(pin_ozone_generator, LOW);
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
      pump_booster.state_cur = 0;
      pump_nano.state_cur = 0;
      oxygen_concentrator.state_cur = 0;
      oxygen_concentrator.nextion_refresh = 1;
      ozone_generator.state_cur = 0;
      ozone_generator.nextion_refresh = 1;
      digitalWrite(pin_nanobubble_pump, LOW);
      digitalWrite(pin_booster_pump, LOW);
      digitalWrite(pin_oxygen_concentrator, LOW);
      digitalWrite(pin_ozone_generator, LOW);
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
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  pinMode(pin_flow, INPUT_PULLUP);
  pinMode(pin_booster_pump, OUTPUT);
  pinMode(pin_oxygen_concentrator, OUTPUT);
  pinMode(pin_ozone_generator, OUTPUT);
  pinMode(pin_nanobubble_pump, OUTPUT);

  delay(3000);
  nextion.page_cur = 1;
}

void loop()
{
  // TODO: implement logic of power
  power.state_cur = 1;
  power.state_old = power.state_cur;
  power.nextion_refresh = 1;
  
  // TODO: implement logic of valve_bypass
  valve_bypass.state_cur = 0;
  valve_bypass.state_old = valve_bypass.state_cur;
  valve_bypass.nextion_refresh = 1;
  
  flow_switch.state_cur = digitalRead(pin_flow);
  if (flow_switch.state_old != flow_switch.state_cur)
  {
    flow_switch.state_old = flow_switch.state_cur;
    flow_switch.nextion_refresh = 1;
    if (flow_switch.state_cur == 0)
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
  
  nextion_update();
}