void sd_manager_2() 
{
  sd_card_init_2();
  sd_card_write_2();
}

void sd_card_init_2() 
{
  sd_card.inserted_cur = (digitalRead(sd_card.pin_cd) == LOW) ? 1 : 0;

  if (sd_card.inserted_cur)
  {
    if (!sd_card.tried_to_initialize)
    {
      sd_card.tried_to_initialize = 1;
      if (!SD.begin()) Serial.println("Card Mount Failed");
      else Serial.println("Card Mounted");
    }
  }
  else
  {
    if (sd_card.tried_to_initialize)
    {
      SD.end();
      sd_card.tried_to_initialize = 0;
      Serial.println("Card Unounted");
    }
  }
}

void sd_card_write_2() 
{
  if (sd_card.minute_cur != rtc.minute_cur)
  {
    sd_card.minute_cur = rtc.minute_cur;
    if (sd_card.tried_to_initialize)
    {
      Serial.printf("Appending to file: %s\n", "/data.csv");
      file = SD.open("/data.csv", FILE_APPEND);
      if (!file) Serial.println("Failed to open file for appending");
      if (file.print(String(rtc.year_cur))) Serial.println("Message 1 appended");
      if (file.print(String(","))) Serial.println("Message 2 appended");
      if (file.print(String(rtc.month_cur))) Serial.println("Message 3 appended");
      if (file.print(String(","))) Serial.println("Message 4 appended");
      if (file.print(String(rtc.day_cur))) Serial.println("Message 5 appended");
      if (file.print(String(","))) Serial.println("Message 6 appended");
      if (file.print(String(rtc.hour_cur))) Serial.println("Message 7 appended");
      if (file.print(String(","))) Serial.println("Message 8 appended");
      if (file.print(String(rtc.minute_cur))) Serial.println("Message 9 appended");
      if (file.print(String(","))) Serial.println("Message 10 appended");
      if (file.print(String(rtc.second_cur))) Serial.println("Message 11 appended");
      if (file.print(String(","))) Serial.println("Message 12 appended");
      if (file.print(String(sensor.ppb_curr))) Serial.println("Message 13 appended");
      if (file.print('\n')) Serial.println("Message appended");
      file.close();
    }
  }
}

void sd_manager() 
{
  sd_card_init();
  sd_write_sensor_val_every_minute();
}

void sd_card_init() 
{
  sd_card.inserted_cur = (digitalRead(sd_card.pin_cd) == LOW) ? 1 : 0;

  if (sd_card.inserted_cur) 
  {
    if (!sd_card.tried_to_initialize) 
    {
      sd_card.tried_to_initialize = 1;
      // if (SD.begin(sd_card.pin)) sd_card.state = 1;
      if (SD.begin()) 
      {
        sd_card.state = 1;
        Serial.println("SD INIT: OK");
      }
      else 
      {
        sd_card.state = 0;
        Serial.println("SD INIT: FAIL");
      }
    }
  } 
  else 
  {
    if (sd_card.state == 1) 
    {
      sd_card.state = 0;
      sd_card.tried_to_initialize = 0;
    }
  }
}

void sd_card_write()
{
  if (sd_card.state == 1)
  {
    Serial.println("SD card in");
    // file = SD.open("data.csv", FILE_WRITE);
    
    char char_arr[2];
    sprintf(char_arr, "%d", rtc.second_cur);
    appendFile(SD, "/seconds.csv", char_arr);

    // File file = SD.open("data-2.csv", FILE_APPEND);
    // if (!file) {
    //   Serial.println("Failed to open file for appending");
    // }
    
    // if (file.print(String(rtc.second_cur))) 
    // {
    //   Serial.println(String(rtc.second_cur));
    // }
    // else
    // {
    //   Serial.print("Append failed: ");
    //   Serial.println(String(rtc.second_cur));
    // }

    // if (file.write('\n'))
    // {
    //   Serial.println("-n");
    // }
    // else
    // {
    //   Serial.print("Append failed: ");
    //   Serial.println("-n");
    // }
    
    // file.print(String(rtc.year));
    // file.write(',');
    // file.print(String(rtc.month));
    // file.write(',');
    // file.print(String(rtc.day));
    // file.write(',');
    // file.print(String(rtc.hour));
    // file.write(',');
    // file.print(String(rtc.minute));
    // file.write(',');
    // file.print(String(rtc.second));
    // file.write(',');
    // file.print(String(sensor.ppb()));
    // file.write(',');
    // file.write('\n');

    // file.close();
  }
  else
  {
    Serial.println("SD card not inserted");
  }
}

void sd_write_sensor_val_every_minute()
{
  if (millis() - sd_millis_cur >= 1000)
  {
    sd_millis_cur = millis();

    sd_card_write();
  }
}


void appendFile(fs::FS &fs, const char *path, const char *message) 
{
  Serial.printf("Appending to file: %s\n", path);

  file = fs.open(path, FILE_APPEND);
  if (!file) {
    Serial.println("Failed to open file for appending");
    return;
  }
  if (file.print(message)) {
    Serial.println("Message appended");
  } else {
    Serial.println("Append failed");
  }
  file.close();
}