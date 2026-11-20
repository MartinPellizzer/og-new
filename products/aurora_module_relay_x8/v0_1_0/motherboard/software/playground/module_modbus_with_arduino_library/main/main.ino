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
  // slave.cbVector[CB_READ_COILS] = readDigital;
  slave.cbVector[CB_READ_INPUT_REGISTERS] = readAnalogIn;

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
      if (address == 100 || address == 40101)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, device_state);
          return STATUS_OK;
      }
      else if (address == 101 || address == 40102)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, analogRead(RELAY_DRIVER_1_PIN));
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

// uint8_t readDigital(uint8_t fc, uint16_t address, uint16_t length, void* data)
// {
//   Serial.print("FC=01/02: ");
//   Serial.println(fc);
//   Serial.println(address);
//   Serial.println(length);

//   for (int i = 0; i < length; i++)
//   {
//     int bt = 0;
//     if (i == 0)
//     {
//       bt = button_value;
//     }
//     slave.writeCoilToBuffer(i, bt);
//   }
//   return STATUS_OK;
// }

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
    digitalWrite(RELAY_DRIVER_1_PIN, slave.readCoilFromBuffer(0));
  }
  if (address == address_coil_2_zero_based)
  {
    digitalWrite(RELAY_DRIVER_2_PIN, slave.readCoilFromBuffer(0));
  }
  if (address == address_coil_3_zero_based)
  {
    digitalWrite(RELAY_DRIVER_3_PIN, slave.readCoilFromBuffer(0));
  }
  if (address == address_coil_4_zero_based)
  {
    digitalWrite(RELAY_DRIVER_4_PIN, slave.readCoilFromBuffer(0));
  }
  if (address == address_coil_5_zero_based)
  {
    digitalWrite(RELAY_DRIVER_5_PIN, slave.readCoilFromBuffer(0));
  }
  if (address == address_coil_6_zero_based)
  {
    digitalWrite(RELAY_DRIVER_6_PIN, slave.readCoilFromBuffer(0));
  }
  if (address == address_coil_7_zero_based)
  {
    digitalWrite(RELAY_DRIVER_7_PIN, slave.readCoilFromBuffer(0));
  }
  if (address == address_coil_8_zero_based)
  {
    digitalWrite(RELAY_DRIVER_8_PIN, slave.readCoilFromBuffer(0));
  }
  return STATUS_OK;
}
