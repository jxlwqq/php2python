#! /usr/bin/env python
# -*- coding: utf8 -*-

from collections import Counter
import random
from functools import reduce
import hashlib
import locale
import csv
import io
import re
import math
import time as py_time
import datetime
import binascii
import urllib.parse
import urllib.request
from itertools import takewhile
import numbers
import pickle
import pprint
import base64
import os
import struct
import sys
import glob as py_glob
import inspect
import textwrap
import crypt as py_crypt
import quopri
import string
import syslog as py_syslog
import fcntl
import fnmatch as py_fnmatch
import shutil
import collections
from socket import inet_ntoa
from socket import inet_aton
import socket
from struct import pack
from struct import unpack
import http.cookies
import codecs

import tzlocal

"""
Array Functions
"""


def array_change_key_case(array, case=0):
    if case == 0:
        f = str.lower
    elif case == 1:
        f = str.upper
    else:
        raise ValueError()
    return dict((f(k), v) for k, v in array.items())


def array_chunk(array, size):
    return [array[i: i + size] for i in range(0, len(array), size)]


def array_column(array, column_key, index_key=None):
    if index_key is None:
        return [item.get(column_key) for item in array]
    else:
        res = {}
        for item in array:
            res[item.get(index_key)] = item.get(column_key)
        return res


def array_combine(keys, values):
    return dict(zip(keys, values))


def array_count_values(array):
    return Counter(array)


def array_diff_assoc():
    pass


def array_diff_key():
    pass


def array_diff_uassoc():
    pass


def array_diff_ukey():
    pass


def array_diff(array1, array2):
    return list(set(array1).difference(array2))


def array_fill_keys(keys, value):
    return dict.fromkeys(keys, value)


def array_fill(start_index, num, value):
    if start_index >= 0:
        keys = range(start_index, num + start_index)
    else:
        keys = [start_index] + list(range(0, num - 1))
    return array_fill_keys(keys, value)


def array_filter(array, callback=None):
    filter(callback, array)


def array_flip(array):
    return dict((v, k) for k, v in array.items())


def array_intersect_assoc(array1, array2):
    pass


def array_intersect_key(array1, *arrays):
    keys = array1.viewkeys()
    for array in arrays:
        keys &= array.viewkeys()
    return {k: array1[k] for k in keys}


def array_intersect_uassoc(array1, array2, callback):
    pass


def array_intersect_ukey(array1, array2, callback):
    pass


def array_intersect(array1, array2):
    pass


def array_key_exists(key, array):
    return key in array


def array_key_first(array):
    return array.keys[0]


def array_key_last(array):
    return array.keys[-1]


def array_keys(array, search_value=None):
    if search_value is None:
        return array.keys()
    else:
        return [k for k, v in array.items() if v == search_value]


def array_map(callback, array):
    return map(callback, array)


def array_merge_recursive(array1, *arrays):
    for array in arrays:
        for key, value in array.items():
            if key in array1:
                if isinstance(value, dict):
                    array[key] = array_merge_recursive(array1[key], value)
                if isinstance(value, (list, tuple)):
                    array[key] += array1[key]
        array1.update(array)
    return array1


def array_merge(array1, array2):
    if isinstance(array1, list) and isinstance(array2, list):
        return array1 + array2
    elif isinstance(array1, dict) and isinstance(array2, dict):
        return dict(list(array1.items()) + list(array2.items()))
    elif isinstance(array1, set) and isinstance(array2, set):
        return array1.union(array2)
    return False


def array_multisort(array):
    return sorted(array, key=lambda x: (x[1], x[2]))


def array_pad(array, size, value):
    if size >= 0:
        return array + [value] * (size - len(array))
    else:
        return [value] * (-size - len(array)) + array


def array_pop(array):
    return array.pop()


def array_product(array):
    if not array:
        return 0
    else:
        reduce(lambda a, b: a * b, array)


def array_push(array, *values):
    for value in values:
        array.extend(value)


def array_rand(array, num=1):
    if num == 1:
        return random.choice(array.keys())
    else:
        return random.sample(array.keys(), num)


def array_reduce(array, callback, initial=None):
    if initial is None:
        return reduce(callback, array)
    else:
        return reduce(function, array, initial)


def array_replace_recursive():
    pass


