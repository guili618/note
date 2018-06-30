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

每个元组中的第一个元素是将存储在数据库中的值。第二个元素将通过默认表单小部件或ModelChoiceField显示。给定一个模型实例，可以使用get_FOO_display（）方法访问选择字段的显示值。例如
```python
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
------------------------------------------------------------------------------
>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'

```
---
#### default
字段的默认值。这可以是一个值或一个可调用的对象。如果可调用，则每次创建新对象时都会调用它。

#### help_text
用窗体小部件显示额外的“帮助”文本。即使你的字段未用于表单，对于文档也很有用

#### primary_key
 如果为True，则此字段是模型的主键

 如果您没有为模型中的任何字段指定primary_key = True，那么Django会自动添加一个IntegerField来保存主键，因此您不需要在任何字段上设置primary_key = True，除非您想覆盖默认的主键行为。有关更多信息，请参阅 Automatic primary key fields

 主键字段是只读的。如果您更改现有对象上主键的值并保存它，则会在旧对象旁边创建一个新对象。例如：
 
```python
from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
---------------------------------------------------------------
>>> fruit = Fruit.objects.create(name='Apple')
>>> fruit.name = 'Pear'
>>> fruit.save()
>>> Fruit.objects.values_list('name', flat=True)
<QuerySet ['Apple', 'Pear']>
```
####  unique
如果为True，则该字段在整个表格中必须是唯一的。

再啰嗦一句，这些只是对最常见字段选项的简短描述。完整的细节可以在 common model field option reference中找到。

### Automatic primary key fields
默认情况下，Django为每个模型提供以下字段：
```pyhton
id = models.AutoField(primary_key=True)
```
这是一个自动递增的主键。 

如果您想要指定自定义主键，只需在其中一个字段上指定primary_key = True。如果Django发现你已经明确设置了Field.primary_key，它将不会添加自动ID列。 

每个模型只需要一个字段就具有primary_key = True（显式声明或自动添加）。

---
### Verbose field names
除ForeignKey，ManyToManyField和OneToOneField外，每个字段类型都采用可选的第一个位置参数 - 一个详细名称。如果没有给出详细名称，Django将使用该字段的属性名称自动创建它，并将下划线转换为空格

在下面这个例子中，verbose name是"person's first name":

```python
first_name = models.CharField("person's first name", max_length=30)
```

在下面这个例子中，verbose name是"first name":

```python
first_name = models.CharField(max_length=30)

```
ForeignKey，ManyToManyField和OneToOneField要求第一个参数是关联的模型类，所以请使用verbose_name关键字参数：
```python
poll = models.ForeignKey(
    Poll,
    on_delete=models.CASCADE,
    verbose_name="the related poll",
)
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    verbose_name="related place",
)
```
约定不是要大写verbose_name的第一个字母。 Django会自动把它需要的第一个字母大写

---
### Relationships

显然，关系数据库的强大之处在于相互关联表。 Django提供了定义三种最常见类型的数据库关系的方法：多对一，多对多和一对一。


#### Many-to-one relationships

要定义多对一关系，请使用django.db.models.ForeignKey。您可以像使用其他字段类型一样使用它：将它作为模型的类属性包含在其中。 

ForeignKey需要一个位置参数：与模型相关的类。

 例如，如果汽车模型有制造商 - 即制造商制造多辆汽车，但每辆汽车只有一家制造商 - 则使用以下定义：

 ```python

from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...

 ```

您还可以创建recursive relationships（与自身具有多对一关系的对象）以及与尚未定义的模型的关系;详细信息请参阅the model field reference


有人建议，但不是必需的，ForeignKey字段的名称（上例中的制造商）是小写字母的名称。当然，无论你想要什么，你都可以调用该字段。例如：

```python

class Car(models.Model):

    company_that_makes_it = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    # ...
```
另外

- ForeignKey字段接受在 the model field reference中解释的多个额外参数。这些选项有助于确定关系应该如何工作;全部都是可选的。
- 有关访问向后相关对象的详细信息，请参阅Following relationships backward example.
- 有关示例代码,参阅Many-to-one relationship model example.

---
### Many-to-many relationships

要定义多对多关系，请使用ManyToManyField。您可以像使用其他字段类型一样使用它：将它作为模型的类属性包含在其中

ManyToManyField需要一个位置参数：与模型相关联的类

例如，如果匹萨饼有多个配料对象 - 也就是说，配料可以在多个比萨饼上，每个比萨饼都有多个配料 
示例如下：

```python

from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)

```

和ForeignKey一样，您也可以创建 recursive relationships（与自身具有多对多关系的对象）以及relationships to models not yet defined.

有人建议，但不是必须的，ManyToManyField的名字（上面例子中的toppings）是描述相关模型对象集合的复数形式。

通常，ManyToManyField实例应该放入要在表单上编辑的对象中。在上面的例子中，配料是在匹萨（而不是Topping有一个匹萨饼ManyToManyField），因为比起在多个匹萨饼上配料，想想匹萨饼更自然。按照上面的设置，匹萨饼形式可以让用户选择配料。

此外，更多的例子参照  Many-to-many relationship model example

ManyToManyField字段还接受许多额外的参数，这些参数在the model field reference中进行了解释。这些选项有助于确定关系应该如何工作;全部都是可选的。


#### Extra fields on many-to-many relationships

