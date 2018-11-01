#! /usr/bin/env python
# -*- coding: utf8 -*-


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
    from collections import Counter
    return Counter(array)


def array_diff_assoc(self):
    pass


def array_diff_key(self):
    pass


def array_diff_uassoc(self):
    pass


def array_diff_ukey(self):
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
        for key, value in array.items(self):
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


def array_multisort(self):
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
        from functools import reduce
        reduce(lambda a, b: a * b, array)


def array_push(array, *values):
    for value in values:
        array.extend(value)


def array_rand(array, num=1):
    import random
    if num == 1:
        return random.choice(array.keys())
    else:
        return random.sample(array.keys(), num)


def array_reduce(array, callback, initial=None):
    from functools import reduce
    if initial is None:
        return reduce(callback, array)
    else:
        return reduce(function, array, initial)


def array_replace_recursive(self):
    pass


def array_replace(self):
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
    pass


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


def in_array(array):
    pass


def key_exists(array):
    pass


def key(array):
    pass


def krsort(array):
    pass


def ksort(array):
    pass


def php_list(array):
    pass


def natcasesort(array):
    pass


def natsort(array):
    pass


def next(array):
    pass


def pos(array):
    pass


def prev(array):
    pass


def php_range(low, high, step=None):
    if low >= high:
        return range(low, high + 1, step)
    else:
        return range(low, high - 1, -step)
    pass


def reset(array):
    pass


def rsort(array):
    pass


