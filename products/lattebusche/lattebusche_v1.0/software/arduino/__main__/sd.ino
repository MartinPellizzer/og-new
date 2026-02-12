bool readLastRowAndSplit(fs::FS &fs, const char *path)
{
  File file = fs.open(path);
  if (!file) {
    Serial.println("Failed to open CSV file");
    return false;
  }

  char lineBuffer[MAX_LINE_LENGTH];
  int idx = 0;

  // Read entire file and keep overwriting lastRow
  while (file.available()) {
    char c = file.read();

    if (c == '\n') {
      lineBuffer[idx] = '\0';
      strncpy(lastRow, lineBuffer, MAX_LINE_LENGTH);
      idx = 0;
    }
    else if (c != '\r' && idx < MAX_LINE_LENGTH - 1) {
      lineBuffer[idx++] = c;
    }
  }

  // Handle file without trailing newline
  if (idx > 0) {
    lineBuffer[idx] = '\0';
    strncpy(lastRow, lineBuffer, MAX_LINE_LENGTH);
  }

  file.close();

  // -------- SPLIT BY COMMAS --------
  fieldCount = 0;

  char *token = strtok(lastRow, ",");
  while (token != NULL && fieldCount < MAX_FIELDS) {
    fields[fieldCount++] = token;
    token = strtok(NULL, ",");
  }

  return true;
}

void readFile(fs::FS &fs, const char * path){
  Serial.printf("Reading file: %s\n", path);

  File file = fs.open(path);
  if(!file){
    Serial.println("Failed to open file for reading");
    return;
  }

  Serial.print("Read from file: ");
  while(file.available()){
    Serial.write(file.read());
  }
  file.close();
}

void readLastCSVLines(fs::FS &fs, const char * path, int maxLines) {
  Serial.printf("Reading last %d lines from: %s\n", maxLines, path);

  File file = fs.open(path);
  if (!file) {
    Serial.println("Failed to open CSV file");
    return;
  }

  // Clear buffer
  for (int i = 0; i < maxLines; i++) {
    lastLines[i][0] = '\0';
  }
  lineCount = 0;

  char lineBuffer[MAX_LINE_LENGTH];
  int index = 0;

  while (file.available()) {
    char c = file.read();

    if (c == '\n' || index >= MAX_LINE_LENGTH - 1) {
      lineBuffer[index] = '\0';

      // Store line in rolling buffer
      strncpy(lastLines[lineCount % maxLines], lineBuffer, MAX_LINE_LENGTH);
      lastLines[lineCount % maxLines][MAX_LINE_LENGTH - 1] = '\0';

      lineCount++;
      index = 0;
    } else if (c != '\r') {
      lineBuffer[index++] = c;
    }
  }

  // Handle last line without newline
  if (index > 0) {
    lineBuffer[index] = '\0';
    strncpy(lastLines[lineCount % maxLines], lineBuffer, MAX_LINE_LENGTH);
    lastLines[lineCount % maxLines][MAX_LINE_LENGTH - 1] = '\0';
    lineCount++;
  }

  file.close();

  // Print last lines in correct order
  int start = max(0, lineCount - maxLines);
  Serial.println("---- Last CSV rows ----");
  for (int i = start; i < lineCount; i++) {
    Serial.println(lastLines[i % maxLines]);
  }
}

void readLastCSVLinesOrdered(fs::FS &fs, const char *path) {
  File file = fs.open(path);
  if (!file) {
    Serial.println("Failed to open CSV file");
    storedLines = 0;
    return;
  }

  storedLines = 0;
  char lineBuffer[MAX_LINE_LENGTH];
  int idx = 0;

  while (file.available()) {
    char c = file.read();

    if (c == '\n') {
      lineBuffer[idx] = '\0';

      if (storedLines < MAX_LINES) {
        // Still filling
        strncpy(lastLines[storedLines], lineBuffer, MAX_LINE_LENGTH);
        storedLines++;
      } else {
        // Shift everything up
        for (int i = 0; i < MAX_LINES - 1; i++) {
          strcpy(lastLines[i], lastLines[i + 1]);
        }
        strncpy(lastLines[MAX_LINES - 1], lineBuffer, MAX_LINE_LENGTH);
      }
      idx = 0;
    }
    else if (c != '\r' && idx < MAX_LINE_LENGTH - 1) {
      lineBuffer[idx++] = c;
    }
  }

  // Handle last line (no trailing newline)
  if (idx > 0) {
    lineBuffer[idx] = '\0';

    if (storedLines < MAX_LINES) {
      strncpy(lastLines[storedLines], lineBuffer, MAX_LINE_LENGTH);
      storedLines++;
    } else {
      for (int i = 0; i < MAX_LINES - 1; i++) {
        strcpy(lastLines[i], lastLines[i + 1]);
      }
      strncpy(lastLines[MAX_LINES - 1], lineBuffer, MAX_LINE_LENGTH);
    }
  }

  file.close();

  // Serial.println("---- Ordered last lines ----");
  // for (int i = 0; i < storedLines; i++) {
  //   Serial.println(lastLines[i]);
  // }
}

