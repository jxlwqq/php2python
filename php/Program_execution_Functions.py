#! /usr/bin/env python
# -*- coding: utf8 -*-
import re
import sys
import os


def escapeshellarg(arg):
    return "\\'".join("'" + p + "'" for p in arg.split("'"))


def escapeshellcmd():
    pass


def passthru():
    pass


def proc_lose():
    pass


def proc_et_tatus():
    pass


def proc_ice():
    pass


def proc_pen():
    pass


def proc_erminate():
    pass


def shell_xec(command):
    return os.popen(command).read()


def system(command):
    return os.system(command)
