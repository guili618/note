grep 基本用法：

```bash
grep [-acniv] [-A] [-B]  [--color=auto] '查找字符串' filename

-a 将binary文件以text文件的方式查数据

-c 计算查找到 '字符串' 的次数

-i 忽略大小写的不同

-n 顺便输出行号

-v 反向选择，即显示出没有找到 '字符串' 内容的那一行

-A 后面加数字，为after的意思，除了该行外，后续的 n 行也列出来
 
-B 后面加数字，为before的意思，除了该行外，前面的 n 行也列出来

```
grep 示例：
```bash
grep -n 't[ae]st' filename  #[]中为一个待查找的字符，该句意为查找tast或test

grep -n '[^b]ook'  # ^为反向选择，该句意为不要开头为b的字符

[^a-z] 不要小写字母 注意跟语系有关
[^A-Z] 不要大写字母 注意跟语系有关
[^0-9] 不要数字


grep -n '^the' filename #查找开头为the的字符串，^在[]外为行首字符

grep -v "^#"  filename   #看没被注释的内容

egrep -v "^#|^$" filename  #看没被注释的内容,且跳过空行

```