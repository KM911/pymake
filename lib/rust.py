import sys
import os
import subprocess

from init import *


def rust_build(argv: list):

    Run("cargo build --release")
    # move file into current directory
    Run("cp ./target/release/"+project+" ./"+project)


def rust_expand(argv: list):

    Run("cargo expand > main.rs")


def rust_r(argv: list):
    rust_release()


def rust_release(argv: list):

    Run("cargo build --release")
    # move file into current directory
    Run("cp ./target/release/"+project+" ./"+project)
