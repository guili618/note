### python re模块笔记

### python 中使用正则表达式步骤
- 1 用 import re  导入正则表达式模块
- 2 用 re.compile() 函数创建一个Regex对象(最好用raw string)
- 3 向 Regex 对象的 search() 方法传入想要查找的的字符串。它返回一个 Match 对象
- 4 调用 Match 对象的 group() 方法，返回实际匹配的文本字符串

