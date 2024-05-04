import sys
import os
import subprocess

from lib.go import * 
from lib.py import *
from lib.rust import *


from lib.docker import *
# Core function

# 输出cmd path or bash path

Github_Username = "KM911"
Template_Dir = "/home/km/Code/template/go/"

def Run(command: str):
    subprocess.run(command, shell=True)

# def CommandSlient(command: str):
#     # 重定向stdout


def ShowCommand(command: str):
    print(command)
    Run(command)


def CommandResult(command: str) -> str:
    return os.popen(command).read()


def RunSlient(command: str):

    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


def RunSlientVerbose(command: str):
    print(command)
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


def RunSlientResult(command: str) -> str:
    file = open(os.path.join(os.environ.get("temp"), "temp.txt"), "w+")
    subprocess.run(command, shell=True, stdout=file,
                   stderr=subprocess.DEVNULL)
    file.seek(0)
    result = file.read()
    file.close()
    return result


def Cd(path: str):
    os.chdir(path)


def ExecutePathConvent(path: str) -> str:
    if os.name == "nt":
        return path
    else:
        return "./"+path


def ExeConvent(path: str) -> str:
    if os.name == "nt":
        return path+".exe"
    else:
        return path


def Load_Project_Env():
    global pwd, project, env
    pwd = os.getcwd()
    # print("pwd =", pwd)
    project = pwd.replace("\\", "/").split("/")[-1]
    # print("project =", project)
    env = os.environ.copy()


def Get_Programming_Using():
    global programming_using
    SupportLanguage = ["go", "rs", "c", "cpp", "py"]


def CheckEnv():
    print("need python3 rg")

def help():  # show all function
    # content = [x[4:-1] for x in open(Template_Dir +"pymake.py", "r", encoding='utf-8').readlines()
    #            if x.startswith("def") and x[4].islower()]
    # print("\n".join(content))
    print("help")

# main function
# TODO add more typo
ErrorDict = {"iamge": "image", "benhc": "bench",
             "clnea": "clean", "dokcer": "docker", "dokecr": "docker", "dcoker": "docker"}

def Parse():
    print(sys.argv)
    global argv
    argc = len(sys.argv)
    # print(argc)
    if argc == 1:
        help()

    elif argc == 2:
        try:
            argv = sys.argv[2:]
            eval(sys.argv[1]+"()")
        except NameError as e:
            # fix typo

            print("name error")
            fixed = ErrorDict.get(sys.argv[1], None)
            if fixed is None:
                help()
            else:
                eval(fixed+"()")

    else:
        argv = sys.argv[3:]
        try:
            eval("_".join(sys.argv[1:3])+"()")
        except NameError as e :
            print("name error", e)
            fixed_1 = ErrorDict.get(sys.argv[1], None)
            fixed_2 = ErrorDict.get(sys.argv[2], None)
            if fixed_1 is None and fixed_2 is None:
                help()
            else:
                try:
                    if fixed_1 is None:
                        eval(sys.argv[1]+"_"+fixed_2+"()")
                    else:
                        eval(fixed_1+"_"+sys.argv[2]+"()")
                except NameError:
                    help()