#! /usr/bin/env python
import http.cookies
import socket
import syslog as py_syslog
import time as py_time
from socket import inet_aton, inet_ntoa
from struct import pack, unpack


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
    table = {
        num: name[8:]
        for name, num in vars(socket).items()
        if name.startswith("IPPROTO")
    }
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


def setcookie(name, value="", expire=0, path="", domain=""):
    cookie = http.cookies.SimpleCookie()
    cookie[name] = value
    cookie[name]["domain"] = domain
    cookie[name]["path"] = path
    cookie[name]["expires"] = (
        expire
        if expire != 0
        else py_time.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
    )
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
