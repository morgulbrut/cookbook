from pyb import CAN
from pyb import LED
from pyb import Pin
from pyb import DAC
from pyb import ADC
from array import array
import math
import sys


def CAN_test():
    can = CAN(1, CAN.LOOPBACK)
    # set a filter to receive messages with id=123, 124, 125 and 126
    can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))
    can.send('ping!', 123)   # send a message with id 123
    print(can.recv(0))

    can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))
    can.send(str(123), 123)   # send a message with id 123
    print(can.recv(0))


def set_led(led, value):
    try:
        l = LED(led)
        if value == 0:
            l.off()
        else:
            l.on()
        print("set led{} to {}".format(led, value))
    except:
        print("error set_led")


def set_pin(pin, value):
    try:
        p_out = Pin(pin, Pin.OUT_PP)
        p_out.value(value)
    except:
        print("error set_pin")


def get_pin(pin):
    try:
        p_in = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        print(p_in.value())
    except:
        print("error get_pin")


def set_analog(pin, value):
    try:
        dac = DAC(pin, bits=12)
        dac.write(value)
    except:
        print("error set_analog")


def read_analog(pin):
    try:
        adc = ADC(Pin(pin))
        adc.read()
    except:
        print("error read_analog")


def sine(pin, freq):
    buf = array('H', 2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128))
    dac = DAC(pin, bits=12)
    dac.write_timed(buf, freq * len(buf), mode=DAC.CIRCULAR)
