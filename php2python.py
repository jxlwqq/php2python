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
import time
import datetime
import binascii
import urllib.parse
from itertools import takewhile
import numbers
import pickle

"""
Array Functions
"""


def array_change_key_case(array, case=0):
    """
    array_change_key_case — Changes the case of all keys in an array
    http://php.net/manual/en/function.array-change-key-case.php
    """
    if case == 0:
        f = str.lower
    elif case == 1:
        f = str.upper
    else:
        raise ValueError()
    return dict((f(k), v) for k, v in array.items())


def array_chunk(array, size):
    """
    array_chunk — Split an array into chunks
    http://php.net/manual/zh/function.array-chunk.php
    """
    return [array[i: i + size] for i in range(0, len(array), size)]


def array_column(array, column_key, index_key):
    pass


def array_combine(keys, values):
    """
    array_combine — Creates an array by using one array for keys and another for its values
    http://php.net/manual/zh/function.array-combine.php
    """
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
    """
    array_filter — Filters elements of an array using a callback function
    http://php.net/manual/en/function.array-filter.php
    """
    filter(callback, array)


def array_flip(array):
    """
    array_flip — Exchanges all keys with their associated values in an array
    http://php.net/manual/en/function.array-flip.php
    """
    return dict((v, k) for k, v in array.items())


def array_intersect_assoc(array1, array2):
    """
    array_intersect_assoc — Computes the intersection of arrays with additional index check
    http://php.net/manual/en/function.array-intersect-assoc.php
    """
    # todo
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
    """
    array_merge — Merge one or more arrays
    http://php.net/manual/en/function.array-merge.php
    """
    if isinstance(array1, list) and isinstance(array2, list):
        return array1 + array2
    elif isinstance(array1, dict) and isinstance(array2, dict):
        return dict(list(array1.items()) + list(array2.items()))
    elif isinstance(array1, set) and isinstance(array2, set):
        return array1.union(array2)
    return False


def array_multisort():
    pass


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
    pass


def array_splice(array, offset, length, replacement=None):
    pass


def array_sum(array):
    pass


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
    pass


def array_unshift(array):
    pass


def array_values(array):
    return array.values()


def array_walk_recursive(array):
    pass


def array_walk(array):
    pass


def array(array):
    pass


def arsort(array):
    pass


def asort(array):
    pass


def compact(array):
    pass


def count(array):
    return len(array)


def current(array):
    pass


def each(array):
    pass


def end(array):
    pass


def extract(array):
    pass


def in_array(needle, haystack):
    return needle in haystack


def key_exists(key, array):
    return array_key_exists(key, array)


def key(array):
    pass


def krsort(array):
    pass


def ksort(array):
    pass


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
    pass


def shuffle(array):
    return random.shuffle(array)


def sizeof(array):
    return len(array)


def sort(array):
    pass


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
    pass


def date_default_timezone_set():
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


def date():
    pass


def getdate():
    pass


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
    return time.localtime(timestamp)


def microtime(get_as_float=False):
    d = datetime.now()
    t = time.mktime(d.timetuple())
    if get_as_float:
        return t
    else:
        ms = d.microsecond / 1000000.
        return '%f %d' % (ms, t)


def mktime(hour, minute, second, month, day, year):
    return time.mktime((year, month, day, hour, minute, second))


def strftime():
    pass


def strptime():
    pass


def strtotime():
    pass


def time():
    return int(time.time())


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


def chunk_split(string):
    pass


def convert_cyr_string(string):
    pass


def convert_uudecode(string):
    pass


def convert_uuencode(string):
    pass


def count_chars(string, mode=0):
    """
    count_chars — Return information about characters used in a string
    http://php.net/manual/en/function.count-chars.php
    """
    pass


def crc32(string):
    return binascii.crc32(string) & 0xffffffff


def crypt(string):
    pass


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
    return implode(glue, pieces)


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


def nl2br(string):
    pass


def number_format(number, decimals):
    locale.setlocale(locale.LC_NUMERIC, '')
    return locale.format("%.*f", (decimals, number), True)


def parse_str(string):
    return urllib.parse.parse_qs(string)


def printf(string):
    return print(string)


def quoted_printable_decode(string):
    pass


def quoted_printable_encode(string):
    pass


def quotemeta(string):
    pass


def rtrim(string, character_mask=None):
    if character_mask is None:
        return string.rstrip()
    return string.rstrip(character_mask)


def setlocale(string):
    pass


def sha1_file(string):
    pass


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


def str_ireplace(string):
    pass


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
    """
    str_repeat — Repeat a string
    http://php.net/manual/en/function.str-repeat.php
    :param str:
    :param multiplier:
    :return:
    """
    return string * multiplier


def str_replace(search, replace, subject, count):
    """
    str_replace — Replace all occurrences of the search string with the replacement string
    :param search:
    :param replace:
    :param subject:
    :param count:
    :return:
    """
    pass


def str_rot13(string):
    pass


def str_shuffle(string):
    """
    str_shuffle — Randomly shuffles a string
    http://php.net/manual/en/function.str-shuffle.php
    :param string:
    :return:
    """
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)


def str_split(string, split_length=1):
    """
    str_split — Convert a string to an array
    http://php.net/manual/en/function.str-split.php
    """
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


def strchr(string):
    pass


def strcmp(string):
    pass


def strcoll(string):
    pass


def strcspn(string1, string2):
    return len(list(takewhile(lambda x: x not in string2, string1)))


def strip_tags(string):
    pass


def stripcslashes(string):
    pass


def stripos(string):
    pass


def stripslashes(string):
    pass


def stristr(string):
    pass


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


def strpbrk(string):
    pass


def strpos(string):
    pass


def strrchr(string):
    pass


def strrev(string):
    pass


def strripos(string):
    pass


def strrpos(string):
    pass


def strspn(string):
    pass


def strstr(string):
    pass


def strtok(string):
    pass


def strtolower(string):
    return string.lower()


def strtoupper(string):
    return string.upper()


def strtr(string):
    pass


def substr_compare(string):
    pass


def substr_count(string):
    pass


def substr_replace(string):
    pass


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
    """
    ucfirst — Make a string's first character uppercase
    http://php.net/manual/en/function.ucfirst.php
    :param string:
    :return:
    """
    return string[0].upper() + string[1:]


def ucwords(string):
    """
    ucwords — Uppercase the first character of each word in a string
    http://php.net/manual/en/function.ucwords.php
    :param string:
    :return:
    """
    pass


def vfprintf(string):
    pass


def vprintf(string):
    pass


def vsprintf(string):
    pass


def wordwrap(string):
    pass


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


def is_callable():
    pass


def is_countable():
    pass


def is_double(variable):
    return isinstance(variable, float)


def is_float(variable):
    return isinstance(variable, float)


def is_int(variable):
    return isinstance(variable, int)


def is_integer(variable):
    return isinstance(variable, int)


def is_iterable():
    pass


def is_long():
    pass


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


def print_r():
    pass


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


'''
Misc. Functions
'''
