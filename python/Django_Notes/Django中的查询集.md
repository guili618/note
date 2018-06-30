## Django 中的查询集
---
### 查询操作
一旦创建了数据模型，Django就会自动为您提供一个数据库抽象API，使您可以创建，检索，更新和删除对象。本文档介绍了如何使用此API。有关所有各种模型查找选项的完整详细信息，请参阅 data model reference。 在本指南（和参考文献）中，我们将参考以下模型，它们构成了一个Weblog应用程序：

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

```

### 创建对象
为了在Python对象中表示数据库表数据，Django使用直观的系统：模型类表示数据库表，该类的实例表示数据库表中的特定记录。

要创建对象，请使用模型类的关键字参数对其进行实例化，然后调用save（）将其保存到数据库中

假设模型存在于/blog/models.py文件中，这是一个例子：

```python

>>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()

```

这在幕后执行INSERT SQL语句。在您明确调用save（）之前，Django不会访问数据库

save（）方法没有返回值。

>  save（）还有许多此处未描述的高级选项。有关完整的详细信息，请参阅save（）的文档。 要在一个步骤中创建和保存对象，请使用create（）方法。

###　保存对对象的更改
要保存对数据库中已有对象的更改，请使用save（）。

给定一个已经保存到数据库的Blog实例b5，这个例子改变它的名字并更新它在数据库中的记录：

```python 
>>> b5.name = 'New name'
>>> b5.save()
```
这会在幕后执行UPDATE SQL语句。直到你显式地调用save（）之前，Django才会打到数据库。

### 保存ForeignKey和ManyToManyField字段

更新ForeignKey字段的方式与保存普通字段的方式完全相同 - 只需将正确类型的对象分配给相关字段即可。此示例更新Entry实例条目的博客属性，假设Entry和Blog的适当实例已保存到数据库（所以我们可以在下面检索它们）：
```python 
>>> from blog.models import Blog, Entry
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog
>>> entry.save()
```
更新ManyToManyField的工作方式有点不同 - 使用该字段上的add（）方法将记录添加到关系中。此示例将Author实例joe添加到条目对象：
```python 
>>> from blog.models import Author
>>> joe = Author.objects.create(name="Joe")
>>> entry.authors.add(joe)

```
要一次将多个记录添加到ManyToManyField，请在add（）的调用中包含多个参数，如下所示：
```python 
>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> entry.authors.add(john, paul, george, ringo)
```

### 检索对象

要从数据库中检索对象，请在您的model class上通过Manager构建一个QuerySet。

QuerySet表示数据库中的对象集合。它可以有零个，一个或多个过滤器。过滤器根据给定的参数缩小查询结果的范围。在SQL术语中，QuerySet等同于SELECT语句，过滤器是限制性子句，如WHERE或LIMIT。


您可以使用模型的Manager获取QuerySet。每个模型至少有一个管理器，默认情况下称为对象。通过模型类直接访问它，如下所示：
```python 
>>> Blog.objects
<django.db.models.manager.Manager object at ...>
>>> b = Blog(name='Foo', tagline='Bar')
>>> b.objects
Traceback:
    ...
AttributeError: "Manager isn't accessible via Blog instances."
```
> Manager 只能通过模型​​类访问，而不能通过模型​​实例访问，以实现“表级”操作和“记录级”操作之间的分离

Manager是模型的QuerySets的主要来源。例如，Blog.objects.all（）返回一个QuerySet，其中包含数据库中的所有Blog对象。
#### 检索所有对象

从表中检索对象的最简单方法是获取所有对象。为此，请使用Manager上的all（）方法：

```python 
all_entries = Entry.objects.all()
```

```python 

```

```python 

```

```python 

```

```python 

```

```python 

```

```python 

```

```python 

```


```python 

```

```python 

```

```python 

```

```python 

```

```python 

```

```python 

```

```python 

```

```python 

```