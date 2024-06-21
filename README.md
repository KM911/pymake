
>[!faq] 解决了什么问题 ? 
>1.兼容性问题. 虽然Windows上可以通过安装 `mingw32` 支持make,但是非常多的命令还是不兼容
>2.字符串处理增强. 还有什么是比python的字符串处理要更好的呢? 

>[!warning] 舍弃了makefile的本意 -- 为C提供增量编译

>[!tip] 使用 alise 解决python xxx.py  argv过于繁琐的问题 
>

>[!note] 脚本集合 
>或许我不应该称其为pymake,其充其量就是一个脚本集合. 

>[!done] 一些约定 
>1. 大写函数是给内部使用的.小写的才是用于导出的
>2. 为了解决makefile无法传递参数的问题,例如 make run build 会执行 run 和 build 命令,而不是将build作为run的参数. 
>3. 优化长命令的输入体验
>4. m image build 
>5. m go bench argv ... 

>[!others] 当然了你也可以使用 m go_bench 来执行命令. 


>[!TODO] TODO 
>- [ ] 添加更多的typo检测
>- [x] go benchmark format 



## Problem I meet 

1. python file grow quick , the single file is  not suitable for project. 
2. python can not modify other mod variable 

python can not change variable dirctrily, only could by function call and do not modify the variable actualy


rebuild it will go / rust 


## rebuild

1. 核心 python eval 可以将 string 作为代码执行. 例如 eval("help()") 或者 eval("a=list()") 
2. 参数传递问题. makefile can not pass args . 