# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-10-12 10:47:46
# @Last Modified by:   1249614072@qq.com
# @Last Modified time: 2017-10-20 00:27:02
import sys
import types


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str,
    integer_types = int,
    class_types = type,
    text_type = str
    binary_type = bytes
    range_type = range

else:
    string_types = basestring,
    integer_types = (int, long)
    class_types = (type, types.ClassType)
    text_type = unicode
    binary_type = str
    range_type = xrange


try:
    from urllib.parse import urlparse
except Exception as e:
    from urlparse import urlparse


try:
    from urllib.parse import parse_qs
except Exception as e:
    from urlparse import parse_qs


def is_type_unicode(value):
    if not PY3 and isinstance(value, text_type):
        return value.encode('utf-8')
    else:
        return str(value)


def is_type_bytes(value):
    if PY3 and isinstance(value, binary_type):
        return value.decode('utf-8')
    else:
        return str(value)


if __name__ == '__main__':
    pass
