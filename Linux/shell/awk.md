## awk是一设计用于数据流的工具，它可以对行和列进行操作，并且有很多内建的功能，如数组、函数
***
### awk的脚本的基本结构由三部分组成(三个部分都是可选项，脚本中可省略任意部分)
- BEGIN
- END
- 带模式匹配选项的常见语句块
***
### 基本结构示例如下
```sh
$ awk 'BEGIN {print "start"} pattern { commands } END {print "end"}' file

```
***
### awk的选项如下:
| 选项           | 描述 |
| ------        | ------ |
| -F fs         | 指定行中划分数据字段的字段分隔符 |
| -f file       | 从指定的文件中读取程序 |
| -v var=value  | 定义awk程序中的一个变量及默认值 |
| -mf N	        | 指定要处理的数据文件中最大的字段数 |
| -mr N	        | 指定数据文件中的最大数据行 |
| -w 	        | 指定awk的兼容模式或者警告等级 |

***
### awk的命令工作方式如下:
- 执行 BEGIN { commands } 语句块中的语句
- 从文件或者stdin中读取一行，然后执行 pattern { commands },重复这个过程，直到文件全部被读取完毕
- 当读至输入流末尾时，执行 END { commands }
- awk 以 ‘行’ 为一次处理的单位，而以 ‘字段’ 为最小的处理单位

### awk内建变量如下:

| 变量名称 | 含义 |
| ------ | ------ |
| $0     | 当前记录 ( 这个变量中存放着整个行的内容 ) |
| $1~$n  | 当前记录的第n个字段，字段间由FS分隔 |
| FS	 | 输入字段分隔符 默认是空格或Tab |
| NF	 | 当前记录中的字段个数，就是有多少列 |
| NR	 | 已经读出的记录数，就是行号，从1开始，如果有多个文件话，这个值也是不断累加中。|
| FNR	 | 当前记录数，与NR不同的是，这个值会是各个文件自己的行号|
| RS	 | 输入的记录分隔符， 默认为换行符 |
| OFS	 | 输出字段分隔符， 默认也是空格 |
| ORS	 | 输出的记录分隔符，默认为换行符 |
| FILENAME| 当前输入文件的名字 |
***
### awk 示例1--利用变量
- $0 代表整一行
- $1 代表第一个字段.
- $2 代表第二个字段.
- $n 代表第三个字段.
```bash
$ echo 'Welcome to awk command tutorial' | awk '{print $1,$2}'
Welcome to

```
***
### awk 示例2--指定分割符号
```bash
$ awk -F: '{print $1}' /etc/passwd #这里指定冒号为分隔符

root
daemon
bin
sys
sync
games
man
lp
mai
...
```
***
### awk 示例3--多个命令用分号隔开
```bash
$ echo "Hello World" | awk '{$2="Python"; print $0}'
Hello Python
```
***
### awk 示例4--从awk脚本中读取命令
```bash
$ cat awktestfile 
{print $1 " home at " $6}

$ awk -F: -f awktestfile /etc/passwd
root home at /root
daemon home at /usr/sbin
bin home at /bin
sys home at /dev
sync home at /bin
games home at /usr/games
man home at /var/cache/man
...
```
***
### awk 示例5--awk的预处理和尾处理

```bash
$ awk 'BEGIN {print "The File Contents:"} {print $0}' myfile

$ awk 'BEGIN {print "The File Contents:"} {print $0} END {print "File footer"}' myfile
$ cat awkprocess 
BEGIN {
 
print "Users and their corresponding home"
 
print " UserName \t HomePath"
 
print "___________ \t __________"
 
FS=":"
 
}
 
{
 
print $1 "  \t  " $6
 
}
 
END {
 
print "The end"
 
}

$ awk -f awkprocess /etc/passwd
Users and thier corresponding home
 UserName 	 HomePath
___________ 	 __________
root  	  /root
daemon  	  /usr/sbin
bin  	  /bin
sys  	  /dev
sync  	  /bin
games  	  /usr/games
man  	  /var/cache/man
lp  	  /var/spool/lpd
mail  	  /var/mail
news  	  /var/spool/news
uucp  	  /var/spool/uucp
proxy  	  /bin

```
***
### awk 示例6--内建变量的使用
| 变量名称 | 含义 |
| ------ | ------ |
| FS-- Specifies the field separator.	 | 输入字段分隔符，默认是空格或Tab |
| RS--Specifies the record separator.	 | 输入记录分隔符， 默认为换行符 |
| OFS--Specifies the Output separator.	 | 输出字段分隔符， 默认也是空格 |
| ORS--Specifies the Output separator.	 | 输出的记录分隔符，默认为换行符 |

```bash
$  awk 'BEGIN{FS=":"; OFS="-"} {print $1,$6,$7}' /etc/passwd
root-/root-/bin/bash
daemon-/usr/sbin-/usr/sbin/nologin
bin-/bin-/usr/sbin/nologin
sys-/dev-/usr/sbin/nologin
sync-/bin-/bin/sync
games-/usr/games-/usr/sbin/nologin
man-/var/cache/man-/usr/sbin/nologin
lp-/var/spool/lpd-/usr/sbin/nologin
mail-/var/mail-/usr/sbin/nologin
news-/var/spool/news-/usr/sbin/nologin
uucp-/var/spool/uucp-/usr/sbin/nologin
proxy-/bin-/usr/sbin/nologin
...
```
***
### awk 示例7
```bash

```
***
### awk 示例8
```bash

```
***
### awk 示例9
```bash

```
***
### awk 示例7
```bash

```
***
### awk 示例8
```bash

```
***
### awk 示例9
```bash

```
***