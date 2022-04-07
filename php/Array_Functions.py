#! /usr/bin/env python
# -*- coding: utf8 -*-
import random
from functools import reduce
import inspect
from collections import Counter
import os

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