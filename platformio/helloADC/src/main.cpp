#include <Arduino.h>

// https://www.arduino.cc/reference/de/language/functions/zero-due-mkr-family/analogreadresolution/

const uint8_t ADC0 = A1;

void setup()
{
  // Öffne serielle Kommunikation
  Serial.begin(115200);
}

void loop()
{
  // Lesen des Eingangspins auf A0 mit der Standardauflösung (10 Bit)
  // und senden auf die serielle Schnittstelle
  analogReadResolution(10);
  Serial.print("ADC0 10-bit: ");
  Serial.print(analogRead(ADC0));

  // Ändern der Auflösung auf 12 Bit und lesen von A0
  analogReadResolution(12);
  Serial.print(", 12-bit: ");
  Serial.print(analogRead(ADC0));

  // Ändern der Auflösung auf 8 Bit und lesen von A0
  analogReadResolution(8);
  Serial.print(", 8-bit: ");
  Serial.println(analogRead(ADC0));

  // Eine kleine Verzögerung, um den seriellen Monitor nicht zu beeinträchtigen
  delay(100);
}