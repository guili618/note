### cx_Oracle 模块学习笔记

### cx_Oracle 模块主要负责 Python 与 Oracle 数据库之间的联系

```python

import cx_Oracle

>>> connection = cx_Oracle.connect(r"classroom/classroom@192.168.22.235:1521/nettest")
>>> cursor = conn.cursor()
>>> cursor.execute('select sysdate from dual')
<cx_Oracle.Cursor on <cx_Oracle.Connection to classroom@192.168.22.235:1521/nettest>>
>>> result = cursor.fetchall()
>>> result
[(datetime.datetime(2017, 12, 18, 21, 49, 45),)]
>>> cursor.close()
>>> conn.close()
```