void update_hour_buff(uint16_t year, uint16_t month, uint16_t day, uint16_t hour, uint16_t minute)
{
    // Shift buffers down (start from bottom!)
    for (int i = LINES - 1; i > 0; i--)
    {
        for (int j = 0; j < LINE_SIZE; j++)
        {
            sd_hour_nextion_lines_buff[i][j] = sd_hour_nextion_lines_buff[i - 1][j];
        }
    }

    // Write new formatted string in position 0
    snprintf(sd_hour_nextion_lines_buff[0],
             LINE_SIZE,
             "%04u/%02u/%02u-%02u:%02u",
             year, month, day, hour, minute);

    // Extra safety (guarantee termination)
    sd_hour_nextion_lines_buff[0][LINE_SIZE - 1] = '\0';
}

void update_minute_buff(int err)
{
    // Shift buffers down (start from bottom!)
    for (int i = LINES - 1; i > 0; i--)
    {
        for (int j = 0; j < LINE_SIZE; j++)
        {
            sd_minute_nextion_lines_buff[i][j] = sd_minute_nextion_lines_buff[i - 1][j];
        }
    }

    // Write new formatted string in position 0
    int16_t ppb_cur = sensor.ppb_cur;
    if (ppb_cur < 0) ppb_cur = 0;
    snprintf(sd_minute_nextion_lines_buff[0],
            LINE_SIZE,
            "%01u|%04u/%02u/%02u %02u:%02u %04uppb",
            err, 
            rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur,
            ppb_cur
    );

    // Extra safety (guarantee termination)
    sd_minute_nextion_lines_buff[0][LINE_SIZE - 1] = '\0';
}

void sd_minute_line_cur_buff_write()
{
    int16_t ppb_cur = sensor.ppb_cur;
    if (ppb_cur < 0) ppb_cur = 0;
    snprintf(sd_minute_line_cur_buff,
            LINE_SIZE,
            "%04u/%02u/%02u %02u:%02u %04uppb",
            rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur,
            ppb_cur
    );

    // Extra safety (guarantee termination)
    sd_minute_line_cur_buff[LINE_SIZE - 1] = '\0';
}

void sd_minute_manager() 
{
  if (sd_card.buff_minute_old != sd_card.buff_minute_cur)
  {
    sd_card.buff_minute_old = sd_card.buff_minute_cur;

    // add sensor reading to hour buff
    sd_hour_buff[sd_hour_buff_i] = 123;
    sd_hour_buff_i += 1;

    sd_minute_line_cur_buff_write();
    
    if (sd_card.tried_to_initialize)
    {
      sd_card_write();
      if (readLastRowAndSplit(SD, "/data.csv")) 
      {

        Serial.println("Last row split values:");

        for (int i = 0; i < fieldCount; i++) 
        {
          Serial.print("Field ");
          Serial.print(i);
          Serial.print(": ");
          Serial.println(fields[i]);
        }

        {
          char _buff[LINE_SIZE] = {0};
          snprintf(_buff,
                LINE_SIZE,
                "%04u/%02u/%02u %02u:%02u %04uppb",
                atoi(fields[0]),
                atoi(fields[1]),
                atoi(fields[2]),
                atoi(fields[3]),
                atoi(fields[4]),
                atoi(fields[5])
          );
          Serial.println("OLD BUFFER:");
          Serial.println(sd_minute_line_cur_buff);
          Serial.println("NEW BUFFER:");
          Serial.println(_buff);

          if (strcmp(_buff, sd_minute_line_cur_buff) == 0) 
          {
              Serial.println("Buffers are identical");
              update_minute_buff(0);
          } else 
          {
              Serial.println("Buffers are different");
              update_minute_buff(3);
          }
        }
      }
      else
      {
        update_minute_buff(2);
      }
    }
    else
    {
      update_minute_buff(1);
    }

    for (int i = 0; i < LINES; i++)
    {
      Serial.println(sd_minute_nextion_lines_buff[i]);
    }
    Serial.println();

    sd_card.nextion_update = 1;
  }
}

void sd_hour_manager() 
{
  if (sd_card.buff_hour_old != sd_card.buff_hour_cur)
  {
    sd_card.buff_hour_old = sd_card.buff_hour_cur;

    update_hour_buff(rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur);

    for (int i = 0; i < LINES; i++)
    {
        Serial.println(sd_hour_nextion_lines_buff[i]);
    }
    Serial.println();

    sd_card.nextion_update = 1;
  }
}

void sd_card_init() 
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
      Serial.println("Card Unmounted");
    }
  }
}

void sd_card_write() 
{
  Serial.printf("Appending to file: %s\n", "/data.csv");
  file = SD.open("/data.csv", FILE_APPEND);
  if (!file)
  {
    Serial.println("Failed to open file for appending");
  }
  else
  {
    char _buff[LINE_SIZE] = {0};
    int16_t ppb_cur = sensor.ppb_cur;
    if (ppb_cur < 0) ppb_cur = 0;
    snprintf(_buff,
            LINE_SIZE,
            "%04u,%02u,%02u,%02u,%02u,%04u\n",
            rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur,
            ppb_cur
    );
    file.print(_buff);
    file.close();
  }
}

void sd_manager() 
{
  sd_card_init();
  
  sd_minute_manager();
  sd_hour_manager();
}