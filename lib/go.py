import sys
import os
import subprocess
# from import init import *

import init


def Load_Go_Env():
    init.init.Load_Project_Env()
    global mod
    mod = open("go.mod", "r").readline().split(" ")[
        1].strip()


def go_test():
    Load_Go_Env()
    init.init.Run(" ".join(["go", "test", "-v", mod+"/test"]))

# 一个大问题 它不会显示 关于内存占用的部分
# 131072 B/op 1 allocs/op


def go_gen():
    Load_Go_Env()
    init.init.Run("go generate")
    go_build()


def go_bin():
    Load_Go_Env()
    go_build()
    init.init.Run("mv -f "+project + " /usr/bin/" + project)


def Go_Benchmark(package: str):
    Load_Go_Env()
    init.Cd(package)
    command = " ".join(
        ["go", "test", "-c", "-o", "benchmark.test", mod+"/"+package])
    init.init.Run(command)
    command = " ".join([init.ExecutePathConvent("benchmark.test"),
                       "-test.benchmem", "-test.bench",  "."])

    result = init.CommandResult(command).split("\n")[4:-2]
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
    init.init.Run("gen cli")
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
    if init.argc <= 3:
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
    init.init.Run(" ".join(["go", "run", "main.go"]+argv))


def go_build():
    init.init.Load_Project_Env()
    if os.name == "nt":
        go_win()
    else:
        go_linux()


def go_win():
    init.Load_Project_Env()
    init.init.env.update({"CGO_ENABLED": "0", "GOOS": "windows"})
    subprocess.run(["go", "build", "-ldflags", "-s -w",
                   "-o", init.project+".exe"], env=init.env)


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
    init.Load_Project_Env()
    # 对main.go进行replace
    ReplaceGoImport(init.project)

    # GoReMod()

    GoProject = "github.com/"+init.Github_Username+"/"+init.project
#     只有一个文件的修改是不足以偿还的
# // 全都需要进行替换
#     FileContentReplaceRegex("main.go", "./lib/*", GoProject)
    CompletedProcess = subprocess.run(
        ["go", "mod", "init", GoProject], env=init.env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if CompletedProcess.returncode == 0:
        print("go mod init success")
    else:
        print("go mod init "+GoProject)
        with open("go.mod", "r") as file:
            lines = file.readlines()
            lines[0] = "module " + GoProject + "\n"
        with open("go.mod", "w") as file:
            file.writelines(lines)

    init.Run("go mod tidy")


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
    init.Load_Project_Env()
    init.env.update({"CGO_ENABLED": "0", "GOOS": "windows"})
    subprocess.run(["go", "build", "-ldflags",
                   "-s -w -H=windowsgui", "-o", init.project+".exe"], env=init.env)


def go_linux():
    init.Load_Project_Env()
    init.env.update({"CGO_ENABLED": "0", "GOOS": "linux"})
    subprocess.run(["go", "build", "-ldflags",
                   "-s -w", "-o", init.project], env=init.env)


def go_static():
    init.Load_Project_Env()
    init.env.update({"CGO_ENABLED": "0", "GOOS": "linux"})
    subprocess.run(["go", "build", "-ldflags",
                   "-s -w -extldflags -static", "-o", init.project], env=init.env)


def go_proxy():
    init.ShowCommand("go env -w GOPROXY=https://goproxy.cn,direct")