def shuffle(array):
    import random
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
Function handling Functions
"""


def call_user_func_array(self):
    pass


def call_user_func(self):
    pass


def create_function(self):
    pass


def forward_static_call_array(self):
    pass


def forward_static_call(self):
    pass


def func_get_arg(self):
    pass


def func_get_args(self):
    pass


def func_num_args(self):
    pass


def function_exists(self):
    pass


def get_defined_functions(self):
    pass


def register_shutdown_function(self):
    pass


def register_tick_function(self):
    pass


def unregister_tick_function(self):
    pass


"""
Date/Time Functions
"""


def checkdate(self):
    pass


def date_add(self):
    pass


def date_create_from_format(self):
    pass


def date_create_immutable_from_format(self):
    pass


def date_create_immutable(self):
    pass


def date_create(self):
    pass


def date_date_set(self):
    pass


def date_default_timezone_get(self):
    pass


def date_default_timezone_set(self):
    pass


def date_diff(self):
    pass


def date_format(self):
    pass


def date_get_last_errors(self):
    pass


def date_interval_create_from_date_string(self):
    pass


def date_interval_format(self):
    pass


def date_isodate_set(self):
    pass


def date_modify(self):
    pass


def date_offset_get(self):
    pass


def date_parse_from_format(self):
    pass


def date_parse(self):
    pass


def date_sub(self):
    pass


def date_sun_info(self):
    pass


def date_sunrise(self):
    pass


def date_sunset(self):
    pass


def date_time_set(self):
    pass


def date_timestamp_get(self):
    pass


def date_timestamp_set(self):
    pass


def date_timezone_get(self):
    pass


def date_timezone_set(self):
    pass


def date(self):
    pass


def getdate(self):
    pass


def gettimeofday(self):
    pass


def gmdate(self):
    pass


def gmmktime(self):
    pass


def gmstrftime(self):
    pass


def idate(self):
    pass


def localtime(self):
    pass


def microtime(self):
    pass


def mktime(self):
    pass


def strftime(self):
    pass


def strptime(self):
    pass


def strtotime(self):
    pass


def time(self):
    pass


def timezone_abbreviations_list(self):
    pass


def timezone_identifiers_list(self):
    pass


def timezone_location_get(self):
    pass


def timezone_name_from_abbr(self):
    pass


def timezone_name_get(self):
    pass


def timezone_offset_get(self):
    pass


def timezone_open(self):
    pass


def timezone_transitions_get(self):
    pass


def timezone_version_get(self):
    pass


"""
Strings Functions
"""


def addcslashes(string):
    pass


def addslashes(string):
    pass


def bin2hex(string):
    pass


def chop(string):
    pass


def chr(string):
    pass


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
    import binascii
    return binascii.crc32(string) & 0xffffffff


def crypt(string):
    pass


def echo(string):
    print(string)


def explode(string):
    pass


def fprintf(string):
    pass


def get_html_translation_table(string):
    pass


def hebrev(string):
    pass


def hebrevc(string):
    pass


def hex2bin(string):
    pass


def html_entity_decode(string):
    pass


def htmlentities(string):
    pass


def htmlspecialchars_decode(string):
    pass


def htmlspecialchars(string):
    pass


def implode(string):
    pass


def join(string):
    pass


def lcfirst(string):
    pass


def levenshtein(string):
    pass


def localeconv(string):
    pass


def ltrim(string, character_mask=None):
    if character_mask is None:
        return string.lstrip()
    return string.lstrip(character_mask)


def md5_file(filename, raw_output=False):
    import hashlib
    crc = hashlib.md5()
    fp = open(filename, 'rb')
    for i in fp:
        crc.update(i)
    fp.close()
    if raw_output:
        return crc.digest()
    return crc.hexdigest()


def md5(str, raw_output=False):
    import hashlib
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
    import locale
    locale.setlocale(locale.LC_NUMERIC, '')
    return locale.format("%.*f", (decimals, number), True)


def ord(string):
    pass


def parse_str(string):
    pass


def php_print(string):
    return print(string)


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
    pass


def similar_text(string):
    pass


def soundex(string):
    pass


def sprintf(string):
    pass


def sscanf(string):
    pass


def str_getcsv(string, delimiter=',', enclosure='"', escape="\\"):
    import csv
    import io
    with io.StringIO(string) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=enclosure, escapechar=escape)
        return next(reader)


def str_ireplace(string):
    pass


def str_pad(string):
    pass


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
    import random
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)


def str_split(string, split_length=1):
    """
    str_split — Convert a string to an array
    http://php.net/manual/en/function.str-split.php
    """
    import re
    return filter(None, re.split('(.{1,%d})' % split_length, string))


def str_word_count(string, format=0, charlist=''):
    import re
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


def strcspn(string):
    pass


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
    pass


def strtoupper(string):
    pass


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


def abs(self):
    pass


def acos(self):
    pass


def acosh(self):
    pass


def asin(self):
    pass


def asinh(self):
    pass


def atan2(self):
    pass


def atan(self):
    pass


def atanh(self):
    pass


def base_convert(self):
    pass


def bindec(self):
    pass


def ceil(self):
    pass


def cos(self):
    pass


def cosh(self):
    pass


def decbin(self):
    pass


def dechex(self):
    pass


def decoct(self):
    pass


def deg2rad(self):
    pass


def exp(self):
    pass


def expm1(self):
    pass


def floor(self):
    pass


def fmod(self):
    pass


def getrandmax(self):
    pass


def hexdec(self):
    pass


def hypot(self):
    pass


def intdiv(self):
    pass


def is_finite(self):
    pass


def is_infinite(self):
    pass


def is_nan(self):
    pass


def lcg_value(self):
    pass


def log10(self):
    pass


def log1p(self):
    pass


def log(self):
    pass


def max(self):
    pass


def min(self):
    pass


def mt_getrandmax(self):
    pass


def mt_rand(self):
    pass


def mt_srand(self):
    pass


def octdec(self):
    pass


def pi(self):
    pass


def pow(self):
    pass


def rad2deg(number):
    import math
    return math.degrees(number)


def rand(minint, maxint):
    import random
    random.randint(minint, maxint)


def php_round(val, precision=0):
    round(val, precision)


def sin(arg):
    import math
    math.sin(arg)


def sinh(arg):
    import math
    math.sinh(arg)


def sqrt(arg):
    import math
    math.sqrt(arg)


def srand(seed=None):
    import random
    if seed is None:
        return random.seed()
    return random.seed(seed)


def tan(arg):
    import math
    return math.tan(arg)


def tanh(arg):
    import math
    math.tanh(arg)
