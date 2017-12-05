## fnmatch 模块专门用来进行文件名匹配，支持使用通配符进行字符串匹配

### fnmatch 只有4个函数:
- fnmatch:      判断文件名是否符合特定的模式
- fnmatchcase: 判断文件名是否符合特定的模式，不区分大小写
- filter:       返回输入列表中，符合特定模式的文件名列表
- translate:    将通配符模式转为正则表达式

### fnmatch支持以下通配符

| 通配符 | 含义 |
| ------ | ------ |
| *          | 匹配任何数量的字符 |
| ? | 匹配单个字符 |
| [seq] | 匹配seq中的字符|
| [!seq] | 匹配除了seq以外的任何字符 |



fnmatch.fnmatch示例
```python
import os
import fnmatch
path = pathname
pattern_1 = '[a-z][!0-9]*xls?'
for files in os.listdir(path):    
    if fnmatch.fnmatch(files,pattern_1):
        print(files)
```

```python
# 利用os.walk(),fnmatch,generators
# 在目录中寻找文件

def findall(topdir,pattern):
    for path,dirs,files in os.walk(topdir):
        for name in files:
            if fnmatch.fnmatch(name,pattern):
                yield os.path.join(path,name)


```