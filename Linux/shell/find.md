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

### 示例6 -- 根据目录的深度搜索
- maxdepth表示find搜索的最大深度
- mindepth表示find搜索的最小深度
  
```sh
$ find . -maxdepth 1 -name "f*" -print

$ find . -mindepth 2 -name "f*" -print
./dir1/dir2/file1
./dir3/dir4/f2
```
> -maxdepth和-mindepth应该作为find的第三个参数出现，不然会影响效率

### 示例7 -- 根据文件的类型进行搜索

| 文件类型 | 类型参数 |
| ------  | ------ |
| 普通文件  | f |
| 符号链接  | l |
| 目录  | d |
| 字符设备  | c |
| 块设备  | b |
| socket  | s |
| FIFO  | p |

```sh
列出目录
$ find . -type d -print 
列出普通文件
$ find . -type f -print
列出符号链接
$ find . -type l -print

```

### 示例8 -- 根据文件时间进行搜索

| 时间 | 含义 |
| ------  | ------ |
| -atime  | 用户最后一次访问文件的时间 （单位：天） |
| -mtime  | 文件内容最后一次被修改的时间 （单位：天） |
| -ctime  | 文件元数据（例如权限或所有权）最后一次改变的时间（单位：天） |
| -amin | 用户最后一次访问文件的时间 （单位：分钟） |
| -mmin | 文件内容最后一次被修改的时间 （单位：分钟） |
| -cmin | 文件元数据（例如权限或所有权）最后一次改变的时间（单位：分钟） |
- mtime +7 大于七天
- mtime -7 小于七天
```sh
最近7天内被访问过的文件
$ find . -type f -atime -7 -print
恰好7天前被访问过的文件
$ find . -type f -atime 7 -print
访问时间超过7天的文件
$ find . -type f -atime +7 -print
```
