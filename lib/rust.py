import sys
import os
import subprocess

from init import *


def rs_expand(argv: list):

    Run("cargo expand > main.rs")


def rs(argv: list):
    # rs_release()
    rs_debug()


def rs_build(argv: list):
    rs_debug()


def rs_release(argv: list):

    Run("cargo build --release")
    # move file into current directory
    Run("cp ./target/release/"+project+" ./"+project)


def rs_debug(argv: list):
    Run("cargo build")
    # move file into current directory
    Run("cp ./target/debug/"+project+" ./"+project)
