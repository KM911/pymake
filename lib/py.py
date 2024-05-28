import sys
import os
import subprocess

from init import *


def py_venv(argv: list):
    Run("python -m venv ./venv")


def py_run(argv: list):
    # Run("./venv/bin/python main.py")

    for i in argv:
        Run("./venv/bin/python "+i)


def py_pip(argv: list):

    # print("your argv is",argv)
    for i in argv:
        Run("./venv/bin/pip install " + i)

def pip(argv: list):

    # print("your argv is",argv)
    for i in argv:
        Run("./venv/bin/pip install " + i)
def py(argv: list):
    for i in argv:
        Run("./venv/bin/python " + i)



def py_proxy(argv: list):
    Run("./venv/bin/pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple pip -U")
    Run("./venv/bin/pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple")


def py_install(argv: list):
    Run("./venv/bin/pip install -r requirements.txt")


def py_export(argv: list):
    # export requirements.txt
    Run("./venv/bin/pip freeze > requirements.txt")
