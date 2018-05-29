## django 的 ORM 映射
---

### 

| 操作           | 示例代码 |
| ------        | ------ |
| Create an object without saving        | board = Board() |
| -f fileSave an object (create or update)       | board.save() |
| Create and save an object in the database  | Board.objects.create(name='...', description='...') |
| List all objects	        | Board.objects.all() |
| Get a single object, identified by a field	        | Board.objects.get(id=1) |
| -w 	        | 指定awk的兼容模式或者警告等级 |