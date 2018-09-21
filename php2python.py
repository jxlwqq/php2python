#! /usr/bin/env python
# -*- coding: utf8 -*-

# Variable and Type Related Extensions


def array_change_key_case(array, case=0):
    """
    array_change_key_case — Changes the case of all keys in an array
    Returns an array with all keys from array lowercased or uppercased. Numbered indices are left as is.
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
    Chunks an array into arrays with size elements. The last chunk may contain less than size elements.
    http://php.net/manual/zh/function.array-chunk.php
    """
    return [array[i: i + size] for i in range(0, len(array), size)]


def array_column(array, column_key, index_key):
    pass


def array_combine(keys, values):
    """
    array_combine — Creates an array by using one array for keys and another for its values
    Creates an array by using the values from the keys array as keys and the values from the values array as the corresponding values.
    http://php.net/manual/zh/function.array-combine.php
    """
    return dict(zip(keys, values))


def array_count_values(array):
    from collections import Counter
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
