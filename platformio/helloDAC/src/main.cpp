#include <Arduino.h>

#include <Wire.h>
#include <SeeedOLED.h>

// These constants won't change. They're used to give names to the pins used:
const int pot0Pin = A1;

const int adcOutPin = A0;

int pot0 = 0;

void setup()
{
  // initialize serial communications at 9600 bps:
  Serial.begin(115200);
  analogReadResolution(12);
  analogWriteResolution(12);

  Wire.begin();
  SeeedOled.init();
  SeeedOled.clearDisplay();     //clear the screen and set start position to top left corner
  SeeedOled.setNormalDisplay(); //Set display to Normal mode
  SeeedOled.setPageMode();      //Set addressing mode to Page Mode
}

void loop()
{
  // read the analog in value:
  pot0 = analogRead(pot0Pin);
  analogWrite(adcOutPin, pot0);

  // print the results to the Serial Monitor:
  Serial.print("sensor = ");
  Serial.println(pot0);

  SeeedOled.setTextXY(0, 0); //Set the cursor to 0th Page, 0th Column
  char output[4];
  sprintf(output, "%04d", pot0);
  SeeedOled.putString(output);
  delay(100);
}