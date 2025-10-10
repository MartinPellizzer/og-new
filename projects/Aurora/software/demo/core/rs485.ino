// rs485_read
// rs485_read_timeout
// rs485_write

// rs485_receiver_buffer_debug
// rs485_receiver_buffer_cear

// rs485_sender_buffer_debug
// rs485_sender_buffer_cear

// rs485_manager

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
}

void rs485_receiver_buffer_debug()
{
  //DEBUG SERIAL
  Serial.print("RCV DATA: ");
  for (int i = 0; i < 9; i++)
  {
    Serial.print(rs485.receiver_buffer[i]);
    Serial.print(", ");
  }
  Serial.println();
  Serial.println();
}

void rs485_sender_buffer_debug()
{
  //DEBUG SERIAL
  Serial.print("SND DATA: ");
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
    Serial.println();
    modules[modules_i].online_cur = 0;
  }
}

void rs485_receiver_buffer_cear()
{
  for (int i = 0; i < 9; i++)
  {
    rs485.receiver_buffer[i] = 0;
  }
}

void rs485_sender_buffer_cear()
{
  for (int i = 0; i < 9; i++)
  {
    rs485.sender_buffer[i] = 0;
  }
}

int rs485_sender_buffer_ack()
{
  if (rs485.receiver_buffer[0] == 0xFF && 
      rs485.receiver_buffer[1] == 0xFF && 
      rs485.receiver_buffer[2] == 0xFF)
  {
    Serial.println("***********************************");
    Serial.println("OK: ACK VALID");
    Serial.println("***********************************");
    return 1;
  }
  return 0;
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
      
      rs485_write();
      rs485_sender_buffer_debug();
      rs485_sender_buffer_cear();
      rs485.state_transmission = 0;
      rs485.state_transmission_timer_millis = millis();
    }
  }

  if (rs485.state_transmission == 0)
  {
    rs485_read();
    if (rs485.receiver_buffer_ready == 1)
    {
      rs485_receiver_buffer_debug();
      int ack = rs485_sender_buffer_ack();
      if (ack == 1)
      {
        modules[modules_i].online_cur = 1;
        if (modules[modules_i].id == 1)
        {
          modules[modules_i].value_cur = rs485.receiver_buffer[3];
        }
      }
      rs485_receiver_buffer_cear();
      rs485.receiver_buffer_ready = 0;
      rs485.state_transmission = 1;

      Serial.println();
      Serial.println();
    }
    rs485_read_timeout();
  }
}