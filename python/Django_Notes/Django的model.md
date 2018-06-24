## Django的Model
***
### Model是你的数据的单一且决定性的信息来源，它包含了你存储的数据中本质的字段和行为，一般来说每个model会被映射成一张数据库的表。
- 每个model都是一个Python的类，并且都是 django.db.models.Model的子类
- 每个model的属性会成为数据库的一个字段
- 综上所述，Django为你提供了一个自动生成的数据库访问API

### 一个简单的例子
下面定义了一个 Person类，它有 first_name 和 last_name 两个属性
```python

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

```
first_name和last_name是模型的字段。每个字段都被指定为一个类属性，并且每个属性映射到一个数据库列。

上面的Person模型会像这样创建一个数据库表
```sql
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);

```
注意以下几点：
- 数据库表名称 myapp_person 自动从某些模型元数据派生，但也可以覆盖
- id字段会自动添加，但是此行为可以被覆盖
- 本例的sql语法是根据PostgreSQL来的，但值得注意的是，Django使用针对您的设置文件中指定的数据库后端定制的SQL
---
### 使用models
一旦你定义了你的模型，你需要告诉Django你要使用这些模型。通过编辑setting.py并更改INSTALLED_APPS设置来添加包含models.py的模块的名称

例如，如果您的应用程序的模型位于模块myapp.models中（由manage.py startapp脚本为应用程序创建的包结构），INSTALLED_APPS设置如下所示：

```python
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```
---
### 字段
模型中最重要的部分 - 也是模型的唯一必需部分 - 是它定义的数据库字段的列表。字段由类属性指定。小心不要选择与模型API冲突的字段名称，例如clean，save或delete

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

### 字段类型
模型中的每个字段都应该是适当的Field类的实例。 Django使用字段类类型来确定几件事情：
- 数据库表字段的类型，它告诉数据库要存储什么类型的数据（例如INTEGER，VARCHAR，TEXT）。
- 呈现表单字段时使用的默认HTML小部件
- Django管理员和自动生成的表单中使用的最小验证要求

Django带有几十种内置字段类型;您可以在模型字段参考中找到完整列表。如果Django的内置函数没有做到这一点，你可以轻松地编写自己的字段;请参阅编写定制模型字段

---
### 字段选项
每个字段都有一组特定于字段的参数（记录在模型字段参考中）。例如，CharField（及其子类）需要一个max_length参数，该参数指定用于存储数据的VARCHAR数据库字段的大小

#### null 
如果为True，Django将在数据库中将空值存储为NULL。默认值是False

#### blank
如果为True，则允许该字段为空。默认值是False

#### choices

一个可迭代的（例如，一个列表或元组）用作该字段的选择的2元组。如果这是给定的，默认表单小部件将是一个选择框而不是标准文本字段，并会限制选择给出的选择
示例如下：
```python
YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)

```