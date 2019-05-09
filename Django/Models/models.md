## models基本
---
###
- 在数据模型中的Meta类表示存放模型的元数据。通过定义ordering = ('-publish',)，指定了Django在进行数据库查询的时候，默认按照发布时间的逆序将查询结果排序。逆序通过加在字段名前的减号表示。这样最近发布的文章就会排在前边。
- author：是一个外键字段。通过这个外键，告诉Django一篇文章只有一个作者，一个作者可以写多篇文章。对于这个字段，Django会在数据库中使用外键关联到相关数据表的主键上。在这个例子中，这个外键关联到Django内置用户验证模块的User数据模型上。on_delete参数表示删除外键关联的内容时候的操作，这个并不是Django特有的定义，而是SQL 数据库的标准操作；将其设置为CASCADE意味着如果删除一个作者，将自动删除所有与这个作者关联的文章，related_name参数设置了从User到Post的反向关联关系，用blog_posts为这个反向关联关系命名，稍后会学习到该关系的使用。
```python
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published')
        )

    title = models.CharField(max_length=250) #对应数据库 VARCHAR(250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True) #表示创建该文章的时间。auto_now_add表示当创建一行数据的时候，自动用创建数据的时间填充。
    updated = models.DateTimeField(auto_now=True) #表示文章最后一次修改的时间，auto_now表示每次更新数据的时候，都会用当前的时间填充该字段
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title
```
