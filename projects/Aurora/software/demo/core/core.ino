#include "rs485.h"

HardwareSerial serial_rs485(1);

rs485_t rs485 = {};

typedef struct module_t {
  int8_t id = 0;
  int8_t online_old = -2;
  int8_t online_cur = 0;
  int8_t identify_attempts = 0;
  int8_t value_old = -2;
  int8_t value_cur = 0;
} module_t;
module_t module_rele = { .id = 0 };
module_t module_sensor = { .id = 1 };
module_t module_sd = { .id = 2 };

int8_t modules_num = 3;
int8_t modules_i = 0;
module_t modules[3] = { module_rele, module_sensor, module_sd};

uint32_t timer_test = 0;

int8_t relay_state = 0;


uint32_t counter = 0;
int module_01_test_digit = 0;
uint32_t nextion_print_millis = 0;




void rs485_read_timeout(rs485_t *rs485, Stream &serial, module_t modules[], int8_t modules_i)
{
  if (millis() - rs485->state_transmission_timer_millis > 1000)
  {
    rs485->state_transmission = 1;
    serial.println("***********************************");
    serial.println("ERR: ACK TIMEOUT");
    serial.println("***********************************");
    serial.println();
    serial.println();
    modules[modules_i].online_cur = 0;
  }
}



void rs485_manager()
{
  if (rs485.state_transmission == 1)
  {
    if (millis() - timer_test > 1000)
    {
      timer_test = millis();
      modules_i += 1;
      modules_i %= modules_num;
      rs485.sender_buffer[0] = modules_i;
      if (modules_i == 0)
      {
        relay_state = !relay_state;
        rs485.sender_buffer[1] = relay_state;
      }
      if (modules_i == 1)
      {
        counter += 1;
        counter %= 10;
        rs485.sender_buffer[1] = counter;
      }
      if (modules_i == 2)
      {
        counter += 1;
        counter %= 10;
        rs485.sender_buffer[1] = counter;
      }
      
      rs485_write(&rs485, serial_rs485);
      rs485_sender_buffer_debug(&rs485);
      rs485_sender_buffer_cear(&rs485);
      rs485.state_transmission = 0;
      rs485.state_transmission_timer_millis = millis();
    }
  }

  if (rs485.state_transmission == 0)
  {
    rs485_read(&rs485, serial_rs485);
    if (rs485.receiver_buffer_ready == 1)
    {
      rs485_receiver_buffer_debug(&rs485);
      int ack = rs485_sender_buffer_ack(&rs485);
      if (ack == 1)
      {
        Serial.println("***********************************");
        Serial.println("OK: ACK VALID");
        Serial.println("***********************************");
        modules[modules_i].online_cur = 1;
        if (modules[modules_i].id == 1)
        {
          modules[modules_i].value_cur = rs485.receiver_buffer[3];
        }
      }
      rs485_receiver_buffer_cear(&rs485);
      rs485.receiver_buffer_ready = 0;
      rs485.state_transmission = 1;

      Serial.println();
      Serial.println();
    }
    rs485_read_timeout(&rs485, Serial, modules, modules_i);
  }
}

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  serial_rs485.begin(9600, SERIAL_8N1, rs485.pin_tx, rs485.pin_rx);
  pinMode(rs485.pin_re_de, OUTPUT);
  digitalWrite(rs485.pin_re_de, LOW);
  
  rs485_init(&rs485);
}

void nextion_print()
{
  if (millis() - nextion_print_millis > 1000)
  {
    nextion_print_millis = millis();
    for (int i = 0; i < modules_num; i++)
    {
      module_t module_cur = modules[i];
      if (module_cur.online_cur == 1)
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x4F, 0x44, 0x20, 0x30, 0x31, 0x3A, 0x20, 0x4F, 0x4E, 0x20, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff};
        _buffer[1] = (module_cur.id) + 0x30;
        _buffer[13] = (module_cur.id) + 0x30;
        _buffer[19] = (module_cur.value_cur % 100 / 10) + 0x30;
        _buffer[20] = (module_cur.value_cur % 10 / 1) + 0x30;
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
      if (module_cur.online_cur == 0)
      {
        uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x4F, 0x44, 0x20, 0x30, 0x31, 0x3A, 0x20, 0x2D, 0x2D, 0x22, 0xff, 0xff, 0xff};
        _buffer[1] = (module_cur.id) + 0x30;
        _buffer[13] = (module_cur.id) + 0x30;
        for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
        {
          Serial2.write(_buffer[i]);
        }
      }
    }
  }
}

void loop()
{
  rs485_manager();
  
  nextion_print();
}

