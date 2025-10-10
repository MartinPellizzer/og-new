String file_read(fs::FS &fs, const char * path)
{
  Serial.printf("Reading file: %s\n", path);
  File file = fs.open(path);
  if (!file)
  {
    Serial.println("Failed to open file for reading");
    return "-1";
  }
  Serial.print("Read from file: ");
  
  String content;
  while (file.available()) 
  {
    content += (char)file.read();
  }
  Serial.println(content);
  Serial.println();
  file.close();
  return content;
}

void file_write(fs::FS &fs, const char * path, const char * message)
{
  Serial.printf("Writing file: %s\n", path);
  File file = fs.open(path, FILE_WRITE);
  if (!file)
  {
    Serial.println("Failed to open file for writing");
    return;
  }
  if (file.print(message))
  {
    Serial.println("File written");
  } 
  else 
  {
    Serial.println("Write failed");
  }
  file.close();
}

void file_append(fs::FS &fs, const char *path, const char *message) 
{
  Serial.printf("Appending to file: %s\n", path);
  File file = fs.open(path, FILE_APPEND);
  if (!file)
  {
    Serial.println("Failed to open file for appending");
    return;
  }
  if (file.print(message))
  {
    Serial.println("Message appended");
  } 
  else 
  {
    Serial.println("Append failed");
  }
  file.close();
}