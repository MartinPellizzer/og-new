// SLAVE

HardwareSerial rs485_serial(1);
uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

#define RE_DE_PIN 16

#include <ModbusSlave.h>
Modbus slave(rs485_serial, 1, RE_DE_PIN);

#define RELAY_DRIVER_1_PIN 13
#define RELAY_DRIVER_2_PIN 18
#define RELAY_DRIVER_3_PIN 19
#define RELAY_DRIVER_4_PIN 23
#define RELAY_DRIVER_5_PIN 32
#define RELAY_DRIVER_6_PIN 33
#define RELAY_DRIVER_7_PIN 25
#define RELAY_DRIVER_8_PIN 26

#define SENSOR_BUFF_LEN 9
typedef struct sensor_t {
  uint8_t buff[SENSOR_BUFF_LEN] = { 0 };
  uint8_t buff_i = 0;
  uint8_t buff_ready = 0;
  uint32_t buff_timer = 0;
  int16_t ppb_old = 0;
  int16_t ppb_cur = 0;
  uint32_t timeout_timer_cur = 0; 
  uint8_t timeout_error = 0; 
} sensor_t;
sensor_t sensor = {};

uint8_t button_value = 0;

int led_state = 0;


uint32_t timer_cur = 0; 

uint8_t relay1_state = LOW;
uint8_t relay2_state = LOW;
uint8_t relay3_state = LOW;
uint8_t relay4_state = LOW;
uint8_t relay5_state = LOW;
uint8_t relay6_state = LOW;
uint8_t relay7_state = LOW;
uint8_t relay8_state = LOW;


enum device_state_enum {
    INITIALIZING,
    READY,
    OPERATING,
    WARNING,
    FAULT,
    MAINTENANCE,
    OFFLINE,
};

device_state_enum device_state = INITIALIZING;

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  rs485_serial.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);
  pinMode(RELAY_DRIVER_1_PIN, OUTPUT);
  digitalWrite(RELAY_DRIVER_1_PIN, LOW);
  pinMode(RELAY_DRIVER_2_PIN, OUTPUT);
  digitalWrite(RELAY_DRIVER_2_PIN, LOW);
  pinMode(RELAY_DRIVER_3_PIN, OUTPUT);
  digitalWrite(RELAY_DRIVER_3_PIN, LOW);
  pinMode(RELAY_DRIVER_4_PIN, OUTPUT);
  digitalWrite(RELAY_DRIVER_4_PIN, LOW);
  pinMode(RELAY_DRIVER_5_PIN, OUTPUT);
  digitalWrite(RELAY_DRIVER_5_PIN, LOW);
  pinMode(RELAY_DRIVER_6_PIN, OUTPUT);
  digitalWrite(RELAY_DRIVER_6_PIN, LOW);
  pinMode(RELAY_DRIVER_7_PIN, OUTPUT);
  digitalWrite(RELAY_DRIVER_7_PIN, LOW);
  pinMode(RELAY_DRIVER_8_PIN, OUTPUT);
  digitalWrite(RELAY_DRIVER_8_PIN, LOW);

  slave.cbVector[CB_WRITE_COILS] = writeDigitalOut;
  // slave.cbVector[CB_READ_COILS] = readCoils; // FC01
  slave.cbVector[CB_READ_DISCRETE_INPUTS] = readDiscreteInputs; // FC02
  // slave.cbVector[CB_READ_INPUT_REGISTERS] = readAnalogIn;

  slave.begin(9600);
}


void loop() 
{
  slave.poll();

  if (device_state == INITIALIZING)
  {
    if (millis() - timer_cur > 5000) 
    {
      device_state = READY;
    }
  }

  // if (millis() - timer_cur > 5000) 
  // {
  //   // if (sensor.timeout_error == 0)
  //   {
  //     // sensor.timeout_error = 1;
  //     sensor.ppb_cur = 10001;
  //   }
  // }

  // ze27o3_listen();

  // if (ze27o3_ready())
  // {
  //   sensor.buff_i = 0;
  //   sensor.buff_ready = 0;

  //   // CHECKSUM
  //   if (ze27o3_checksum_valid())
  //   {
  //     Serial.println("CHECKSUM: VALID");
  //     sensor.ppb_cur = ze27o3_ppb_get();

  //     sensor.timeout_timer_cur = millis();
  //     // sensor.timeout_error = 0;
  //   }
  //   else
  //   {
  //     Serial.println("CHECKSUM: ERROR");
  //   }

  //   ze27o3_debug();
  // }
}

uint8_t readAnalogIn(uint8_t fc, uint16_t address, uint16_t length, void* data)
{
    Serial.printf(
        "FC=%u, Address=%u, Length=%u -> ",
        fc, address, length
    );
    if (length == 1)
    {
      if (address == 100)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, device_state);
          return STATUS_OK;
      }
      else if (address == 102)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, digitalRead(RELAY_DRIVER_2_PIN));
          return STATUS_OK;
      }
      else if (address == 103)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, digitalRead(RELAY_DRIVER_3_PIN));
          return STATUS_OK;
      }
      else if (address == 104)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, digitalRead(RELAY_DRIVER_4_PIN));
          return STATUS_OK;
      }
      else if (address == 105)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, digitalRead(RELAY_DRIVER_5_PIN));
          return STATUS_OK;
      }
      else if (address == 106)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, digitalRead(RELAY_DRIVER_6_PIN));
          return STATUS_OK;
      }
      else if (address == 107)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, digitalRead(RELAY_DRIVER_7_PIN));
          return STATUS_OK;
      }
      else if (address == 108)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, digitalRead(RELAY_DRIVER_8_PIN));
          return STATUS_OK;
      }
      else
      {
        Serial.println("STATUS_ILLEGAL_DATA_ADDRESS");
        return STATUS_ILLEGAL_DATA_ADDRESS;
      }
    }
    else
    {
      Serial.println("STATUS_ILLEGAL_DATA_VALUE");
      return STATUS_ILLEGAL_DATA_VALUE;
    }
}

