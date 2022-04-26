#! /usr/bin/env python
# -*- coding: utf8 -*-
import shutil
import fnmatch as py_fnmatch
import re
import csv
import glob as py_glob
import fcntl
import string
import os


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
