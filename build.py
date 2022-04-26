#! /usr/bin/env python
# -*- coding: utf8 -*-
import re
import sys
import os

path = os.path.abspath(os.path.dirname(sys.argv[0]))
header_file_template = """
#! /usr/bin/env python
# -*- coding: utf8 -*-
"""

setup_file_template = """from setuptools import setup

setup(name='php2python',
      version='0.0.1-{}',
      packages=['php',],
      description='Python alternatives for PHP functions',
      url='https://github.com/jxlwqq/php2python',
      author='jxlwqq',
      author_email='jxlwqq@gmail.com',
      license='MIT',
      python_requires='>=3',
      requires=[
            'tzlocal>=1.5',
            'var_dump>=1.2'
      ],
      zip_safe=False)
"""


class file(object):
    def read(fil, mode="r"):
        with open(fil, mode) as f:
            f = f.read()
        return f

    def write(fil, content, mode="w"):
        f = open(fil, mode)
        return f.write(content)

    def list(mypath):
        from os.path import isfile, isdir, join
        ret = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
        return ret


def reformater():
    batas = '"""\n.*\n"""'
    nama = '"""\n(.*)\n"""'
    code = file.read(path+"/php2python.py")
    batas_reg = re.compile(batas)
    batas = re.split(batas_reg, code)
    nama_reg = re.compile(nama)
    nama = re.findall(nama_reg, code)
    mh = batas[0]
    del batas[0]
    mls = {}
    for nm in mh.split("\n"):
        if " as " in nm:
            namatmp = nm.split(" as ")[-1].strip()
            if namatmp != "":
                mls[namatmp] = nm.strip()
        else:
            namatmp = nm.split("import")[-1].strip()
            if namatmp != "":
                mls[namatmp] = nm.strip()

    for k, v in enumerate(batas):
        nf = nama[k].strip()
        nf = nf.replace("/", "_")
        nf = nf.replace(" ", "_")
        nf = nf.replace(".", "")
        nf = path+"/php/"+nf+".py"
        print("processing", nf)
        file.write(nf, header_file_template.strip()+"\n")
        for mk, mv in mls.items():
            if "."+mk in v or mk+"." in v or mk+"(" in v:
                file.write(nf, mv+"\n", mode="a")
        file.write(nf, "\n", mode="a")
        file.write(nf, v.strip(), mode="a")

    print("complete!")


def gen_init():
    tmp_add = "from .{0} import {1}\n"
    res = ""
    ls = file.list(path+"/php")
    for fn in ls:
        if fn != "__init__.py":
            print("processing", fn)
            code = file.read(path+"/php/"+fn)
            mod = re.findall("def\s(.*)\(", code)
            res = res + tmp_add.format(fn.replace(".py", ""), ",".join(mod))
    file.write(path+"/php/__init__.py", res)
    file.write(path+"/php/__init__.py",
               "from var_dump import var_dump\n", mode="a")
    print("complete!")


def gen_setup():
    from gitbinding import Git
    import os
    sha = "'{}'".format(os.getenv('GITHUB_SHA'))
    git = Git(direct_output=False)
    has = git.rev_parse("--short", sha)
    tx = setup_file_template.format(has.strip())
    file.write("setup.py", tx)
    print("complete!")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        com = sys.argv[1]
        if com == "reformat":
            print("reformatting ..")
            reformater()
            quit()
        elif com == "init":
            print("generating php/__init__.py ..")
            gen_init()
            quit()
        elif com == "setup":
            print("generating setup.py ..")
            gen_setup()
            quit()
        else:
            pass
    print("Usage: build.py [command]")
    print("\nlist command:")
    print("-"*len("list command:"))
    print("init     : auto generating __init__.py.")
    print("setup    : auto generating setup.py.")
    print("reformat : reformat old php2python.py.")
