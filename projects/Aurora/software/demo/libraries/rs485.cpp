#include "rs485.h"

void rs485_init(rs485_t *rs485)
{
  rs485->pin_re_de = 16;
  rs485->pin_tx = 17;
  rs485->pin_rx = 4;
  rs485->buffer_len = BUFFER_LEN;
  rs485->new_data_state = 0;
  rs485->new_data_timer = 0;
  rs485->sender_buffer[BUFFER_LEN] = {0};
  rs485->sender_buffer_i = 0;
  rs485->receiver_buffer[BUFFER_LEN] = {0};
  rs485->receiver_buffer_i = 0;
  rs485->receiver_buffer_ready = 0;
  rs485->state_transmission = 1;
  rs485->state_transmission_timer_millis = 0;
}

void rs485_read(rs485_t *rs485, HardwareSerial &serial_rs485)
{
  if (rs485->new_data_state)
  {
    if (millis() - rs485->new_data_timer > 40)
    {
      rs485->receiver_buffer_i = 0;
      rs485->new_data_state = 0;
      rs485->receiver_buffer_ready = 1;
    }
  }
  
  if (serial_rs485.available() > 0)  
  {
    uint8_t c = serial_rs485.read();
    rs485->receiver_buffer[rs485->receiver_buffer_i] = c;
    rs485->receiver_buffer_i++;
    rs485->new_data_state = 1;
    rs485->new_data_timer = millis();
  }
}

void rs485_write(rs485_t *rs485, HardwareSerial &serial_rs485)
{
    digitalWrite(rs485->pin_re_de, HIGH);
    for (int i = 0; i < rs485->buffer_len; i++)
    {
      serial_rs485.write(rs485->sender_buffer[i]);
    }
    delay(10);
    digitalWrite(rs485->pin_re_de, LOW);
}

int rs485_receiver_buffer_ack(rs485_t *rs485)
{
  if (rs485->receiver_buffer[0] == 0xFF && 
      rs485->receiver_buffer[1] == 0xFF && 
      rs485->receiver_buffer[2] == 0xFF)
  {
    return 1;
  }
  return 0;
}

void rs485_receiver_buffer_clear(rs485_t *rs485)
{
  for (int i = 0; i < rs485->buffer_len; i++)
  {
    rs485->receiver_buffer[i] = 0;
  }
}

void rs485_sender_buffer_clear(rs485_t *rs485)
{
  for (int i = 0; i < rs485->buffer_len; i++)
  {
    rs485->sender_buffer[i] = 0;
  }
}

void rs485_receiver_buffer_debug(rs485_t *rs485)
{
  Serial.print("RCV DATA: ");
  for (int i = 0; i < rs485->buffer_len; i++)
  {
    Serial.print(rs485->receiver_buffer[i]);
    Serial.print(", ");
  }
  Serial.println();
  Serial.println();
}

void rs485_sender_buffer_debug(rs485_t *rs485)
{
  Serial.print("SND DATA: ");
  for (int i = 0; i < rs485->buffer_len; i++)
  {
    Serial.print(rs485->sender_buffer[i]);
    Serial.print(", ");
  }
  Serial.println();
  Serial.println();
}

void rs485_read_timeout(rs485_t *rs485)
{
  if (millis() - rs485->state_transmission_timer_millis > 1000)
  {
    rs485->state_transmission = 1;
    rs485->read_timeout_cur = 1;
  }
}