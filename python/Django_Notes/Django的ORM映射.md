## django 的 ORM 映射
---

### 

| 操作   | 示例代码 |
| ------ | ------ |
| 创建对象但没有保存   | board = Board() |
| 保存对象（创建或更新）| board.save() |
| 在数据库中创建并保存一个对象 | Board.objects.create(name='...', description='...') |
| 列出某个类（数据库某张表）的所有对象（所有字段） | Board.objects.all() |
| 根据对象的某个属性（字段）取得值| Board.objects.get(id=1) |
