import sys
import os
import subprocess
from import init import *



def py_venv():
    Run("python -m venv ./venv")


def py_run():
    # Run("./venv/bin/python main.py")
    Load_Project_Env()
    for i in argv:
        Run("./venv/bin/python "+i)

def py_pip():
    Load_Project_Env()

    # print("your argv is",argv)
    for i in argv :
        Run("./venv/bin/pip install " + i)
def py_install():
    Run("./venv/bin/pip install -r requirements.txt")

def py_export():
    # export requirements.txt
    Run("./venv/bin/pip freeze > requirements.txt")