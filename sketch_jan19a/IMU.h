#include <Arduino_LSM6DSOX.h>


/**
 * Test if IMU has new data available
 */
bool isIMUReady() {
  // if acceleration is not ready, abort
  if (!IMU.accelerationAvailable())
    return false;

  // await for gyroscope
  while (!IMU.gyroscopeAvailable())
    ;

  return true;
}


/**
 * Read IMU data
 */
void readIMU(float *ax, float *ay, float *az, float *gx, float *gy, float *gz) {
  IMU.readAcceleration(*ax, *ay, *az);
  IMU.readGyroscope(*gx, *gy, *gz);
}
