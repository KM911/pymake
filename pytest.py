import os
import sys
import subprocess


import typo
from lib.test import *
from lib.go import *
from lib.rust import *
from lib.py import *
from lib.docker import *


Github_Username = "KM911"
Template_Dir = "/home/km/Code/template/go/"


def Load_Project_Env():
    global pwd, project, env
    pwd = os.getcwd()
    # print("pwd =", pwd)
    project = pwd.replace("\\", "/").split("/")[-1]
    # print("project =", project)
    env = os.environ.copy()


def changeMessage():
    global message
    message = "This is change message"


message = "This is pymake"
argc = 0
argv = []


#
if __name__ == "__main__":

    # pre check
    argv = sys.argv.copy()
    print("argv is", argv)
    argc = len(argv)
    print("argc is ", argc)
    for i in range(argc):
        argv[i] = typo.ERROR_DICT.get(argv[i], argv[i])

    offset = 1
    error = None
    # py run
    while True:

        try:
            print("offset is ", offset)
            print(f'{"_".join(argv[1:offset+1])}({argv[offset+1:]})')
            eval(f'{"_".join(argv[1:offset+1])}({argv[offset+1:]})')
            break
        except Exception as e:
            error = e
            offset += 1
            if offset == 3:
                print(error)
                break
        except IndentationError:
            print("Your Input is ", sys.argv)
            print("Fixed typo result is ", argv)
            print("execute command is ")

    # eval(f'test_args({sys.argv})')

    # eval('hello_world({li})'.format(li=list_))

    # first parse just fix the problem
