### sed 被称作为 流编辑器(stream editor),它在处理数据之前基于预先提供的一组规则来编辑数据流

### sed特点如下:
- 本身是一个管道命令，可以用来分析 standard input
- 可以将数据进行替换，删除，新增，选取特定行等功能
### sed 命令结构如下：
```sh
$ sed [-nefr] 动作
$ sed options file
```
### sed 命令参数说明如下

| 参数   | 描述 |
| ------| ------ |
| -n    | 使用安静 silent 模式，在一般sed用法中，所有来自STDIN的数据一般都会被列出屏幕上，但如果加上 -n 参数后，则只有经过sed 特殊处理的 那一行(或操作)才会被列出来 |
| -e    | 直接在命令行模式上进行 sed 动作编辑 |
| -f    | 直接将 sed 的动作写在一个文件内，-f filename 则可以执行filename 内的sed 动作 |
| -r    | sed 的动作支持的是扩展型正则表达式的语法(默认是基础正则表达式语法) |
| -i    | 直接修改读取文件内容，而不是由屏幕输出 |


### sed模式解析
```sh
sed -i 's/original/new/g' file.txt
```
解释:
- sed = Stream EDitor
- -i = 就地修改，将替换结果应用于原文件

- s = 表示替换命令  substitute command
- original = 正则表达式 (或者被替换的字符串本身)
- new = 想要被替换的字符串
- g = 全局替换 (替换所有的匹配行)
- file.txt = 文件名称
### 示例1 -- 文本替换

```bash

$ echo "Welcome to LikeGeeks page" | sed 's/page/website/'
Welcome to LikeGeeks website

```
- 默认替换第一个匹配
```bash
$ echo "hello hello wotld hello" | sed  's/hello/sed/'
sed hello wotld hello
```
- 全局替换
```bash
$ echo "hello hello wotld hello" | sed  's/hello/sed/g'
sed sed wotld sed
```
- 从第N处开始匹配
```bash
$ echo "hello hello wotld hello hello" | sed  's/hello/sed/1g'
sed sed wotld sed sed
$ echo "hello hello wotld hello hello" | sed  's/hello/sed/2g'
hello sed wotld sed sed

$ echo "hello hello wotld hello hello" | sed  's/hello/sed/3g'
hello hello wotld sed sed

$ echo "hello hello wotld hello hello" | sed  's/hello/sed/4g'
hello hello wotld hello sed

```
```bash
$ cat sed.txt
sed
sed
sed

awk
awk
awk

replace
replace
replace

$ cat sed.txt | sed 's/sed/replace-str/g'
replace-str
replace-str
replace-str

awk
awk
awk

replace
replace
replace

```
### 示例2 -- 替换文件内容并保存至原文件

- 
```bash
$ sed -i 's/awk/replace_str/g' sed.txt 

```