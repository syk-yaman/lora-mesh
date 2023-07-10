#include "Wire.h"
#define SEN0562_LightSensorAddress 0x23                 //I2C Address 0x23
#define SHT31_TempHumiditySensorAddress 0x44

void setup()
{
  Serial.begin(9600);
  Wire.begin();
}
uint8_t buf[4] = {0};
uint16_t data, data1;

float Lux;
float Humidity;
float Temperature;

void loop()
{

  writeCommand(SHT31_SOFTRESET);
  
  readReg(SEN0562_LightSensorAddress, 0x10, buf, 2);              //Register Address 0x10
  data = buf[0] << 8 | buf[1];
  Lux = (((float)data )/1.2);
  Serial.print("LUX:");
  Serial.print(Lux);
  Serial.print("lx");
  Serial.print("\n");
  delay(500);
}
uint8_t readReg(uint8_t address, uint8_t reg, const void* pBuf, size_t size)
{
  if (pBuf == NULL) {
    Serial.println("pBuf ERROR!! : null pointer");
  }
  uint8_t * _pBuf = (uint8_t *)pBuf;
  Wire.beginTransmission(address);
  byte arr[] = {0x10};
  Wire.write(arr, 1);
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
