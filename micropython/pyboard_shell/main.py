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


def set_pin(pin, value):
    try:
        return (0, "set pin: {} : {}".format(pin.name(), value))
    except:
        return (1, "set_pin")


def get_pin(pin):
    try:
        return (0, "pin: {} : {}".format(pin.name(), pin.value()))
    except:
        return (1, "get_pin")


def set_analog(pin, value):
    try:
        dac=DAC(pin, bits=12)
        dac.write(value)
        return (0, "set dac : : {}".format(value))
    except:
        return (1, "set_analog")


def read_analog(pin):
    try:
        return (0, "pin: : {}".format(pin.read()))
    except:
        return (1, "read_analog")


def sine(pin, freq):
    buf=array('H', 2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128))
    dac=DAC(pin, bits=12)
    dac.write_timed(buf, freq * len(buf), mode=DAC.CIRCULAR)


def print_help():
    print("===================")
    print("        HELP       ")
    print("===================")
    print("Commands:")
    print("exit             - exit the shell")
    print("help             - showing this help")
    print("select <CH>      - select channel CH1 to CH4, ALL or NONE")
    print("set <PIN>        - set PIN1 to PIN4 to 1")
    print("reset <PIN>      - reset PIN1 to PIN4 to low")
    print("read <ADC>       - read an analog value from ADC1 to ADC4")
    print("read <PIN>       - read 0 or 1 from PIN1 to PIN4")
    print("write <DAC>      - write an analog value to DAC1 or DAC2")
    print("write <PIN>      - write 0 or 1 to PIN1 to PIN4")


def main():

    pnsio = {}
    for p in PINS_IO:
        pnsio[p] = Pin(PINS_IO[p], Pin.PULL_UP)

    adci = {}
    for p in PINS_ADC:
        adci[p] = ADC(Pin(PINS_ADC[p]))

    daco = {}
    for p in PINS_DAC:
        daco[p] = DAC(PINS_DAC[p], bits=12)

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
