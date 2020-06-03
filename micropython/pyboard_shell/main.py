from pyb import CAN
from pyb import LED
from pyb import Pin
from pyb import DAC
from pyb import ADC
from array import array
import math
import sys
import time

PINS_IO = {
    "CH1": "A13",  # red LED
    "CH2": "A14",  # green LED
    "CH3": "A15",  # yello LED
    "CH4": "B4",  # blue LED

    "PIN1": "A13",
    "PIN2": "A14",
    "PIN3": "A15",
    "PIN4": "B4",
}

PINS_ADC = {
    "ADC1": "X1",
    "ADC2": "X2",
    "ADC3": "X3",
    "ADC4": "X4",
}

PINS_DAC = {
    "DAC1": "X5",
    "DAC2": "X6",
}


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
        return "set led{} to {}".format(led, value)
    except:
        return "error set_led"


def set_pin(pin, value):
    try:
        p_out = Pin(pin, Pin.OUT_PP)
        p_out.value(value)
        return "set pin {} to {}".format(pin, value)
    except:
        return "error set_pin"


def get_pin(pin):
    try:
        p_in = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        return "pin {} is {}".format(pin, p_in.value()
    except:
        return "error get_pin"


def set_analog(pin, value):
    try:
        dac=DAC(pin, bits=12)
        dac.write(value)
        return "set pin {} to {}".format(pin, value)
    except:
        return "error set_analog"


def read_analog(pin):
    try:
        adc=ADC(Pin(pin))
        return "pin {} is {}".format(pin, adc.read())
    except:
        return "error read_analog"


def sine(pin, freq):
    buf=array('H', 2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128))
    dac=DAC(pin, bits=12)
    dac.write_timed(buf, freq * len(buf), mode=DAC.CIRCULAR)


def main():
    while 1:
        x=input(">>> ")
        if x.lower() == "exit":
            break

        elif "select" in x.lower():
            if "CH1" in x.upper():
                res=set_led(1, 1)
                res += set_led(2, 0)
                res += set_led(3, 0)
                res += set_led(4, 0)
                res += set_pin(CH1, 1)
                res += set_pin(CH2, 0)
                res += set_pin(CH3, 0)
                res += set_pin(CH4, 0)
            elif "CH2" in x:
                res=set_led(1, 0)
                res += set_led(2, 1)
                res += set_led(3, 0)
                res += set_led(4, 0)
                res += set_pin(CH1, 0)
                res += set_pin(CH2, 1)
                res += set_pin(CH3, 0)
                res += set_pin(CH4, 0)
            elif "CH3" in x:
                res=set_led(1, 0)
                res += set_led(2, 0)
                res += set_led(3, 1)
                res += set_led(4, 0)
                res += set_pin(CH1, 0)
                res += set_pin(CH2, 0)
                res += set_pin(CH3, 1)
                res += set_pin(CH4, 0)
            elif "CH4" in x:
                res=set_led(1, 0)
                res += set_led(2, 0)
                res += set_led(3, 0)
                res += set_led(4, 1)
                res += set_pin(CH1, 0)
                res += set_pin(CH2, 0)
                res += set_pin(CH3, 0)
                res += set_pin(CH4, 1)
            if "error" in res:
                print("100 ERROR")
            else:
    time.sleep(0.02)


if __name__ == "__main__":
    main()
