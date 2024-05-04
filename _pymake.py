
import sys
import os
import subprocess

import init

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
# def 

# def 


# basic function




def clean():
    Load_Project_Env()
    ShowCommand("rm -rf "+project)
    ShowCommand("rm -rf *.exe")
    ShowCommand("rm -rf *.test")
    ShowCommand("rm -rf *.out")
    ShowCommand("rm -rf *.log")
    ShowCommand("rm -rf *.prof")

# go function


def Load_Go_Env():
    Load_Project_Env()
    global mod
    mod = open("go.mod", "r").readline().split(" ")[
        1].strip()


def go_test():
    Load_Go_Env()
    Run(" ".join(["go", "test", "-v", mod+"/test"]))

# 一个大问题 它不会显示 关于内存占用的部分
# 131072 B/op 1 allocs/op


def go_gen():
    Load_Go_Env()
    Run("go generate")
    go_build()


def go_bin():
    Load_Go_Env()
    go_build()
    Run("mv -f "+project + " /usr/bin/" + project)


def Go_Benchmark(package: str):
    Load_Go_Env()
    Cd(package)
    command = " ".join(
        ["go", "test", "-c", "-o", "benchmark.test", mod+"/"+package])
    Run(command)
    command = " ".join([ExecutePathConvent("benchmark.test"),
                       "-test.benchmem", "-test.bench",  "."])

    result = CommandResult(command).split("\n")[4:-2]
    import re
    regex_time = re.compile(r"\d+.?\d?(?= [mnu]s/op)")

    function_result = [result[i].split("-12") for i in range(len(result))]

    # BenchmarkConbineJoin-12            48390             24538 ns/op           16224 B/op          8 allocs/op
    unit = re.findall(r"[mnu]s/op", function_result[0][1],)[0]

    for i in range(len(function_result)):
        function_result[i][1] = float(
            regex_time.findall(function_result[i][1])[0])

    sorted_function_result = sorted(function_result, key=lambda x: float(x[1]))
    min_time = float(sorted_function_result[0][1])

    # sorted_function_result.insert(0, ["function", "time/op", "ratio", "delay"])
    format_output = [
        f"{x[0]:20}    {x[1]:12}{unit}   {round(float(x[1]/min_time),3):10}    {float(x[1])-min_time}{unit}" for x in sorted_function_result]
    # format_output.insert(
    #     0, "function name              time/op     ratio    delta")
    format_output.insert(0,
                         f"function name              time/op     ratio    delta")

    print("\n".join(format_output))

    os.remove("benchmark.test")


def GoReMod(file: str, project: str):
    lines = open(file, "r", encoding="utf-8").readlines()
    for i in range(len(lines)):
        if lines[i].find("github.com/KM911") != -1:
            items = lines[i].split("/")
            items[2] = project
            lines[i] = "/".join(items)

    # save file
    with open(file, "w", encoding="utf-8") as f:
        f.writelines(lines)


def go_router():
    Load_Go_Env()
    router_text = """"""

    get_list = []
    post_list = []

    for file in os.listdir("./router/get"):
        # if file == "commands.go":
        # continue
        # letter = file[0].upper()
        # get_list.append(f"&{letter}{file[1:-3]},\n\t")
        get_list.append(file)

    print(get_list)

def go_cli():
    Run("gen cli")
    go_mod()
    go_build()


# must replace
#  yes you are right

def go_bench():  # go test -bench
    global argv
    # print(argc, argv)
    # # for i in range(3):
    # # print(i, argv)
    # # Go_Benchmark("benchmark")
    if argc <= 3:
        Go_Benchmark("benchmark")

    else:
        for i in argv:
            Go_Benchmark(i)


def go_prof():
    # main or benchmark ????
    global argv
    if len(argv) == 0:
        pass
    # pass


def go_run():
    Load_Go_Env()
    Run(" ".join(["go", "run", "main.go"]+argv))


def go_build():
    Load_Project_Env()
    if os.name == "nt":
        go_win()
    else:
        go_linux()


def go_win():
    Load_Project_Env()
    env.update({"CGO_ENABLED": "0", "GOOS": "windows"})
    subprocess.run(["go", "build", "-ldflags", "-s -w",
                   "-o", project+".exe"], env=env)