def array_replace():
    pass


def array_reverse(array):
    return array[::-1]


def array_search(needle, haystack, strict=False):
    pass


def array_shift(array):
    return array.pop(0)


def array_slice(array, offset, length=None):
    if is_array(array) and not isinstance(array, dict):
        if isinstance(array, set):
            array = list(array)
            return set(array[offset:length])
        return array[offset:length]
    return False


def array_splice(array, offset, length, replacement=None):
    if replacement is None:
        del array[offset: offset + length]
    else:
        array[offset: offset + length] = replacement
    return array


def array_sum(array):
    return sum(array)


def array_udiff_assoc(array):
    pass


def array_udiff_uassoc(array):
    pass


def array_udiff(array):
    pass


def array_uintersect_assoc(array):
    pass


def array_uintersect_uassoc(array):
    pass


def array_uintersect(array):
    pass


def array_unique(array):
    return list(set(array))


def array_unshift(array, *args):
    for i in reversed(args):
        array.insert(0, i)
    return array


def array_values(array):
    return array.values()


def array_walk_recursive(array):
    pass


def array_walk(array, callback):
    for k, val in array.items():
        callback(val, k)


def array(array):
    pass


def arsort(array):
    return sorted(array.items(), key=lambda x: x[1], reverse=True)


def asort(array):
    return sorted(array.items(), key=lambda x: x[1])


def compact(*names):
    caller = inspect.stack()[1][0]
    vars = {}
    for n in names:
        if n in caller.f_locals:
            vars[n] = caller.f_locals[n]
        elif n in caller.f_globals:
            vars[n] = caller.f_globals[n]
    return vars


def count(array):
    return len(array)


def current(array):
    pass


def each(array):
    pass


def end(array):
    return array[-1]


def extract(array):
    pass


def in_array(needle, haystack):
    return needle in haystack


def key_exists(key, array):
    return array_key_exists(key, array)


def key(array):
    pass


def krsort(array):
    return [(k, array[k]) for k in sorted(array.keys(), reverse=True)]


def ksort(array):
    return [(k, array[k]) for k in sorted(array.keys())]


def natcasesort(array):
    pass


def natsort(array):
    pass


def pos(array):
    pass


def prev(array):
    pass


def reset(array):
    pass


def rsort(array):
    return array.sort(reverse=True)


def shuffle(array):
    return random.shuffle(array)


def sizeof(array):
    return len(array)


def sort(array):
    return array.sort()


def uasort(array):
    pass


def uksort(array):
    pass


def usort(array):
    pass


"""
Date/Time Functions
"""


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


'''
Filesystem Functions
'''


def basename(path, suffix=None):
    base_name = os.path.basename(path)
    if suffix is not None and basename.endswith(suffix):
        return base_name[:-len(suffix)]
    return base_name


def chgrp(filename, group):
    return os.chown(filename, None, group)


def chmod(filename, mode):
    return os.chmod(filename, mode)


def chown(filename, user):
    return os.chown(filename, user, None)


def clearstatcache():
    pass


def copy(source, dest):
    return shutil.copy(source, dest)


def delete(filename):
    return unlink(filename)


def dirname(path):
    return os.path.dirname(path.rstrip(os.pathsep)) or '.'


def disk_free_space():
    pass


def disk_total_space():
    pass


def diskfreespace():
    pass


def fclose():
    pass


def feof():
    pass


def fflush(handle):
    return handle.flush()


def fgetc():
    pass


def fgetcsv():
    pass


def fgets():
    pass


def fgetss():
    pass


def file_exists(path):
    return os.path.exists(path)


def file_get_contents():
    pass


def file_put_contents(filename, mode, data):
    file = open(filename, mode)
    file.write(data)
    file.close()


def file():
    pass


def fileatime(filename):
    return os.path.getatime(filename)


def filectime(filename):
    return os.path.getctime(filename)


def filegroup(filename):
    return os.stat(filename).st_gid


def fileinode(filename):
    return os.stat(filename).st_ino


def filemtime(filename):
    return os.path.getmtime(filename)


def fileowner(filename):
    return os.stat(filename).st_uid


def fileperms(filename):
    return os.stat(filename).st_mode


def filesize(filename):
    return os.path.getsize(filename)


def filetype():
    pass


