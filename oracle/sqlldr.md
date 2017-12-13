### Oracle SQL*Loader 学习笔记

### SQL*Loader 在 Oracle 第七版中引入，用来提供数据加载的功能
- 在 windows 下命令为 SQLLDR
- 在 Uniux/Linux 下命令为 sqlldr

### 编写 loader.ctl 控制文件
```sql
load data
 infile '/path/filename'  -- 指定需要导入的文件
 into table table_name
 fields terminated by "," optionally enclosed by '"'		  
 ( col1,col2,... )
```
### 使用 sqlldr 命令进行数据的加载

```sql
 sqlldr username/password@server control=loader.ctl
```