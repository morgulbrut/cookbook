#!/usr/bin/env python3

import serial
from serial.tools.list_ports import comports

if comports:
    print('--- Available ports:')
    for port, desc, hwid in sorted(comports()):
        print('--- %-20s %s [%s]' % (port, desc, hwid))


