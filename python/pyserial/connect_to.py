#!/usr/bin/env python3

import serial
from serial.tools.list_ports import comports
import time

FTDI = 'VID:PID=0403:6001'
CP2102 = 'VID:PID=10C4:EA60'
PYBOARD = 'VID:PID=F055:9800'


if comports:
    for port, desc, hwid in sorted(comports()):
        if FTDI in hwid:
            print('found FTDI on {}'.format(port))
            with serial.Serial(port, 115200, timeout=1) as ser:
                ser.write(b'hello FTDI\n')
        if PYBOARD in hwid:
            print('found PYBPOARD on {}'.format(port))
            with serial.Serial(port, 115200, timeout=1) as ser:
                ser.write(b'set_led(1,1)\r\n')
                ser.readline()
                print(ser.readline())
                time.sleep(1)
                ser.write(b'set_led(1,0)\r\n')
                ser.readline()
                print(ser.readline())
