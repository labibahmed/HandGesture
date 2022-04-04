#include <Wire.h>

int f0,f1,f2,f3,f4;
bool isRecording = false;

long timer = 0;

const int MPU_ADDR = 0x68; // I2C address of the MPU-6050. If AD0 pin is set to HIGH, the I2C address will be 0x69.

int16_t accelerometer_x, accelerometer_y, accelerometer_z; // variables for accelerometer raw data
int16_t gyro_x, gyro_y, gyro_z; // variables for gyro raw data
int16_t temperature; // variables for temperature data

char tmp_str[7]; // temporary variable used in convert function

char* convert_int16_to_str(int16_t i) { // converts int16 to string. Moreover, resulting strings will have the same length in the debug monitor.
  sprintf(tmp_str, "%6d", i);
  return tmp_str;
}




void setup() {
  Serial.begin(9600);
  Wire.begin();
  Wire.beginTransmission(MPU_ADDR); // Begins a transmission to the I2C slave (GY-521 board)
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0); // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
}

void loop() {

//
//if (Serial.available()) {
//    String command = Serial.readStringUntil('\n');
//
//    Serial.print("Command: ");
//    Serial.println(command);
//
//    // if user sent "record", start recording
//    if (command.equals("record")) {
//      Serial.println("Start recording...");
//      isRecording = true;
//    }
//    // otherwise stop recording
//    else {
//      Serial.println("Stop recording...");
//      isRecording = false;
//    }
//  }
//  if (!isRecording)
//    return;
  
  if(millis() - timer > 1000){
  f0 = analogRead(A0);
  f1 = analogRead(A1);
  f2 = analogRead(A2);
  f3 = analogRead(A3);
  f4 = analogRead(A4);

  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H) [MPU-6000 and MPU-6050 Register Map and Descriptions Revision 4.2, p.40]
  Wire.endTransmission(false); // the parameter indicates that the Arduino will send a restart. As a result, the connection is kept active.
  Wire.requestFrom(MPU_ADDR, 7*2, true); // request a total of 7*2=14 registers
  
  // "Wire.read()<<8 | Wire.read();" means two registers are read and stored in the same variable
  accelerometer_x = Wire.read()<<8 | Wire.read(); // reading registers: 0x3B (ACCEL_XOUT_H) and 0x3C (ACCEL_XOUT_L)
  accelerometer_y = Wire.read()<<8 | Wire.read(); // reading registers: 0x3D (ACCEL_YOUT_H) and 0x3E (ACCEL_YOUT_L)
  accelerometer_z = Wire.read()<<8 | Wire.read(); // reading registers: 0x3F (ACCEL_ZOUT_H) and 0x40 (ACCEL_ZOUT_L)
  temperature = Wire.read()<<8 | Wire.read(); // reading registers: 0x41 (TEMP_OUT_H) and 0x42 (TEMP_OUT_L)
  gyro_x = Wire.read()<<8 | Wire.read(); // reading registers: 0x43 (GYRO_XOUT_H) and 0x44 (GYRO_XOUT_L)
  gyro_y = Wire.read()<<8 | Wire.read(); // reading registers: 0x45 (GYRO_YOUT_H) and 0x46 (GYRO_YOUT_L)
  gyro_z = Wire.read()<<8 | Wire.read(); // reading registers: 0x47 (GYRO_ZOUT_H) and 0x48 (GYRO_ZOUT_L)


  Serial.print(f0);
  Serial.print(",");
  Serial.print(f1);
  Serial.print(",");
  Serial.print(f2);
  Serial.print(",");
  Serial.print(f3);
  Serial.print(",");
  Serial.print(f4);
  Serial.print(",");
  Serial.print(convert_int16_to_str(accelerometer_x));
  Serial.print(",");
  Serial.print(convert_int16_to_str(accelerometer_y));
  Serial.print(",");
  Serial.print(convert_int16_to_str(accelerometer_z));
  Serial.print(",");
  Serial.print(convert_int16_to_str(gyro_x));
  Serial.print(",");
  Serial.print(convert_int16_to_str(gyro_y));
  Serial.print(",");
  Serial.println(convert_int16_to_str(gyro_z));

  delay(100);
    Serial.flush();
  }
  
}
