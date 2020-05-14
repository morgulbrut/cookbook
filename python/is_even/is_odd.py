#!/usr/bin/env python3

def is_odd(number):
    if isinstance(number, int):
        return number % 2 == 1
    else:
        raise TypeError("is_odd() needs an integer")
