## Python 对 CSV 文件的处理
---

### CSV 是 Comma Separated Values(逗号分隔的值)的简称,是一种用与电子表格和数据库之间的交换格式，因为在制定标准之前，CSV已经通用多年，使得不用应用程序在处理CSV时存在细微的差异性，如 delimier (分隔符)、 quoting character (引号字符)、换行字符等不同。尽管如此，CSV格式依然具有足够的通用性
- 文本文件,容易读写
- 可以被多种程序和数据库支持
- 每行代表电子表格中的一行，逗号分割了该行中的单元格
- **值没有类型，所有东西都是字符串**
- 没有字体大小或颜色的的设置
- 没有多个工作表
- 不能指定单元格的宽度和高度
- 不能合并单元格
- 不能嵌入图像或图表
---
### 示例1--读取并打印出csv数据
- 要从CSV文件读取数据，需要创建一个Reader对象，它可以让你迭代遍历CSV文件的每一行
- 打开文件时最好显式的指定文件路径，用**with open(filename) as csv_file** 比直接open好
- **不能直接的把文件名字符串传给csv.reader()函数**


```python
>>> import csv
>>> csv_file = open(r'example.csv') #最好显示加上文件的绝对路径
>>> csv_file
<_io.TextIOWrapper name='example.csv' mode='r' encoding='cp936'>
>>> csv_reader = csv.reader(csv_file) #
>>> csv_reader
<_csv.reader object at 0x0000000003197F50>
>>> csv_data = list(csv_reader)
>>> csv_data
[['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'], ['4/6/2014 12:46', 'Pears', '14'], ['4/8/2014 8:59', 'Oranges', '52'], ['4/10/2014 2:07', 'Apples', '152'], ['4/10/2014 18:10', 'Bananas', '23'], ['4/10/2014 2:40', 'Strawberries', '98']]
>>> for data in csv_data:
	print(data)
	
['4/5/2014 13:34', 'Apples', '73']
['4/5/2014 3:41', 'Cherries', '85']
['4/6/2014 12:46', 'Pears', '14']
['4/8/2014 8:59', 'Oranges', '52']
['4/10/2014 2:07', 'Apples', '152']
['4/10/2014 18:10', 'Bananas', '23']
['4/10/2014 2:40', 'Strawberries', '98']

>>> csv_data[0][0]
'4/5/2014 13:34'
>>> csv_data[0][1]
'Apples'
>>> csv_data[0][2]
'73'
>>> csv_data[1][1]
'Cherries'
>>> csv_data[6][1]
'Strawberries'

```
---

### 示例2--打开大型CSV文件
- 对于大型文件，最好在一个for循环中打开reader对象，避免一次性将文件装入内存
- 用 with open 代替 open
- reader对象只能循环遍历一次，要再次读取csv文件，必须调用csv.reader,创建一个对象
```python

import csv
>>> with open(r'example.csv') as csv_file:
	for row in csv.reader(csv_file):
		print('Row No.' + str(csv_reader.line_num) + ' --> ' + str(row))

		
Row No.1 --> ['4/5/2014 13:34', 'Apples', '73']
Row No.2 --> ['4/5/2014 3:41', 'Cherries', '85']
Row No.3 --> ['4/6/2014 12:46', 'Pears', '14']
Row No.4 --> ['4/8/2014 8:59', 'Oranges', '52']
Row No.5 --> ['4/10/2014 2:07', 'Apples', '152']
Row No.6 --> ['4/10/2014 18:10', 'Bananas', '23']
Row No.7 --> ['4/10/2014 2:40', 'Strawberries', '98']

```
---

### 示例3--写入CSV文件

```python
import csv

```