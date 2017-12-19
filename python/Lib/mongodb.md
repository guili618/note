### PyMongo 模块学习笔记

```python
>>> import pymongo
>>> client = pymongo.MongoClient('192.168.245.130', 27017)
>>> db = client.test
>>> db.name
'test'



```