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


def py_install(argv: list):
    Run("./venv/bin/pip install -r requirements.txt")


def py_export(argv: list):
    # export requirements.txt
    Run("./venv/bin/pip freeze > requirements.txt")
