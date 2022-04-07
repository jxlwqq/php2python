#! /usr/bin/env python
# -*- coding: utf8 -*-
import base64
import re
import urllib.parse
import urllib.request

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