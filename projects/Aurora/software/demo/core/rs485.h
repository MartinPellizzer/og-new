#ifndef RS485_H
#define RS485_H

#include <Arduino.h>

/* default rs485 pins
#define PIN_RE_DE 16
#define PIN_TX 17
#define PIN_RX 4
*/
#define BUFFER_LEN 9

typedef struct rs485_t {
  uint8_t pin_re_de = 16;
  uint8_t pin_tx = 17;
  uint8_t pin_rx = 4;
  uint8_t buffer_len = BUFFER_LEN;
  uint32_t new_data_state = 0;
  uint32_t new_data_timer = 0;
  uint8_t sender_buffer[BUFFER_LEN] = {0};
  uint8_t sender_buffer_i = 0;
  uint8_t receiver_buffer[BUFFER_LEN] = {0};
  uint8_t receiver_buffer_i = 0;
  uint8_t receiver_buffer_ready = 0;
  int8_t state_transmission = 1;
  uint32_t state_transmission_timer_millis = 0;
} rs485_t;

void rs485_init(rs485_t *rs485);

void rs485_read(rs485_t *rs485, HardwareSerial &serial_rs485);
void rs485_write(rs485_t *rs485, HardwareSerial &serial_rs485);

int rs485_sender_buffer_ack(rs485_t *rs485);

void rs485_receiver_buffer_cear(rs485_t *rs485);
void rs485_sender_buffer_cear(rs485_t *rs485);

void rs485_receiver_buffer_debug(rs485_t *rs485);
void rs485_sender_buffer_debug(rs485_t *rs485);



#endif