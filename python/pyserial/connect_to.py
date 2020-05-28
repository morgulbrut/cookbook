#!/usr/bin/env python3

import serial
from serial.tools.list_ports import comports


FTDI ='VID:PID=0403:6001'
CP2102='VID:PID=10C4:EA60'

if comports:
    print('Connecting to FTDI')
    for port, desc, hwid in sorted(comports()):
        if FTDI in hwid:
            print('found FTDI')
            with serial.Serial(port, 115200, timeout=1) as ser:
                ser.write(b'hello FTDI\n')
