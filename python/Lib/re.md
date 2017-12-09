### 正则表达式模块 re 学习笔记

### python 中使用正则表达式步骤
- 1 用 import re  导入正则表达式模块
- 2 用 re.compile() 函数创建一个Regex对象(最好用raw string)
- 3 向 Regex 对象的 search() 方法传入想要查找的的字符串。它返回一个 Match 对象
- 4 调用 Match 对象的 group() 方法，返回实际匹配的文本字符串

### re示例1-简单的re程序
```python
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('my number is 415-555-4242 .')
>>> print('phone number found : ' + mo.group())
phone number found : 415-555-4242
>>>
```

### re示例-利用括号进行分组
> 正则表达式字符串中的第一对括号是第一组，第二对括号是第二组
> 向group()匹配对象方法传入1或者2，就可以取得匹配文本的不同部分
> 向group()方法传入0或者不传入参数，将返回整个匹配的文本
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