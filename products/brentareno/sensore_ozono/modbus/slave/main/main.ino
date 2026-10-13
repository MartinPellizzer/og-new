// SLAVE

HardwareSerial rs485_serial(1);
uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

#define RE_DE_PIN 16

#include <ModbusSlave.h>
Modbus slave(rs485_serial, 23, RE_DE_PIN);

#define LED_PIN 13

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

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  rs485_serial.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // slave.cbVector[CB_WRITE_COILS] = writeDigitalOut;
  // slave.cbVector[CB_READ_COILS] = readDigital;
  slave.cbVector[CB_READ_INPUT_REGISTERS] = readAnalogIn;

  slave.begin(9600);
}


void loop() 
{
  slave.poll();

  if (millis() - sensor.timeout_timer_cur > 5000) 
  {
    // if (sensor.timeout_error == 0)
    {
      // sensor.timeout_error = 1;
      sensor.ppb_cur = 10001;
    }
  }

  ze27o3_listen();

  if (ze27o3_ready())
  {
    sensor.buff_i = 0;
    sensor.buff_ready = 0;

    // CHECKSUM
    if (ze27o3_checksum_valid())
    {
      Serial.println("CHECKSUM: VALID");
      sensor.ppb_cur = ze27o3_ppb_get();

      sensor.timeout_timer_cur = millis();
      // sensor.timeout_error = 0;
    }
    else
    {
      Serial.println("CHECKSUM: ERROR");
    }

    ze27o3_debug();
  }
}

uint8_t readAnalogIn(uint8_t fc, uint16_t address, uint16_t length, void* data)
{
    Serial.printf(
        "FC=%u, Address=%u, Length=%u -> ",
        fc, address, length
    );

    if (length == 1)
    {
      if (address == 0 || address == 30001)
      {
          Serial.println("MATCH");
          slave.writeRegisterToBuffer(0, sensor.ppb_cur);
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

// uint8_t writeDigitalOut(uint8_t fc, uint16_t address, uint16_t length, void* data)
// {
//   Serial.print("FC=05: ");
//   Serial.println(fc);
//   Serial.println(address);
//   Serial.println(length);

//   if (address == 12)
//   {
//     digitalWrite(LED_PIN, slave.readCoilFromBuffer(0));
//   }
//   return STATUS_OK;
// }
