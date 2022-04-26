#! /usr/bin/env python
# -*- coding: utf8 -*-
import random
import math
import os


def acos(arg):
    return math.acos(arg)


def acosh(arg):
    return math.acosh(arg)


def asin(arg):
    return math.asin(arg)


def asinh(arg):
    return math.asinh(arg)


def atan2(y, x):
    return math.atan2(y, x)


def atan(arg):
    return math.atan(arg)


def atanh(arg):
    return math.atanh(arg)


def base_convert(number, from_base, to_base):
    try:
        base10 = int(number, from_base)
    except ValueError:
        raise

    if to_base < 2 or to_base > 36:
        raise NotImplementedError

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    sign = ''

    if base10 == 0:
        return '0'
    elif base10 < 0:
        sign = '-'
        base10 = -base10

    s = ''
    while base10 != 0:
        r = base10 % to_base
        r = int(r)
        s = digits[r] + s
        base10 //= to_base

    output_value = sign + s
    return output_value


def bindec(binary_string):
    return int(binary_string, 2)


def ceil(value):
    return math.ceil(value)


def cos(arg):
    return math.cos(arg)


def cosh(arg):
    return math.cosh(arg)


def decbin(number):
    return bin(number)


def dechex(number):
    return hex(number)


def decoct(number):
    return oct(number)


def deg2rad(number):
    return math.radians(number)


def exp(arg):
    return math.exp(arg)


def expm1(arg):
    return math.exp(arg) - 1


def floor(value):
    return math.floor(value)


def fmod(x, y):
    return math.fmod(x, y)


def getrandmax():
    pass


def hexdec(hex_string):
    return int(hex_string, 16)


def hypot(x, y):
    return math.hypot(x, y)


def intdiv(dividend, divisor):
    pass


def is_finite(val):
    return math.isfinite(val)


def is_infinite(val):
    return math.isinf(val)


def is_nan(val):
    return math.isnan(val)


def lcg_value():
    pass


def log10(arg):
    return math.log10(arg)


def log1p(arg):
    return math.log1p(arg)


def log(arg, base):
    return math.log(arg, base)


def mt_getrandmax():
    pass


def mt_rand(low, high):
    return random.randint(low, high)


def mt_srand():
    pass


def octdec(octal_string):
    return int(octal_string, 8)


def pi():
    return math.pi


def rad2deg(number):
    return math.degrees(number)


def rand(minint, maxint):
    return random.randint(minint, maxint)


def sin(arg):
    return math.sin(arg)


def sinh(arg):
    return math.sinh(arg)


def sqrt(arg):
    return math.sqrt(arg)


def srand(seed=None):
    if seed is None:
        return random.seed()
    return random.seed(seed)


def tan(arg):
    return math.tan(arg)


def tanh(arg):
    return math.tanh(arg)
