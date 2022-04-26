#! /usr/bin/env python
# -*- coding: utf8 -*-
import datetime
import string
import time as py_time
import tzlocal


def checkdate(month, day, year):
    import datetime
    try:
        month, day, year = map(int, (month, day, year))
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False
    pass


def date_add():
    pass


def date_create_from_format():
    pass


def date_create_immutable_from_format():
    pass


def date_create_immutable():
    pass


def date_create():
    pass


def date_date_set():
    pass


def date_default_timezone_get():
    return tzlocal.get_localzone().zone


def date_default_timezone_set(timezone_identifier):
    pass


def date_diff():
    pass


def date_format():
    pass


def date_get_last_errors():
    pass


def date_interval_create_from_date_string():
    pass


def date_interval_format():
    pass


def date_isodate_set():
    pass


def date_modify():
    pass


def date_offset_get():
    pass


def date_parse_from_format():
    pass


def date_parse():
    pass


def date_sub():
    pass


def date_sun_info():
    pass


def date_sunrise():
    pass


def date_sunset():
    pass


def date_time_set():
    pass


def date_timestamp_get():
    pass


def date_timestamp_set():
    pass


def date_timezone_get():
    pass


def date_timezone_set():
    pass


def date(format, timestamp=None):
    if timestamp is None:
        timestamp = py_time.time()
    return py_time.strftime(format, timestamp)


def getdate(timestamp=None):
    if timestamp is None:
        timestamp = py_time.time()


def gettimeofday():
    pass


def gmdate():
    pass


def gmmktime():
    pass


def gmstrftime():
    pass


def idate():
    pass


def localtime(timestamp):
    return py_time.localtime(timestamp)


def microtime(get_as_float=False):
    d = datetime.now()
    t = py_time.mktime(d.timetuple())
    if get_as_float:
        return t
    else:
        ms = d.microsecond / 1000000.
        return '%f %d' % (ms, t)


def mktime(hour, minute, second, month, day, year):
    return py_time.mktime((year, month, day, hour, minute, second))


def strftime():
    pass


def strptime():
    pass


def strtotime():
    pass


def time():
    return int(py_time.time())


def timezone_abbreviations_list():
    pass


def timezone_identifiers_list():
    pass


def timezone_location_get():
    pass


def timezone_name_from_abbr():
    pass


def timezone_name_get():
    pass


def timezone_offset_get():
    pass


def timezone_open():
    pass


def timezone_transitions_get():
    pass


def timezone_version_get():
    pass