def flock(handle, operation):
    return fcntl.flock(handle, operation)


def fnmatch(filename, pattern):
    return py_fnmatch.fnmatch(filename, pattern)


def fopen():
    pass


def fpassthru():
    pass


def fputcsv():
    pass


def fputs():
    pass


def fread(handle, length):
    f = open(handle, "r+")
    return f.read(length)


def fscanf():
    pass


def fseek(handle, offset, whence=0):
    # SEEK_SET=0
    # SEEK_CUR=1
    # SEEK_END=2
    return handle.seek(offset, whence)


def fstat(handle):
    os.fstat(handle)


def ftell(handle):
    return handle.tell()


def ftruncate(handle, size):
    return handle.truncate(size)


def fwrite():
    pass


def glob(pattern):
    return py_glob.glob(pattern)


def is_dir(path):
    return os.path.isdir(path)


def is_executable(filename):
    return os.access(filename, os.X_OK)


def is_file(filename):
    return os.path.isfile(filename)


def is_link(filename):
    return os.path.islink(filename)


def is_readable(filename):
    return os.access(filename, os.R_OK)


def is_uploaded_file():
    pass


def is_writable(filename):
    return os.access(filename, os.W_OK)


def is_writeable(filename):
    return os.access(filename, os.W_OK)


def lchgrp(filename, group):
    os.lchown(filename, None, group)


def lchown(filename, user):
    return os.lchown(filename, user, None)


def link(target, link):
    return os.link(target, link)


def linkinfo(path):
    return os.stat(path).st_dev


def lstat(filename):
    return os.lstat(filename)


def mkdir(pathname, mode):
    return os.mkdir(pathname, mode)


def move_uploaded_file():
    pass


def parse_ini_file():
    pass


def parse_ini_string():
    pass


def pathinfo():
    pass


def pclose():
    pass


def popen():
    pass


def readfile(filename):
    return open(filename, 'r').read()


def readlink(path):
    return os.readlink(path)


def realpath_cache_get():
    pass


def realpath_cache_size():
    pass


def realpath(path):
    return os.path.realpath(path)


def rename(oldname, newname):
    return os.rename(oldname, newname)


def rewind():
    pass


def rmdir(dirname):
    return os.rmdir(dirname)


def set_file_buffer():
    pass


def stat(filename):
    return os.stat(filename)


def symlink(target, link):
    return os.symlink(target, link)


def tempnam():
    pass


def tmpfile():
    pass


def touch(filename, atime=None, mtime=None):
    return os.utime(filename, (atime, mtime))


def umask(mask):
    return os.umask(mask)


def unlink(filename):
    return os.unlink(filename)


"""
Mathematical Functions
"""


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


'''
Misc. Functions
'''


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


def die():
    sys.exit()


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


'''
Network Functions
'''


def checkdnsrr():
    pass


def closelog():
    return py_syslog.closelog()


def define_syslog_variables():
    pass


def dns_check_record():
    pass


def dns_get_mx(hostname):
    pass


def dns_get_record():
    pass


def fsockopen(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))
    return sock.makefile()


def gethostbyaddr(ip_address):
    return socket.gethostbyaddr(ip_address)


def gethostbyname(hostname):
    return socket.gethostbyname(hostname)


def gethostbynamel(hostname):
    return socket.gethostbyname(hostname)


def gethostname():
    return socket.gethostname()


def getmxrr():
    pass


def getprotobyname(name):
    return socket.getprotobyname(name)


def getprotobynumber(number):
    table = {num: name[8:] for name, num in vars(socket).items() if name.startswith("IPPROTO")}
    return table[number]


def getservbyname(service, protocol):
    return socket.getservbyname(service, protocol)


def getservbyport(port, protocol):
    return socket.getservbyport(port, protocol)


def header_register_callback():
    pass


def header_remove():
    pass


def header():
    pass


def headers_list():
    pass


def headers_sent():
    pass


def http_response_code():
    pass


def inet_ntop(in_addr):
    return socket.inet_ntop(socket.AF_INET, in_addr)


def inet_pton(address):
    return socket.inet_pton(socket.AF_INET, address)


def ip2long(ip_addr):
    return unpack("!L", inet_aton(ip_addr))[0]


def long2ip(ip):
    return inet_ntoa(pack("!L", ip))


