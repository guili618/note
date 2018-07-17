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
all（）方法返回数据库中所有对象的QuerySet。

#### 使用过滤器检索特定的对象

all（）返回的QuerySet描述数据库表中的所有对象。但是，通常情况下，您只需要选择完整对象集的一部分。 要创建这样的子集，可以优化初始QuerySet，添加过滤条件。

优化QuerySet的两种最常用方法是： 
- filter（** kwargs） 返回包含匹配给定查找参数的对象的新QuerySet。 
- 排除（** kwargs） 返回包含与给定查找参数不匹配的对象的新QuerySet。 
查找参数（上述函数定义中的** kwargs）应采用以下字段查找中描述的格式。 例如，要获取2006年的博客条目的QuerySet，请使用filter（），如下所示：
```python 
Entry.objects.filter(pub_date__year=2006)

```
如果使用默认管理器类，它与以下内容相同：
```python 
Entry.objects.all().filter(pub_date__year=2006)

```
#### 链接过滤器
精炼QuerySet的结果本身就是一个QuerySet，因此可以将精化链接在一起。例如：
```python 
>>> Entry.objects.filter(
...     headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(
...     pub_date__gte=datetime.date(2005, 1, 30)
... )
```
这将获取数据库中所有条目的初始QuerySet，添加过滤器，然后是排除，然后是另一个过滤器。最终结果是一个QuerySet，其中包含标题以“What”开头的所有条目，这些条目在2005年1月30日和当天发布。

#### Filtered QuerySets是唯一的
每次您完善QuerySet时，都会获得全新的QuerySet，它绝不会绑定到以前的QuerySet。每个优化都会创建一个独立且不同的QuerySet，可以存储，使用和重用。 例：
```python 

>>> q1 = Entry.objects.filter(headline__startswith="What")
>>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
>>> q3 = q1.filter(pub_date__gte=datetime.date.today())

```
这三个QuerySet是分开的。第一个是包含所有包含以“What”开头的标题的条目的QuerySet。第二个是第一个的子集，另外还有一个标准排除pub_date是今天或将来的记录。第三个是第一个的子集，附加标准只选择pub_date是今天或将来的记录。初始QuerySet（q1）不受精化过程的影响。


#### QuerySets 是惰性的
创建QuerySet的操作不涉及任何数据库活动。您可以整天将过滤器堆叠在一起，在评估QuerySet之前，Django实际上不会运行查询。看看这个例子：
```python 
>>> q = Entry.objects.filter(headline__startswith="What")
>>> q = q.filter(pub_date__lte=datetime.date.today())
>>> q = q.exclude(body_text__icontains="food")
>>> print(q)
```

虽然这看起来像三个数据库命中，但实际上它只在最后一行（print（q））处命中数据库一次。一般来说，直到你“询问”它们之前，QuerySet的结果都不会从数据库中获取。当你这样做时，通过访问数据库来评估QuerySet。有关确切何时进行评估的更多详细信息，请参阅何时评估QuerySet。
#### 用get（）检索单个对象

即使只有一个对象与查询匹配，filter（）将始终为您提供一个QuerySet - 在这种情况下，它将是包含单个元素的QuerySet。

如果您知道只有一个对象与您的查询匹配，则可以在Manager上直接使用返回对象的get（）方法：
```python 

>>> one_entry = Entry.objects.get(pk=1)


```
您可以使用get（）来使用任何查询表达式，就像使用filter（）一样 - 再次请参阅下面的Field lookups。

请注意，使用get（）和使用带有[0]切片的filter（）之间存在差异。如果没有匹配查询的结果，则get（）将引发DoesNotExist异常。此异常是正在执行查询的模型类的属性 - 因此在上面的代码中，如果没有主键为1的Entry对象，则Django将引发Entry.DoesNotExist。

同样，如果多个项目与get（）查询匹配，则Django会投诉。在这种情况下，它将引发MultipleObjectsReturned，它再次是模型类本身的属性。


### Limiting QuerySets
使用Python的数组切片语法的子集将QuerySet限制为一定数量的结果。这相当于SQL的LIMIT和OFFSET子句。 例如，这将返回前5个对象（限制5）：

```python 
>>> Entry.objects.all()[:5]

```

这将返回第六到第十个对象（OFFSET 5 LIMIT 5）：
```python 
>>> Entry.objects.all()[5:10]
```
负数索引（即Entry.objects.all（）[ - 1]）不受支持。

通常，切片QuerySet会返回一个新的QuerySet - 它不评估查询。如果使用Python切片语法的“step”参数，则是一个例外。例如，这实际上会执行查询以返回前10个中每个第二个对象的列表：
```python 
>>> Entry.objects.all()[:10:2]
```
要检索单个对象而不是列表（例如，SELECT foo FROM bar LIMIT 1），请使用简单索引而不是片段。例如，在按标题按字母顺序排序条目后，这将返回数据库中的第一个条目：
```python 
>>> Entry.objects.order_by('headline')[0]
```

```python 
>>> Entry.objects.order_by('headline')[0:1].get()
```
但是，请注意，如果没有对象与给定条件匹配，则第一个将引发IndexError，而第二个将引发DoesNotExist。有关更多详细信息，请参阅get（）。
```python 

```

```python 

```

```python 

```

```python 

```