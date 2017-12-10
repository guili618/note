### excel 表格处理模块 openpyxl 模块学习笔记

### openpyxl 模块使用步骤
- 1 导入 openpyxl 模块
- 2 调用 openpyxl.load_workbook() 函数
- 3 取得 Workbook 对象
- 4 调用 get_active_sheet() 或 get_sheet_by_name() 工作簿方法
- 5 取得 Worksheet 对象
- 6 使用索引或者工作表的 cell() 方法，带上 row 和 column 关键字参数
- 7 取得 Cell 对象
- 8 读取 Cell 对象的 value 属性

### 示例1-用 openpyxl 模块打开 excel 文档
>openpyxl.load_workbook() 函数接受文件名，返回一个 workbook 数据类型的值，这个 workbook 对象代表这个 excel 文件


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook(r'D:\\example.xlsx')
>>> type(wb)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> wb.get_active_sheet()    #取得工作簿的活动表，即 excel 打开时出现的工作表
<Worksheet "Sheet1">
>>> wb.get_sheet_names()     #取得工作簿中所有表名的列表
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet_2 = wb.get_sheet_by_name('Sheet2') #每个表由一个Worksheet 对象表示,通过向 get_sheet_by_name() 方法传入表名获得
>>> sheet_2
<Worksheet "Sheet2">
>>> sheet_2.title
'Sheet2'
>>> 
```