def openlog(ident, option, facility):
    return py_syslog.openlog(ident, option, facility)


def pfsockopen():
    pass


def setcookie(name, value='', expire=0, path='', domain=''):
    cookie = http.cookies.SimpleCookie()
    cookie[name] = value
    cookie[name]['domain'] = domain
    cookie[name]['path'] = path
    cookie[name]['expires'] = expire if expire != 0 else py_time.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
    return cookie.output()


def setrawcookie():
    pass


def socket_get_status():
    pass


def socket_set_blocking():
    pass


def socket_set_timeout():
    pass


def syslog(priority, message):
    return py_syslog.syslog(priority, message)


'''
Program execution Functions
'''


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


"""
Strings Functions
"""


def addcslashes(string):
    pass


def addslashes(string):
    pass


def bin2hex(string):
    return binascii.hexlify(string)


def chop(string, character_mask=None):
    return rtrim(string, character_mask)


def chunk_split(body, chunklen, end="\r\n"):
    return end.join(textwrap.wrap(body, chunklen))


def convert_cyr_string(string):
    pass


def convert_uudecode(string):
    pass


def convert_uuencode(string):
    pass


def count_chars(s, mode=0):
    temp = {chr(_x): 0 for _x in range(256)}
    if mode == 0:
        temp.update(Counter(s))
        return temp
    elif mode == 1:
        temp.update(Counter(s))
        res = temp.copy()
        for i, j in temp.items():
            if not j:
                res.pop(i)
        return res
    elif mode == 2:
        temp.update(Counter(s))
        res = temp.copy()
        for i, j in temp.items():
            if j:
                res.pop(i)
        return res
    elif mode == 3:
        res = ""
        temp.update(Counter(s))
        for i, j in temp.items():
            if j:
                res += i
        return res
    elif mode == 4:
        res = ""
        temp.update(Counter(s))
        for i, j in temp.items():
            if not j:
                res += i
        return res
    else:
        raise ValueError("Incorrect value of mode (%d)" % (mode,))


def crc32(string):
    return binascii.crc32(string) & 0xffffffff


def crypt(string, salt):
    return py_crypt.crypt(string, salt)


def echo(string):
    print(string)


def explode(delimiter, string, limit):
    if limit == 0:
        limit = 1

    if limit > 0:
        return string.split(delimiter, limit)
    else:
        return string.split(delimiter)[:limit]


def fprintf(handle, format):
    pass


def get_html_translation_table(string):
    pass


def hebrev(string):
    pass


def hebrevc(string):
    pass


def hex2bin(hex_string):
    return binascii.unhexlify(hex_string)


def html_entity_decode(string):
    pass


def htmlentities(string):
    pass


def htmlspecialchars_decode(string):
    pass


def htmlspecialchars(string):
    pass


def implode(glue='', pieces=[]):
    return glue.join(pieces)


def join(glue='', pieces=[]):
    return glue.join(pieces)


def lcfirst(string):
    return string[0].lower() + string[1:]


def levenshtein(string1, string2):
    n, m = len(string1), len(string2)
    if n > m:
        string1, string2 = string2, string1
        n, m = m, n

    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if string1[j - 1] != string2[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def localeconv(string):
    pass


def ltrim(string, character_mask=None):
    if character_mask is None:
        return string.lstrip()
    return string.lstrip(character_mask)


def md5_file(filename, raw_output=False):
    crc = hashlib.md5()
    fp = open(filename, 'rb')
    for i in fp:
        crc.update(i)
    fp.close()
    if raw_output:
        return crc.digest()
    return crc.hexdigest()


def md5(str, raw_output=False):
    res = hashlib.md5(str.encode())
    if raw_output:
        return res.digest()
    return res.hexdigest()


def metaphone(string):
    pass


def money_format(string):
    pass


def nl_langinfo(string):
    pass


def nl2br(string, is_xhtml=True):
    if is_xhtml:
        return string.replace('\n', '<br />\n')
    else:
        return string.replace('\n', '<br>\n')


def number_format(number, decimals):
    locale.setlocale(locale.LC_NUMERIC, '')
    return locale.format("%.*f", (decimals, number), True)


def parse_str(string):
    return urllib.parse.parse_qs(string)


def printf(string):
    return print(string)


def quoted_printable_decode(string):
    return quopri.decodestring(string)


def quoted_printable_encode(string):
    return quopri.encodestring(string)


def quotemeta(string):
    pass


def rtrim(string, character_mask=None):
    if character_mask is None:
        return string.rstrip()
    return string.rstrip(character_mask)


def setlocale(string):
    pass


def sha1_file(filename, raw_output=False):
    crc = hashlib.sha1()
    fp = open(filename, 'rb')
    for i in fp:
        crc.update(i)
    fp.close()
    if raw_output:
        return crc.digest()
    return crc.hexdigest()


def sha1(string):
    return hashlib.sha1(string.encode()).hexdigest()


def similar_text(string):
    pass


def soundex(string):
    pass


def sprintf(string):
    pass


def sscanf(string):
    pass


def str_getcsv(string, delimiter=',', enclosure='"', escape="\\"):
    with io.StringIO(string) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=enclosure, escapechar=escape)
        return next(reader)


