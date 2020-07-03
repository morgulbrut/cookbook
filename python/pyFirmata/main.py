#!/usr/bin/python3

import pyfirmata2
import time

PIN = 13  # Pin 13 is used
DELAY = 1  # 1 second delay

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0,
# On Windows: \\.\COM1, \\.\COM2
PORT = pyfirmata2.Arduino.AUTODETECT

# Creates a new board
board = pyfirmata2.Arduino(PORT)

print("setup servo on pin 9")
pin9 = board.get_pin('d:9:s')  # set up servo
pin9.write(255)
print(pin9.read())

print("read analog pin 0")
analog_0 = board.get_pin('a:0:i')  # read analog pin
print(analog_0.read())

print("set up pwm on pin 3")
pin3 = board.get_pin('d:3:p')
pin3.write(0.2)
print(pin3.read())

print("set up pwm on pin 13")
pin13 = board.get_pin('d:13:o')
pin13.write(1)
print(pin13.read())

time.sleep(10)
