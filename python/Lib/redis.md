### redis 模块学习笔记

### 

```python
>>> import redis
>>> r = redis.StrictRedis(host='192.168.245.130', port=6379, db=0)
>>> r.set('hello','world')
True
>>> r.get('hello')
b'world'
>>> r.set('count',1)
True
>>> r.incr('count')
2
>>> r.incr('count')
3
>>> r.decr('count')
2
>>> r.get('count')
b'2'
>>> r.set('count',123456789012345678901234567890)
True
>>> r.incr('count')
redis.exceptions.ResponseError: value is not an integer or out of range
>>> r.rpush('hispanic', 'uno')
1
>>> r.rpush('hispanic', 'dos')
2
>>> r.rpush('hispanic', 'tres')
3
>>> r.rpush('hispanic', 'cuatro')
4
>>> r.llen('hispanic')
4
>>> r.lindex('hispanic', 3)
b'cuatro'
>>> 

```