def str_ireplace(search, replace, subject, count=0):
    pattern = re.compile(search, re.IGNORECASE)
    return pattern.sub(replace, subject, count)


def str_pad(string, pad_length, pad_string=' ', pad_type=1):
    # STR_PAD_LEFT = 0
    # STR_PAD_RIGHT = 1
    # STR_PAD_BOTH = 2
    if pad_type == 0:
        return string.ljust(pad_length, pad_string)
    elif pad_type == 2:
        return string.center(pad_length, pad_string)
    else:
        return string.rjust(pad_length, pad_string)


def str_repeat(string, multiplier):
    return string * multiplier


def str_replace(search, replace, subject, count=-1):
    return subject.replace(search, replace, count)


def str_rot13(string):
    enc = codecs.getencoder("rot-13")
    return enc(string)[0]


def str_shuffle(string):
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)


def str_split(string, split_length=1):
    return filter(None, re.split('(.{1,%d})' % split_length, string))


def str_word_count(string, format=0, charlist=''):
    if isinstance(string, str):
        words = re.sub('[^\w ' + charlist + ']', '', string)
        words = words.replace('  ', ' ').split(' ')
        if format == 0:
            return len(words)
        elif format == 1:
            return words
        elif format == 2:
            result = {}
            for word in words:
                result[string.find(word)] = word
            return result
    return False


def strcasecmp(string):
    pass


def strchr(haystack, needle):
    pos = haystack.find(needle)
    if pos < 0:
        return None
    else:
        return haystack[pos:]


def strcmp(string1, string2):
    return (string1 > string2) - (string1 < string2)


def strcoll(string):
    pass


def strcspn(string1, string2):
    return len(list(takewhile(lambda x: x not in string2, string1)))


def strip_tags(string):
    pass


def stripcslashes(string):
    pass


def stripos(haystack, needle, offset=0):
    return haystack.upper().find(needle.upper(), offset)


def stripslashes(string):
    pass


def stristr(haystack, needle):
    pos = haystack.upper().find(needle.upper())
    if pos < 0:
        return None
    else:
        return haystack[pos:]


def strlen(string):
    return len(string)


def strnatcasecmp(string):
    pass


def strnatcmp(string):
    pass


def strncasecmp(string):
    pass


def strncmp(string):
    pass


def strpbrk(haystack, char_list):
    try:
        pos = next(i for i, x in enumerate(haystack) if x in char_list)
        return haystack[pos:]
    except:
        return None


def strpos(haystack, needle, offset=0):
    pos = haystack.find(needle, offset)
    if pos == -1:
        return False
    else:
        return pos


def strrchr(haystack, needle):
    return haystack.rfind(needle)


def strrev(string):
    return string[::-1]


def strripos(haystack, needle, offset=0):
    return haystack.upper().rfind(needle.upper(), offset)


def strrpos(haystack, needle, offset=0):
    pos = haystack.rfind(needle, offset)
    if pos == -1:
        return False
    else:
        return pos


def strspn(subject, mask, start=0, length=None):
    if not length: length = len(subject)
    return len(re.search('^[' + mask + ']*', subject[start:start + length]).group(0))


def strstr(haystack, needle):
    pos = haystack.find(needle)
    if pos < 0:
        return None
    else:
        return haystack[pos:]


def strtok(string):
    pass


