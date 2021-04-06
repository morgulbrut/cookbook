#include <Arduino.h>

#include "TM1637.h"

// These constants won't change. They're used to give names to the pins used:
const int pot0Pin = A1;
const int pot1Pin = A2;

const int pwm0OutPin = 4;
const int pwm1OutPin = 5;

// 4-Digit display (for debug purposes)
const int CLK = 2; //pins definitions for TM1637 and can be changed to other ports
const int DIO = 3;
TM1637 tm1637(CLK, DIO);
int8_t TimeDisp[] = {0x00, 0x00, 0x00, 0x00};

int pot0 = 0;
int pot1 = 0;

void setup()
{
  // initialize serial communications at 9600 bps:
  Serial.begin(115200);
  analogReadResolution(8);

  tm1637.set();
  tm1637.init();
}

void loop()
{
  // read the analog in value:
  pot0 = analogRead(pot0Pin);
  pot1 = analogRead(pot1Pin);
  analogWrite(pwm0OutPin, pot0);
  analogWrite(pwm1OutPin, pot1);

  // print the results to the Serial Monitor:
  Serial.print("sensor = ");
  Serial.println(pot0);

  TimeDisp[0] = pot0 / 16;
  TimeDisp[1] = pot0 % 16;

  TimeDisp[2] = pot1 / 16;
  TimeDisp[3] = pot1 % 16;
  tm1637.display(TimeDisp);

  delay(100);
}