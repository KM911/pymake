import sys
import os
import subprocess
from init import *


# Docker function


def Load_Docker_Env(argv=[]):
    global image_info, version
    image_info = [x for x in CommandResult("sudo docker image list").split(
        "\n") if x.startswith(project)]
    if len(image_info) == 0:
        print("no image")
        version = "0.0.0"
    else:
        import re
        version = re.findall(r"\d+\.\d+\.\d+", image_info[0])[0]


def image(argv=[]):

    Load_Docker_Env()
    if len(image_info) == 0:
        print("no image")
    else:
        print(image_info)


def container(argv=[]):

    container = [x for x in CommandResult(
        "docker container list").split("\n") if x.startswith(project)]
    if len(container) == 0:
        print("no container")
    else:
        print(container)


def docker_init(argv=[]):
    os.mkdir("docker")
    os.mkdir("docker/public")

    file = open("docker/Dockerfile", "w+")
    file.write("FROM alpine:latest\n")
    file.write("WORKDIR /app\n")
    file.write("ADD . /app\n")
    file.close()


def docker_build(argv=[]):
    image_build()


def redis_start(argv=[]):
    Run("docker run -d --name redis -p 6379:6379  -v /data/redis:/data/redis redis:latest")


def image_build(argv=[]):
    Load_Docker_Env()
    import re
    version_num = version.split(".")
    version_num[-1] = str(int(version_num[-1])+1)
    new_version = ".".join(version_num)

    if os.path.exists(project):
        if os.path.exists("docker/public/app"):
            os.remove("docker/public/app")
        os.rename(project, "docker/public/app")
    # else:

    Run("docker build -t "+project+":"+new_version+" ./docker/.")
    Run("docker tag "+project+":"+new_version+" "+project+":latest")
    Run("docker image rm -f "+project+":"+version)


def image_list(argv=[]):
    Load_Docker_Env()
    Run("docker image list | grep " + project)


def image_ls(argv=[]):
    image_list()


def container_clean(argv=[]):
    Run("docker container prune ")


#
def image_clean(argv=[]):
    #
    Run("docker image prune")


def image_run(argv=[]):
    Load_Docker_Env()
    Run("docker run -it "+project+":"+version)
