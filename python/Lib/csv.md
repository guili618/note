### CSV 模块学习笔记

### CSV 是 Comma-Separated Values 的缩写， CSV 文件中的每行代表电子表格中的一行，都好分割了该行中的单元格。

### CSV 文件有以下的特点
- 值没有类型，所有的东西都是字符串
- 没有字体大小或颜色的设置
- 没有多个工作表
- 不能指定单元格的宽度和高度
- 不能合并单元格
- 不能嵌入图像或图表

### Reader 对象
- 要从 csv 文件中读取数据，要创建一个 Reader 对象，它可以让你迭代遍历 csv 文件中的每一行
- 用 open 函数打开文件，这将返回一个 Reader 对象
- 注意不能直接把文件名的字符串传递给 csv.reader() 函数
- 在这个 Reader 对象上应用 list() 函数，将返回一个列表的列表，可以将它保存在变量 data 中
- 最后用 data[row][col] 来访问特定行和列的值，中 row 是data 中一个列表的下标， col是该列表中你想访问的项的下标
```python
>>> import csv
>>> file = open(r'D:\\example.csv')
>>> filereader = csv.reader(file)
>>> filereader
<_csv.reader object at 0x0000000002FA49A0>
>>> data = list(filereader)
>>> data
[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'], ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'], ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'], ['4/10/2015 2:40', 'Strawberries', '98']]
>>> 

```