uint8_t readDiscreteInputs(uint8_t fc, uint16_t address, uint16_t length, void* data)
{
    Serial.printf(
        "FC=%u, Address=%u, Length=%u -> ",
        fc, address, length
    );

    if (length != 1)
        return STATUS_ILLEGAL_DATA_VALUE;

    if (address == 0)
    {
      Serial.print("RELAY 1 STATE: ");
      Serial.println(relay1_state);
      slave.writeCoilToBuffer(0, relay1_state);
      return STATUS_OK;
    }
    else if (address == 1)
    {
      Serial.print("RELAY 2 STATE: ");
      Serial.println(relay2_state);
      slave.writeCoilToBuffer(0, relay2_state);
      return STATUS_OK;
    }
    else if (address == 2)
    {
      Serial.print("RELAY 3 STATE: ");
      Serial.println(relay3_state);
      slave.writeCoilToBuffer(0, relay3_state);
      return STATUS_OK;
    }
    else if (address == 3)
    {
      Serial.print("RELAY 4 STATE: ");
      Serial.println(relay4_state);
      slave.writeCoilToBuffer(0, relay4_state);
      return STATUS_OK;
    }
    else if (address == 4)
    {
      Serial.print("RELAY 5 STATE: ");
      Serial.println(relay5_state);
      slave.writeCoilToBuffer(0, relay5_state);
      return STATUS_OK;
    }
    else if (address == 5)
    {
      Serial.print("RELAY 6 STATE: ");
      Serial.println(relay6_state);
      slave.writeCoilToBuffer(0, relay6_state);
      return STATUS_OK;
    }
    else if (address == 6)
    {
      Serial.print("RELAY 7 STATE: ");
      Serial.println(relay7_state);
      slave.writeCoilToBuffer(0, relay7_state);
      return STATUS_OK;
    }
    else if (address == 7)
    {
      Serial.print("RELAY 8 STATE: ");
      Serial.println(relay8_state);
      slave.writeCoilToBuffer(0, relay8_state);
      return STATUS_OK;
    }

    return STATUS_ILLEGAL_DATA_ADDRESS;
}

uint8_t writeDigitalOut(uint8_t fc, uint16_t address, uint16_t length, void* data)
{
  Serial.print("FC=05: ");
  Serial.println(fc);
  Serial.println(address);
  Serial.println(length);
  
  const char* address_coil_1 = "00001";
  uint16_t address_coil_1_zero_based = atoi(address_coil_1) - 1;
  const char* address_coil_2 = "00002";
  uint16_t address_coil_2_zero_based = atoi(address_coil_2) - 1;
  const char* address_coil_3 = "00003";
  uint16_t address_coil_3_zero_based = atoi(address_coil_3) - 1;
  const char* address_coil_4 = "00004";
  uint16_t address_coil_4_zero_based = atoi(address_coil_4) - 1;
  const char* address_coil_5 = "00005";
  uint16_t address_coil_5_zero_based = atoi(address_coil_5) - 1;
  const char* address_coil_6 = "00006";
  uint16_t address_coil_6_zero_based = atoi(address_coil_6) - 1;
  const char* address_coil_7 = "00007";
  uint16_t address_coil_7_zero_based = atoi(address_coil_7) - 1;
  const char* address_coil_8 = "00008";
  uint16_t address_coil_8_zero_based = atoi(address_coil_8) - 1;

  if (address == address_coil_1_zero_based)
  {
    relay1_state = slave.readCoilFromBuffer(0);
    digitalWrite(RELAY_DRIVER_1_PIN, relay1_state);
  }
  if (address == address_coil_2_zero_based)
  {
    relay2_state = slave.readCoilFromBuffer(0);
    digitalWrite(RELAY_DRIVER_2_PIN, relay2_state);
  }
  if (address == address_coil_3_zero_based)
  {
    relay3_state = slave.readCoilFromBuffer(0);
    digitalWrite(RELAY_DRIVER_3_PIN, relay3_state);
  }
  if (address == address_coil_4_zero_based)
  {
    relay4_state = slave.readCoilFromBuffer(0);
    digitalWrite(RELAY_DRIVER_4_PIN, relay4_state);
  }
  if (address == address_coil_5_zero_based)
  {
    relay5_state = slave.readCoilFromBuffer(0);
    digitalWrite(RELAY_DRIVER_5_PIN, relay5_state);
  }
  if (address == address_coil_6_zero_based)
  {
    relay6_state = slave.readCoilFromBuffer(0);
    digitalWrite(RELAY_DRIVER_6_PIN, relay6_state);
  }
  if (address == address_coil_7_zero_based)
  {
    relay7_state = slave.readCoilFromBuffer(0);
    digitalWrite(RELAY_DRIVER_7_PIN, relay7_state);
  }
  if (address == address_coil_8_zero_based)
  {
    relay8_state = slave.readCoilFromBuffer(0);
    digitalWrite(RELAY_DRIVER_8_PIN, relay8_state);
  }
  return STATUS_OK;
}
