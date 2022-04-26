#! /usr/bin/env python
# -*- coding: utf8 -*-
import string
import time as py_time
import sys
from struct import unpack
import struct
import os
from struct import pack


def connection_aborted():
    pass


def connection_status():
    pass


def constant():
    pass


def define():
    pass


def defined():
    pass


def die(msg=""):
    exit(msg)


def get_browser():
    pass


def __halt_compiler():
    pass


def highlight_file():
    pass


def highlight_string():
    pass


def hrtime():
    pass


def ignore_user_abort():
    pass


def pack(format_codes, args):
    return struct.pack(format_codes, args)


def php_check_syntax():
    pass


def php_strip_whitespace():
    pass


def sapi_windows_cp_conv():
    pass


def sapi_windows_cp_get():
    pass


def sapi_windows_cp_is_utf8():
    pass


def sapi_windows_cp_set():
    pass


def sapi_windows_vt100_support():
    pass


def show_source():
    pass


def sleep(seconds):
    py_time.sleep(seconds)


def sys_getloadavg():
    return os.getloadavg()


def time_nanosleep(seconds, nanoseconds):
    pass


def time_sleep_until(timestamp):
    py_time.sleep(timestamp - py_time.time())


def uniqid(prefix=''):
    return prefix + hex(int(py_time.time()))[2:10] + hex(int(py_time.time() * 1000000) % 0x100000)[2:7]


def unpack(format_codes, data):
    return struct.unpack(format_codes, data)


def usleep(micro_seconds):
    py_time.sleep(micro_seconds / 1000000.0)
