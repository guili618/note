## Python 中的面向对象编程
---
### 面向对象编程的思考切入角度
- 以粘合对象的状态和操作为起点
---
### 面向对象编程的要素、
- 封装
- 继承 
- 多态
---
### Python中的类 class 和 对象 object ( 实例 instance )
#### 对象的思考角度
- 对象的属性
- 对象的行为
#### 问题：
- 类如何创建对象？
- 对象如何初始化？
- 类属性与实例属性的对比
- 类方法与实例方法的对比
- bound method 和 unbound method 的对比
- classmethod 和 staticmethod 的对比
- property是什么，如何应用
- 抽象类
- 抽象方法

```python
class Hero:
    
    species = 'Attack Damage' #class attributes
  # Ability Power

    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print("My name is " + self.name)
```

---
### Python中的继承
---
### Python中的 duck typing
---
### Python中的运算符