def strtolower(string):
    return string.lower()


def strtoupper(string):
    return string.upper()


def strtr(string, from_str, to_str=None):
    if is_array(from_str):
        return string.translate(str.maketrans(from_str))
    return string.translate(str.maketrans(from_str, to_str))


def substr_compare(string):
    pass


def substr_count(haystack, needle, offset=0, length=0):
    if offset == 0:
        return haystack.count(needle)
    else:
        if length == 0:
            return haystack.count(needle, offset)
        else:
            return haystack.count(needle, offset, offset + length)


def substr_replace(subject, replace, start, length=None):
    if length is None:
        return subject[:start] + replace
    elif length < 0:
        return subject[:start] + replace + subject[length:]
    else:
        return subject[:start] + replace + subject[start + length:]


def substr(string, start, length=None):
    if len(string) >= start:
        if start > 0:
            return False
        else:
            return string[start:]
    if not length:
        return string[start:]
    elif length > 0:
        return string[start:start + length]
    else:
        return string[start:length]


def trim(string, character_mask=None):
    if character_mask is None:
        return string.strip()
    return string.strip(character_mask)


def ucfirst(string):
    return string[0].upper() + string[1:]


def ucwords(words):
    return string.capwords(words)


def vfprintf(string):
    pass


def vprintf(string):
    pass


def vsprintf(string):
    pass


def wordwrap(string, width):
    return textwrap.wrap(string, width)


'''
URL Functions
'''


def base64_decode(data):
    return base64.b64decode(data)


def base64_encode(data):
    return base64.encode(data)


def get_headers(url):
    return urllib.request.urlopen('%s' % url).headers


def get_meta_tags(url):
    out = {}
    html = urllib.request.urlopen('%s' % url).read()
    m = re.findall("name=\"([^\"]*)\" content=\"([^\"]*)\"", html)
    for i in m:
        out[i[0]] = i[1]
    return out


def http_build_query(query_data):
    return urllib.parse.urlencode(query_data)


def parse_url(url):
    return urllib.parse.urlparse(url)


def rawurldecode(string):
    return urllib.parse.unquote(string)


def rawurlencode(string):
    return urllib.parse.quote(string)


def urldecode(string):
    return urllib.parse.unquote_plus(string)


def urlencode(string):
    return urllib.parse.quote_plus(string)


'''
Variable handling Functions
'''


def boolval(variable):
    return bool(variable)


def debug_zval_dump():
    pass


def doubleval(variable):
    return float(variable)


def empty(variable):
    if not variable:
        return True
    return False


def floatval(variable):
    return float(variable)


def get_defined_vars():
    pass


def get_resource_type():
    pass


def gettype(variable):
    return type(variable).__name__


def import_request_variables():
    pass


def intval(variable, base=10):
    return int(variable, base)


def is_array(variable):
    return isinstance(variable, (list, tuple))


def is_bool(variable):
    return isinstance(variable, bool)


def is_callable(name):
    return callable(name)


def is_countable(variable):
    try:
        Counter(variable)
        return True
    except:
        return False


def is_double(variable):
    return isinstance(variable, float)


def is_float(variable):
    return isinstance(variable, float)


def is_int(variable):
    return isinstance(variable, int)


def is_integer(variable):
    return isinstance(variable, int)


def is_iterable(variable):
    return is_array(variable) or isinstance(variable, collections.Iterable)


def is_long(variable):
    return isinstance(variable, int)


def is_null(variable):
    return variable is None


def is_numeric(variable):
    return isinstance(variable, numbers.Number) or variable.isnumeric()


def is_object(variable):
    return isinstance(variable, object)


def is_real(variable):
    return isinstance(variable, float)


def is_resource():
    pass


def is_scalar(variable):
    return isinstance(variable, (type(None), str, int, float, bool))


def is_string(variable):
    return isinstance(variable, str)


def isset(variable):
    try:
        variable
        return True
    except NameError:
        return False


def print_r(variable):
    pprint.pprint(variable)


def serialize(value):
    return pickle.dump(value)


def settype(variable, variable_type):
    pass


def strval(variable):
    return str(variable)


def unserialize():
    pass


def unset(variable):
    del variable


def var_dump(variable):
    print(variable)


def var_export(variable):
    print(variable)
