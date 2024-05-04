import sys
import os
import subprocess
from import init import *



# Docker function


def Load_Docker_Env():
    Load_Project_Env()
    global image_info, version
    image_info = [x for x in CommandResult("docker image list").split(
        "\n") if x.startswith(project)]
    if len(image_info) == 0:
        print("no image")
        version = "0.0.0"
    else:
        import re
        version = re.findall(r"\d+\.\d+\.\d+", image_info[0])[0]


def image():
    Load_Project_Env()
    Load_Docker_Env()
    if len(image_info) == 0:
        print("no image")
    else:
        print(image_info)


def container():
    Load_Project_Env()
    container = [x for x in CommandResult(
        "docker container list").split("\n") if x.startswith(project)]
    if len(container) == 0:
        print("no container")
    else:
        print(container)


def docker_init():
    os.mkdir("docker")
    os.mkdir("docker/public")

    file = open("docker/Dockerfile", "w+")
    file.write("FROM alpine:latest\n")
    file.write("WORKDIR /app\n")
    file.write("ADD . /app\n")
    file.close()


def docker_build():
    image_build()


def redis_start():
    Run("docker run -d --name redis -p 6379:6379  -v /data/redis:/data/redis redis:latest")


def image_build():
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


def image_list():
    Load_Docker_Env()
    Run("docker image list | grep " + project)


def image_ls():
    image_list()


def container_clean():
    Run("docker container prune ")


#
def image_clean():
    #
    Run("docker image prune")


def image_run():
    Load_Docker_Env()
    Run("docker run -it "+project+":"+version)