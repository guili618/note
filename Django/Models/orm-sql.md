## Django ORM 和 SQL 对比
---

### 表的创建
- sql
```sql
CREATE TABLE Person (
    id int,
    name varchar(50),
    age int NOT NULL,
    gender varchar(10),
);
```
- orm,django默认自动添加id为主键
```python
class Person(models.Model):
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=True)

```

| sql | django |
| ------ | ------ |
|INT	 | IntegerField()|
|VARCHAR(n) |	CharField(max_length=n)|
|TEXT	 | TextField()|
|FLOAT(n) |	FloatField()|
|DATE	  | DateField()|
|TIME	  | TimeField()|
|DATETIME | DateTimeField()|



###  select语句
- sql
```sql
SELECT * FROM Person;
```
- django
```python
persons = Person.objects.all()
for person in persons:
    print(person.name)
    print(person.gender)
    print(person.age)
```
####  选取特定的字段
- sql
```sql
SELECT name, age FROM Person;
```
- django
```python
Person.objects.only('name', 'age')
```
#### distinct
```sql
SELECT DISTINCT name, age FROM Person;
```
- django
```python
Person.objects.values('name', 'age').distinct()
```

####  查询结果限定行数
- sql
```sql
SELECT * FROM Person LIMIT 10;
```
- django
```python
Person.objects.all()[:10]
```

- sql
```sql
SELECT * FROM Person OFFSET 5 LIMIT 5;
```
- django
```python
Person.objects.all()[5:10]
```
---
###  where 语句
- sql
```sql
SELECT *FROM Person WHERE id = 1;
```
- django
```python
Person.objects.filter(id=1)
```

####  比较
- sql
```sql
SELECT * FROM Person WHERE age > 18;
SELECT * FROM Person WHERE age >= 18;
SELECT * FROM Person WHERE age < 18;
SELECT * FROM Person WHERE age <= 18;
SELECT * FROM Person WHERE age != 18;
```
- django
```python
Person.objects.filter(age__gt=18)
Person.objects.filter(age__gte=18)
Person.objects.filter(age__lt=18)
Person.objects.filter(age__lte=18)
Person.objects.exclude(age=18)

```
---
###  between语句
- sql
```sql
SELECT *
FROM Person 
WHERE age BETWEEN 10 AND 20;
```
- django
```python
Person.objects.filter(age__range=(10, 20))
```
---
###  LIKE 语句
- sql
```sql
SELECT * FROM Person WHERE name like '%A%';
SELECT * FROM Person WHERE name like binary '%A%';
SELECT * FROM Person WHERE name like 'A%';
SELECT * FROM Person WHERE name like binary 'A%';
SELECT * FROM Person WHERE name like '%A';
SELECT * FROM Person WHERE name like binary '%A';
```
- django
```python
Person.objects.filter(name__icontains='A')
Person.objects.filter(name__contains='A')
Person.objects.filter(name__istartswith='A')
Person.objects.filter(name__startswith='A')
Person.objects.filter(name__iendswith='A')
Person.objects.filter(name__endswith='A')

```
---
###  IN 语句
- sql
```sql
SELECT * FROM Person WHERE id in (1, 2);
```
- django
```python
Person.objects.filter(id__in=[1, 2])
```
---
###   AND, OR and NOT 语句
- and sql
```sql
SELECT * FROM Person WHERE gender='male' AND age > 25;
```
- django
```python
Person.objects.filter(gender='male', age__gt=25)
```

- or sql
```sql
SELECT * FROM Person WHERE gender='male' OR age > 25;
```
- django
```python
from django.db.models import Q
Person.objects.filter(Q(gender='male') | Q(age__gt=25))
```

