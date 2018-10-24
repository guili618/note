## find命令学习笔记
---
### find命令工作方式如下：沿着文件层次结构向下遍历，匹配符合条件的文件，执行响应的操作

### 示例1 --  find . -print
```sh
$ find . -print
```
> -print指明打印出匹配文件的文件名（路径），当使用-print时，'\n'作为用户对输出的文件名进行分隔
> -print0指明使用 '\0' 作为匹配的文件名之间的定界符

### 示例2 -- 根据文件名或正则表达式进行搜索

```
$ find ./ -name "*.sh" -print

```
### 示例3 -- 根据多条件匹配搜索

```sh
$ find . \( -name "*.txt" -o -name "*.pdf" \) -print

```

### 示例4 -- 根据-path参数进行文件路径匹配
```sh
$ find /home/users -path "*/slynux/*" -print

/home/users/list/slynux.txt
/home/users/slynux/eg.css

```

### 示例5 -- 根据-regex参数进行正则表达式匹配

```sh
$ ls
new.PY next.jpg test.py
$ find . -regex ".*\(\.py\|\.sh\)$"
./test.py

-i 表示忽略大小写
$ find . -iregex ".*\(\.py\|\.sh\)$"
./test.py
./new.PY

```

### 示例6 -- 根据否定参数! 进行匹配

```sh
$ ls
list.txt new.PY new.txt next.jpg test.py

$ find . ! -name "*.txt" -print
.
./next.jpg
./test.py
./new.PY

```
> 上面的命令匹配不以txt结尾的文件