void rs485_read()
{
  if (rs485.new_data_state)
  {
    if (millis() - rs485.new_data_timer > 40)
    {
      rs485.receiver_buffer_i = 0;
      rs485.new_data_state = 0;
      rs485.receiver_buffer_ready = 1;
    }
  }
  
  if (serial_rs485.available() > 0)  
  {
    uint8_t c = serial_rs485.read();
    rs485.receiver_buffer[rs485.receiver_buffer_i] = c;
    rs485.receiver_buffer_i++;
    rs485.new_data_state = 1;
    rs485.new_data_timer = millis();
  }
}

void rs485_write()
{
    digitalWrite(rs485.PIN_RE_DE, HIGH);
    for (int i = 0; i < 9; i++)
    {
      serial_rs485.write(rs485.sender_buffer[i]);
    }
    delay(10);
    digitalWrite(rs485.PIN_RE_DE, LOW);
    rs485.state_transmission = 0;
    rs485.state_transmission_timer_millis = millis();
}


void rs485_read_debug()
{
  //DEBUG SERIAL
  Serial.println("DATA RECEIVED");
  for (int i = 0; i < 9; i++)
  {
    Serial.print(rs485.receiver_buffer[i]);
    Serial.print(", ");
  }
  Serial.println();
  Serial.println();
}

void rs485_write_debug()
{
  //DEBUG SERIAL
  Serial.println("DATA RECEIVED");
  for (int i = 0; i < 9; i++)
  {
    Serial.print(rs485.sender_buffer[i]);
    Serial.print(", ");
  }
  Serial.println();
  Serial.println();
}

void rs485_read_timeout()
{
  if (millis() - rs485.state_transmission_timer_millis > 1000)
  {
    rs485.state_transmission = 1;
    Serial.println("***********************************");
    Serial.println("ERR: ACK TIMEOUT");
    Serial.println("***********************************");
    Serial.println();
    // modules[modules_i].online_cur = 0;
  }
}

void rs485_manager()
{
  if (rs485.state_transmission == 1)
  {
    rs485_write();
  }

  if (rs485.state_transmission == 0)
  {
    rs485_read();
    if (rs485.receiver_buffer_ready == 1)
    {
      rs485.receiver_buffer_ready = 0;
      rs485.state_transmission = 1;

      // TODO: CHECK ACK

      // rs485_read_debug();
      // modules[modules_i].online_cur = 1;
    }
    rs485_read_timeout();
  }
}