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