def FileContentReplace(_src, old_s, new_s):
    # with open(_src) as f :
    # content = f.read()
    file = open(_src, "r", encoding="utf-8")
    content = file.readlines()
    file.close()

    # import re
    # regex = re.compile( old_s )
    for i in range(len(content)):
        if content[i].find(old_s) != -1:
            content[i] = content[i].replace(old_s, new_s)
            print("replace", old_s, new_s)
            # print(content[i])
# def FileContentReplaceRegex(_src)
    file = open(_src, "w", encoding="utf-8")
    file.writelines(content)
    file.close()


def FileContentReplaceRegex(_src, old_regex, new_s):
    import re

    file = open(_src, "r", encoding="utf-8")
    content = file.readlines()
    file.close()
    #  "./lib/*" --> "$(new_s)/lib/*"
    # 感觉利用regex 比较好不是吗
    # print(content[i])
    regex = re.compile(old_regex)
    for i in range(len(content)):
        regex_result = regex.search(content[i])
        if regex_result:
            # content[i] = content[i].replace(old_regex,new_s)
            # print(content[i])
            # print(regex_result)
            content[i] = content[i].replace(".", new_s)

    file = open(_src, "w", encoding="utf-8")
    file.writelines(content)
    file.close()


def ReplaceGoImport(project):
    files = os.listdir('.')
    # 文件处理
    # 以及文件夹处理
    for file in files:
        # print(files)
        if file.endswith(".go"):
            print(file)
        elif os.path.isdir(file):
            # Cd(file)
            _files = os.listdir('./'+file)
            for _file in _files:
                if _file.endswith(".go"):
                    GoReMod(file+"/"+_file, project)



def go_mod():
    # go: D:\GITHUB\KM911\template\p\gm\go.mod already exists
    Load_Project_Env()
    # 对main.go进行replace
    ReplaceGoImport(project)

    # GoReMod()

    GoProject = "github.com/"+Github_Username+"/"+project
#     只有一个文件的修改是不足以偿还的
# // 全都需要进行替换
#     FileContentReplaceRegex("main.go", "./lib/*", GoProject)
    CompletedProcess = subprocess.run(
        ["go", "mod", "init", GoProject], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if CompletedProcess.returncode == 0:
        print("go mod init success")
    else:
        print("go mod init "+GoProject)
        with open("go.mod", "r") as file:
            lines = file.readlines()
            lines[0] = "module " + GoProject + "\n"
        with open("go.mod", "w") as file:
            file.writelines(lines)

    Run("go mod tidy")


def go_import():
    global argv
    print(argv)
    if len(argv) != 2:
        print("go_import old new")
    else:
        ReplaceGoImport(argv[0], argv[1])

# TODO : create every template init ????


def go_init():

    go_mod()
    main_text = """package main
func main() {

}
"""
    file = open("main.go", "w", encoding="utf-8")
    file.write(main_text)
    file.close()


def go_hidegui():
    Load_Project_Env()
    env.update({"CGO_ENABLED": "0", "GOOS": "windows"})
    subprocess.run(["go", "build", "-ldflags",
                   "-s -w -H=windowsgui", "-o", project+".exe"], env=env)


def go_linux():
    Load_Project_Env()
    env.update({"CGO_ENABLED": "0", "GOOS": "linux"})
    subprocess.run(["go", "build", "-ldflags",
                   "-s -w", "-o", project], env=env)


def go_static():
    Load_Project_Env()
    env.update({"CGO_ENABLED": "0", "GOOS": "linux"})
    subprocess.run(["go", "build", "-ldflags",
                   "-s -w -extldflags -static", "-o", project], env=env)


def go_proxy():
    ShowCommand("go env -w GOPROXY=https://goproxy.cn,direct")


def upx():
    ShowCommand("upx *.exe")


# Rust function

def rust_build():
    Load_Project_Env()
    Run("cargo build --release")
    # move file into current directory
    Run("cp ./target/release/"+project+" ./"+project)
def rust_expand():
    Load_Project_Env()
    Run("cargo expand > main.rs")

def rust_r():
    rust_release()


def rust_release():
    Load_Project_Env()
    Run("cargo build --release")
    # move file into current directory
    Run("cp ./target/release/"+project+" ./"+project)


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




init.Parse()
# if __name__ == "__main__":
