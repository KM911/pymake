# import pymake
# from pymake import *
import pytest

# bug: this could not know the message is import from pymake.py
def hello():
    print("start hello")
    pytest.changeMessage()
    print(pytest.message)
    print("exit hello")
    # pytest.EnvClass.change()
    # print(pytest.EnvClass.message)
    # pytest.EnvClass.changeWithArg("hello world")

# project , pwd , 
def hello_world( args : list, pwd  : str , project  : str) :
    for i in args :
        print("args i is ", i)

def test_args(args : list):
    for i in range (len(args)) : 
        print(f"{i} is , {args[i]}")
