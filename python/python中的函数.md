## Python中的函数
---
### 思考函数的角度
- 函数的参数，包括默认参数、位置参数、关键字参数，任意数量位置参数和任意数量关键字参数
- 函数传递和返回值
- 函数作用域
- 闭包
- 生成器
- 装饰器
- 匿名函数
### 函数的参数
- 普通的函数
```python
def func(a,b):
    return a+b
```
- 默认参数,注意默认参数不能为可变对象，若有需要，应该用None
```python
def func(name='default'):
    print(name)
======console=======
>>> func()
default
>>> func(name='input')
input
>>> 
```
- 默认参数与位置参数一起,**位置参数必须在默认参数前面**
```python
def func(arg1,name='default'):
    print(arg1)
    print(name)
======console=======
>>> func('hello')
hello
default
>>> func('hello',name='world')
hello
world
```
- 任意数量的位置参数，除第一个参数外，余下的参数组成一个tuple传入函数
```python
def func(arg1,*args):
	print(arg1)
	print(args)
======console=======	
>>> func(1)
1
()
>>> func(1,2)
1
(2,)
>>> func(1,2,3)
1
(2, 3)
```
- 关键字参数
> 使用关键字参数时，参数的顺序无关紧要，除非提供了默认值，否则必须显式的命名所有必须的函数参数
> 定义函数时，使用这种描述性的参数是个好方法
> 位置参数和关键字参数可以一起出现在函数中，但是位置参数必须先给出
```python
def func(a,b,c,d):
	print(a,b,c,d)
======console=======	
>>> func(b=2,a=1,d=4,c=3)
1 2 3 4
>>> func(1,2,d=4,c=3)
1 2 3 4
```
- 任意数量的关键字参数，使用**kwargs，这些参数会放入一个dict中，传入函数
```python
>>> def func(a,**kwargs):  ##**kwargs放在入参最后
	print(a)
	print(kwargs)

======console=======		
>>> func(1,kw1='hello',kw2='world',kw3='python')
1
{'kw1': 'hello', 'kw2': 'world', 'kw3': 'python'}
```
- 接受数量不定的位置参数和关键字参数
> 通常用来编写装饰器和代理
```python
def func(**args,**kwargs):
    pass

```
- 只接受关键字参数的函数
原理：*开头的参数只能作为最后一个位置参数出现，**开头的参数只能作为最后一个参数出现，所以*arg和\**kwargs之间仍然可以有参数，这个参数就是 keyword-only参数
- 定义1
```python
def func(a,*args,c):
    print(a)
    print(args)
    print(c)
======console=======
>>> func(1,2,3,4,5,c='keyword-only')
1
(2, 3, 4, 5)
keyword-only
```
- 定义2
```python
def func(a,*args,c,**kwargs):
    print(a)
    print(args)
    print(c)
======console=======
>>> func(1,2,3,4,5,c='keyword-only',kw1='hello',kw2='world')
1
(2, 3, 4, 5)
keyword-only
{'kw1': 'hello', 'kw2': 'world'}
```