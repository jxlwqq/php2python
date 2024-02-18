#! /usr/bin/env python
import collections
import numbers
import pickle
import pprint
from collections import Counter


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
    return is_array(variable) or isinstance(variable, collections.abc.Iterable)


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


def var_export(variable):
    return repr(variable)
