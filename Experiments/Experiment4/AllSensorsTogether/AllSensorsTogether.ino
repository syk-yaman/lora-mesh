#include "Wire.h"
               //I2C Address 0x23
uint8_t SHT31_TempHumiditySensorAddress = 0x44;
uint8_t SEN0562_LightSensorAddress = 0x23;

//SHT31 commands
#define SHT31_MEAS_HIGHREP_0 0x24 //MSB
#define SHT31_MEAS_HIGHREP_1 0x00 //LSB

void setup()
{
  Serial.begin(9600);
  Wire.begin();
}
//Light
uint8_t buf[4] = {0};
uint16_t data, data1;
float Lux;

//Humidity


void loop()
{
  //////////////// Light Sensor Section
  uint8_t readbuffer[6];  
  uint8_t command = SHT31_MEAS_HIGHREP_0; // MSB section of the command - see datasheet
  uint8_t command2 = SHT31_MEAS_HIGHREP_1; // LSB section of the command - see datasheet


  Wire.beginTransmission(SHT31_TempHumiditySensorAddress);
  Wire.write(&command, 1);
  Wire.write(&command2, 1);
  
  if ( Wire.endTransmission() != 0) {
    return 0;
  }
  delay(20);
  Wire.requestFrom(SHT31_TempHumiditySensorAddress, sizeof(readbuffer));
  for (uint16_t i = 0; i < sizeof(readbuffer); i++) {
    readbuffer[i] = Wire.read();
  }
  
  int32_t stemp = (int32_t)(((uint32_t)readbuffer[0] << 8) | readbuffer[1]); //readbuffer[2] is CRC, ignored for now
  stemp = ((4375 * stemp) >> 14) - 4500;
  float temp = (float)stemp / 100.0f;

  uint32_t shum = ((uint32_t)readbuffer[3] << 8) | readbuffer[4]; //readbuffer[5] is CRC, ignored for now
  shum = (625 * shum) >> 12;
  float humidity = (float)shum / 100.0f;

  Serial.print("temp:");
  Serial.print(temp);
  Serial.print("\n");
  Serial.print("humidity:");
  Serial.print(humidity);
  Serial.print("\n");
  
  Wire.endTransmission();
  
  //////////////// Light Sensor Section
  delay(500);
  readReg(SEN0562_LightSensorAddress, 0x10, buf, 2);              //Register Address 0x10
  data = buf[0] << 8 | buf[1];
  Lux = (((float)data )/1.2);
  Serial.print("LUX:");
  Serial.print(Lux);
  Serial.print("lx");
  Serial.print("\n");
  Wire.endTransmission();
  delay(500);

  
}

uint8_t readReg(uint8_t address, uint8_t reg, const void* pBuf, size_t size)
{
  if (pBuf == NULL) {
    Serial.println("pBuf ERROR!! : null pointer");
  }
  uint8_t * _pBuf = (uint8_t *)pBuf;
  Wire.beginTransmission(address);
  Wire.write(&reg, 1);
  if ( Wire.endTransmission() != 0) {
    return 0;
  }
  delay(20);
  Wire.requestFrom(address, (uint8_t) size);
  for (uint16_t i = 0; i < size; i++) {
    _pBuf[i] = Wire.read();
  }
  return size;
}
