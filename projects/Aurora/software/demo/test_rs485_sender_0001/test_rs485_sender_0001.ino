#include <rs485.h>
HardwareSerial serial_rs485(1);
rs485_t rs485 = {};
// HardwareSerial Sender(1);


#define HEARTBEAT_PIN 13
uint32_t heartbeat_millis_cur = 0;


uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

uint32_t timer_test = 0;

#define RE_DE_PIN 16

enum Nextion_Pages {
  P_HOME,
};

typedef struct module_t {
  int8_t online_old = -2;
  int8_t online_cur = 0;
} module_t;
module_t module = {};


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


void heartbeat_manager()
{
  if (millis() - heartbeat_millis_cur > 1000)
  {
    heartbeat_millis_cur = millis();
    digitalWrite(HEARTBEAT_PIN, !(digitalRead(HEARTBEAT_PIN)));
  }
}

uint16_t modbusCRC(uint8_t *buffer, uint8_t length)
{
  uint16_t crc = 0xFFFF;

  for (uint8_t pos = 0; pos < length; pos++)
  {
    crc ^= (uint16_t)buffer[pos];

    for (int i = 0; i < 8; i++)
    {
      if (crc & 0x0001)
      {
        crc >>= 1;
        crc ^= 0xA001;
      }
      else
      {
        crc >>= 1;
      }
    }
  }

  return crc;
}

uint8_t relay_state = 0;
uint8_t relay_1_state = 0;
uint8_t relay_2_state = 0;
uint8_t relay_3_state = 0;
uint8_t relay_4_state = 0;

uint8_t txBuffer[8];   // 8 bytes for Write Single Coil

void buildModbusWriteCoil(int8_t module_address)
{
  // txBuffer[0] = 0x01;   // Slave Address
  // txBuffer[1] = 0x05;   // Function Code (Write Single Coil)
  // txBuffer[2] = 0x00;   // Coil Address High
  // txBuffer[3] = 0x00;   // Coil Address Low (Coil 0)
  // txBuffer[4] = 0xFF;   // Value High (ON)
  // txBuffer[5] = 0x00;   // Value Low  (ON)

  rs485.sender_buffer[0] = module_address;   // Slave Address
  rs485.sender_buffer[1] = 0x05;   // Function Code (Write Single Coil)
  rs485.sender_buffer[2] = 0x00;   // Coil Address High
  rs485.sender_buffer[3] = 0x00;   // Coil Address Low (Coil 0)

  if (module_address == 0x01) 
  {
    relay_1_state = !relay_1_state;
    relay_state = relay_1_state;
  }
  if (module_address == 0x02) 
  {
    relay_2_state = !relay_2_state;
    relay_state = relay_2_state;
  }
  if (module_address == 0x03) 
  {
    relay_3_state = !relay_3_state;
    relay_state = relay_3_state;
  }
  if (module_address == 0x04) 
  {
    relay_4_state = !relay_4_state;
    relay_state = relay_4_state;
  }

  if (relay_state == 0)
  {
    rs485.sender_buffer[4] = 0x00;   // Value High (ON)
    rs485.sender_buffer[5] = 0x00;   // Value Low  (ON)
  }
  else
  {
    rs485.sender_buffer[4] = 0xFF;   // Value High (ON)
    rs485.sender_buffer[5] = 0x00;   // Value Low  (ON)
  }

  // Calculate CRC for first 6 bytes
  uint16_t crc = modbusCRC(rs485.sender_buffer, 6);

  // Append CRC (LOW byte first!)
  rs485.sender_buffer[6] = crc & 0xFF;         // CRC Low
  rs485.sender_buffer[7] = (crc >> 8) & 0xFF;  // CRC High
}

void rs485_manager()
{
  // transmit
  if (rs485.state_transmission == 1)
  {
    if (millis() - timer_test > 100)
    {
      timer_test = millis();

      // buildModbusWriteCoil();
      if (rs485.sender_buffer[0] != 0x00)
      {
        rs485_write(&rs485, serial_rs485);
        rs485_sender_buffer_debug(&rs485);
        // rs485_sender_buffer_clear(&rs485);
        
        rs485.state_transmission = 0;
        rs485.state_transmission_timer_millis = millis();
      }
    }
  }
  // receive
  if (rs485.state_transmission == 0)
  {
    rs485_read(&rs485, serial_rs485);
    if (rs485.receiver_buffer_ready == 1)
    {
      Serial.println("***********************************");
      Serial.println("OK: ACK RECEIVED...");
      Serial.println("***********************************");
      
      // TODO: calculate crc
      // TODO: if write command:
      //        check if message echoed back from the module match the one sent
      //        if so, good - if not, check error message

      rs485_receiver_buffer_debug(&rs485);
      
      int ack = 0;
      if (
        rs485.sender_buffer[0] == rs485.receiver_buffer[0] &&
        rs485.sender_buffer[1] == rs485.receiver_buffer[1] &&
        rs485.sender_buffer[2] == rs485.receiver_buffer[2] &&
        rs485.sender_buffer[3] == rs485.receiver_buffer[3] &&
        rs485.sender_buffer[4] == rs485.receiver_buffer[4] &&
        rs485.sender_buffer[5] == rs485.receiver_buffer[5] &&
        rs485.sender_buffer[6] == rs485.receiver_buffer[6] &&
        rs485.sender_buffer[7] == rs485.receiver_buffer[7] 
      )
      {
        ack = 1;
      }
      else
      {
        ack = 0;
      }

      // int ack = rs485_receiver_buffer_ack(&rs485);
      if (ack == 1)
      {
        Serial.println("***********************************");
        Serial.println("OK: ACK VALID");
        Serial.println("***********************************");
        module.online_cur = 1;

        // modules[modules_i].online_cur = 1;
        // if (modules[modules_i].id == 1)
        // {
        //   modules[modules_i].value_cur = rs485.receiver_buffer[3];
        // }
      }
      else
      {
        module.online_cur = 0;
        Serial.println("***********************************");
        Serial.println("OK: ACK NOT VALID");
        Serial.println("***********************************");
      }
      rs485_receiver_buffer_clear(&rs485);
      rs485.receiver_buffer_ready = 0;
      rs485.state_transmission = 1;
      
        rs485_sender_buffer_clear(&rs485);

      Serial.println();
      Serial.println();
    }
    rs485_read_timeout(&rs485);
    if (rs485.read_timeout_cur == 1)
    {
      rs485.read_timeout_cur = 0;
      // modules[modules_i].online_cur = 0;
      module.online_cur = 0;
      Serial.println("***********************************");
      Serial.println("ERR: ACK TIMEOUT");
      Serial.println("***********************************");
      Serial.println();
      Serial.println();
      rs485_sender_buffer_clear(&rs485);
    }
  }
}

void setup() 
{
  Serial.begin(9600);
  
  pinMode(HEARTBEAT_PIN, OUTPUT);
  digitalWrite(HEARTBEAT_PIN, LOW);

  // Serial2.begin(9600, SERIAL_8N1, 27, 14);
  // Sender.begin(9600, SERIAL_8N1, 17, 4);
  // pinMode(RE_DE_PIN, OUTPUT);

  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  serial_rs485.begin(9600, SERIAL_8N1, rs485.pin_tx, rs485.pin_rx);
  pinMode(rs485.pin_re_de, OUTPUT);
  digitalWrite(rs485.pin_re_de, LOW);
  
  rs485_init(&rs485);
}


void loop() 
{
  rs485_manager();
  heartbeat_manager();
  nextion_manager();
}