- not sql
```sql
SELECT * FROM Person WHERE NOT gender='male';
```
- django
```python
Person.objects.exclude(gender='male')
```
---
###   NULL 语句
- sql
```sql
SELECT * FROM Person  WHERE age is NULL;
SELECT * FROM Person  WHERE age is NOT NULL;
```
- django
```python
Person.objects.filter(age__isnull=True)
Person.objects.filter(age__isnull=False)

# 另一种用法
Person.objects.filter(age=None)
Person.objects.exclude(age=None)
```
---
###   ORDER BY 语句
- sql
```sql
SELECT * FROM Person order by age;
```
- django
```python
Person.objects.order_by('age')
```

####    Descending Order 语句
- sql
```sql
SELECT * FROM Person ORDER BY age DESC;
```
- django
```python
Person.objects.order_by('-age')
```
---
###   INSERT INTO 语句
- sql
```sql
INSERT INTO Person
VALUES ('Jack', '23', 'male');
```
- django
```python
Person.objects.create(name='jack', age=23, gender='male)
```
---
###   UPDATE  语句
- 单行 update sql
```sql
UPDATE Person SET age = 20 WHERE id = 1;
```
- django
```python
person = Person.objects.get(id=1)
person.age = 20
person.save()
```

####   多行 update语句
- sql
```sql
UPDATE PersonSET age = age * 1.5;
```
- django
```python
from django.db.models import F

Person.objects.update(age=F('age')*1.5)
```
---
###   delete 语句
- sql
```sql
DELETE FROM Person;
```
- django
```python
Person.objects.all().delete()
```

####  Delete 特定行 
- sql
```sql
DELETE FROM Person WHERE age < 10;
```
- django
```python
Person.objects.filter(age__lt=10).delete()
```
---
###   聚合函数语句
- min sql
```sql
SELECT MIN(age) FROM Person;
```
- django
```python
from django.db.models import Min
Person.objects.all().aggregate(Min('age'))

```
- max sql
```sql
SELECT MAX(age) FROM Person;
```
- django
```python
from django.db.models import Max
Person.objects.all().aggregate(Max('age'))

```
- avg sql
```sql
SELECT AVG(age) FROM Person;
```
- django
```python
>>> from django.db.models import Avg
>>> Person.objects.all().aggregate(Avg('age'))
{'age__avg': 50}
```
- sum sql
```sql
SELECT SUM(age) FROM Person;
```
- django
```python
>>> from django.db.models import Sum
>>> Person.objects.all().aggregate(Sum('age'))
{'age__sum': 5050}
```

- COUNT sql
```sql
SELECT COUNT(*) FROM Person;
```
- django
```python
Person.objects.count()
```
---
### GROUP BY   语句
- sql
```sql
SELECT gender, COUNT(*) as count FROM Person GROUP BY gender;
```
- django
```python
Person.objects.values('gender').annotate(count=Count('gender'))
```
---
###   HAVING 语句
- sql
```sql
SELECT gender, COUNT('gender') as count
FROM Person
GROUP BY gender
HAVING count > 1;
```
- django
```python
Person.objects.annotate(count=Count('gender'))
.values('gender', 'count')
.filter(count__gt=1)
```
---
###    JOINS语句
- table definition
```python
class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
```
- sql
```sql
SELECT name
FROM Book
LEFT JOIN Publisher
ON Book.publisher_id = Publisher.id
WHERE Book.id=1;
```
- django
```python
book = Book.objects.select_related('publisher').get(id=1)
book.publisher.name
```
---
###    语句
- sql
```sql
SELECT *
FROM Book
WHERE Book.publisher_id = 1;
```
- django
```python
publisher = Publisher.objects.prefetch_related('book_set').get(id=1)
books = publisher.book_set.all()
```
---
###    语句
- sql
```sql

```
- django
```python

```
---
###    语句
- sql
```sql

```
- django
```python

```
---
###    语句
- sql
```sql

```
- django
```python

```
---
###    语句
- sql
```sql

```
- django
```python

```
---
###    语句
- sql
```sql

```
- django
```python

```
---
###    语句
- sql
```sql

```
- django
```python

```
---
###    语句
- sql
```sql

```
- django
```python

```
---




