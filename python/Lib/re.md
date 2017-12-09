### 正则表达式模块 re 学习笔记

### python 中使用正则表达式步骤
- 1 用 import re  导入正则表达式模块
- 2 用 re.compile() 函数创建一个Regex对象(最好用raw string避免各种转义)
- 3 向 Regex 对象的 search() 方法传入想要查找的的字符串。它返回一个 Match 对象
- 4 调用 Match 对象的 group() 方法，返回实际匹配的文本字符串

### python中正则表达式符号对照表
| 字符           | 含义 |
| ------        | ------ |
| .             | 匹配所有的字符，换行符除外|
| ?             | 匹配 0 次或 1次  前面的分组 |
| *             | 匹配 0 次或 多次 前面的分组  |
| +             | 匹配 1 次或 多次 前面的分组  |
| {n}           | 匹配 n 次前面的分组 |
| {n,}	        | 匹配 n 次或更多次前面的分组 |
| {,m}	        | 匹配 0 次到 m 次前面的分组 |
| {n,m}         | 匹配 n 次到 m 次前面的分组 |
| ^begin        | 字符串以 begin 开头 |
| end$          | 字符串以 end 结尾 |
| \d            | 匹配 数字 |
| \w	        | 匹配 单词 |
| \s	        | 匹配 空格 |
| \D            | 匹配 “数字外” 的所有的字符 |
| \W	        | 匹配 “单词外” 的所有的字符 |
| \S	        | 匹配 “空格外” 的所有的字符 |
| [abc]         | 匹配 “方括号内” 的任意字符 |
| [^abc]	    | 匹配 “不在”  方括号内的任意字符 |

### re示例1-简单的re程序
```python
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('my number is 415-555-4242 .')
>>> print('phone number found : ' + mo.group())
phone number found : 415-555-4242
>>>
```

### re示例2-利用括号进行分组
> 正则表达式字符串中的第一对括号是第一组，第二对括号是第二组。向group()匹配对象方法传入1或者2，就可以取得匹配文本的不同部分。向group()方法传入0或者不传入参数，将返回整个匹配的文本
```python
>>> import re
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('my number is 415-555-4242 .')
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'
>>> mo.groups()             #一次性获取所有分组
('415', '555-4242')
>>> 
```


### re示例3-利用管道匹配多个分组
> 和linux中一样， 符号'|'在python 中也有管道的作用，希望匹配许多表达式中的一个的时候，就可以使用它。

```python
>>> import re
>>> langRegex = re.compile(r'golang|python')
>>> mo1 = langRegex.search('I love python .')
>>> mo1.group()
'python'
>>> mo2 = langRegex.search('I love golang .')
>>> mo2.group()
'golang'
>>> 
```

### re示例4-用问号实现可选匹配
### re示例5-用星号实现0次或多次匹配
### re示例6-用加号实现一次或多次匹配
### re示例7-用花括号匹配特定次数
### re示例8-贪心和非贪心匹配
### re示例9-findall()方法
### re示例10-字符分类
### re示例11-建立自己的字符分类
### re示例12-插入字符和美元字符
### re示例13-通配字符
### re示例14-用点-星匹配所有字符
### re示例15-用句点字符匹配换行
### re示例16-不区分大小写的匹配
### re示例17-用sub()方法替换字符串
### re示例18-管理复杂的正则表达式
### re示例19-组合使用 re.IGNORECASE,re.DOTALL,re.VERBOSE