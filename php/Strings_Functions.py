#! /usr/bin/env python
# -*- coding: utf8 -*-
import locale
import codecs
import random
import io
from itertools import takewhile
import crypt as py_crypt
import binascii
import re
import csv
import urllib.parse
import string
import textwrap
import hashlib
from collections import Counter
import quopri
import os

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