当你只处理简单的多对多关系时，比如混合和匹配比萨饼和配料，一个标准的ManyToManyField就是你所需要的。但是，有时您可能需要将数据与两个模型之间的关系相关联。


例如，考虑追踪音乐家所属乐队的应用程序的情况。在一个人和他们所属的乐队之间存在多对多的关系，因此您可以使用ManyToManyField来表示这种关系。但是，关于您可能想要收集的成员资格有很多详细信息，例如加入该组的人的日期。

对于这些情况，Django允许您指定将用于管理多对多关系的模型。然后您可以在中间模型上添加额外的字段。中间模型使用through参数与ManyToManyField关联，以指向充当中间的模型。对于我们音乐家的例子，代码看起来像这样：

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

```

在设置中间模型时，显式指定涉及多对多关系的模型的外键。这个明确的声明定义了两个模型是如何相关的

中间模型有几个限制：
- 您的中间模型必须包含一个 - 且只有一个 - 源模型的外键（在我们的示例中，这将是Group），或者您必须显式指定Django应该用于关系的外键使用ManyToManyField.through_fields。如果您有多个外键，并且未指定through_fields，则会引发验证错误。类似的限制适用于目标模型的外键（在我们的示例中，这将是Person）。
- 对于通过中间模型与自身有多对多关系的模型，允许使用同一模型的两个外键，但它们将被视为多对多关系的两个（不同）方面。如果有两个以上的外键，那么你还必须像上面那样指定through_fields，否则会出现验证错误。
- 在定义从模型到其自身的多对多关系时，使用中间模型，必须使用symmetrical = False,参考 the model field reference

现在您已经将您的ManyToManyField设置为使用您的中介模型（在这种情况下为Membership），您已准备好开始创建一些多对多关系。您可以通过创建中间模型的实例来完成此操作：

```python

>>> ringo = Person.objects.create(name="Ringo Starr")
>>> paul = Person.objects.create(name="Paul McCartney")
>>> beatles = Group.objects.create(name="The Beatles")
>>> m1 = Membership(person=ringo, group=beatles,
...     date_joined=date(1962, 8, 16),
...     invite_reason="Needed a new drummer.")
>>> m1.save()
>>> beatles.members.all()
<QuerySet [<Person: Ringo Starr>]>
>>> ringo.group_set.all()
<QuerySet [<Group: The Beatles>]>
>>> m2 = Membership.objects.create(person=paul, group=beatles,
...     date_joined=date(1960, 8, 1),
...     invite_reason="Wanted to form a band.")
>>> beatles.members.all()
<QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>]>


与普通的多对多字段不同，您不能使用add（），create（）或set（）来创建关系：

>>> 下面这些是不行滴~~~
>>> beatles.members.add(john)
>>> beatles.members.create(name="George Harrison")
>>> beatles.members.set([john, paul, ringo, george])
```

为什么？您不能仅在Person和Group之间创建关系 - 您需要指定Membership模型所需关系的所有详细信息。简单的添加，创建和赋值调用不提供指定这些额外细节的方法。因此，它们在使用中间模型的多对多关系中被禁用。创建这种类型的关系的唯一方法是创建中间模型的实例。

由于类似的原因，remove（）方法被禁用。例如，如果由中间模型定义的自定义直通表没有在（模型1，模型2）对上强制实施唯一性，则remove（）调用将不会提供足够的信息来确定应删除哪个中间模型实例：

```python
>>> Membership.objects.create(person=ringo, group=beatles,
...     date_joined=date(1968, 9, 4),
...     invite_reason="You've been gone for a month and we miss you.")
>>> beatles.members.all()
<QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>, <Person: Ringo Starr>]>
>>> # This will not work because it cannot tell which membership to remove
>>> beatles.members.remove(ringo)

```

但是，clear（）方法可用于删除实例的所有多对多关系：

```python

>>> # Beatles have broken up
>>> beatles.members.clear()
>>> # Note that this deletes the intermediate model instances
>>> Membership.objects.all()
<QuerySet []>
```

一旦通过创建中间模型的实例建立了多对多关系，就可以发出查询。与正常的多对多关系一样，您可以使用多对多关联模型的属性进行查询

```python
# Find all the groups with a member whose name starts with 'Paul'
>>> Group.objects.filter(members__name__startswith='Paul')
<QuerySet [<Group: The Beatles>]>

```
在您使用中间模型时，您还可以查询其属性：

```python
# Find all the members of the Beatles that joined after 1 Jan 1961
>>> Person.objects.filter(
...     group__name='The Beatles',
...     membership__date_joined__gt=date(1961,1,1))
<QuerySet [<Person: Ringo Starr]>

```


如果您需要访问membership信息，您可以直接查询membership模型：
```python
>>> ringos_membership = Membership.objects.get(group=beatles, person=ringo)
>>> ringos_membership.date_joined
datetime.date(1962, 8, 16)
>>> ringos_membership.invite_reason
'Needed a new drummer.'

```

访问相同信息的另一种方法是通过查询Person对象中的多对多反向关系：
```python

>>> ringos_membership = ringo.membership_set.get(group=beatles)
>>> ringos_membership.date_joined
datetime.date(1962, 8, 16)
>>> ringos_membership.invite_reason
'Needed a new drummer.'
```

### 一对一的关系

