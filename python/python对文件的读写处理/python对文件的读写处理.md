### Python 对文件的读写处理
---
##### open()函数说明
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

使用open()函数打开文件，主要关注2个参数，file和mode，file指文件的路径，可相对路径，也可绝对路径，mode指打开文件的方式，说明如下：

<<<<<<< HEAD
<<<<<<< HEAD
| 字符串           | 含义 |
=======
| 字符串         | 含义 |
>>>>>>> 80904a0511ec04254ac4ed67745af0b7d313eb7b
=======
| 字符串         | 含义 |
>>>>>>> 80904a0511ec04254ac4ed67745af0b7d313eb7b
| ------        | ------ |
| r             | 读取模式，默认|
| w             | 写入模式，注意，会先清空内容 |
| x             | 只有文件不存在时才创建文件并打开为写入模式，若文件已经存在会引发 FileExitError  |
| a             | 附加模式，若文件已存在，写入内容会附加到文件尾端  |
| b             |  二进制模式|
| t	            | 文本模式，默认 |
| +	            | 更新模式(读取与写入) |
