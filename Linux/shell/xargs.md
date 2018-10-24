## xargs 笔记
***
### 工作原理：
####  我们可以用管道 "|" 将一个命令的 stdout 重定向到另一个命令的 stdin
如
```bash
$ ps -ef | grep python
```
但是有些命令只能以命令行参数的形式接收参数，无法通过stdin接受数据流
####  xargs可以将stdin转换为命令行参数，也可以将单号或者多行的文本输入转换为其他格式

---
```bash

ps aux | grep PROCESS | grep -v grep | awk '{print $2}' | xargs kill -9

```

### 

```bash
$ echo 'hello hello hello hello hello hello' | xargs -n 2
hello hello
hello hello
hello hello

```

```bash
find . -name '*.py' -print0 | xargs -0 grep 'something' > output.txt


find . -name '*.py' -exec grep 'something' {} \; > output.txt
```