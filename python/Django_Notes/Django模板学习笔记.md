## Django模板学习笔记
***
### Django模板根据以下两部分理解
1. 语法 Synax 
    1. [变量 Variables](###变量-Variables)
    2. [标签 Tags](###标签-Tags)
    3. [过滤器 Filters](###过滤器-Filters)
    4. [注释 Comments](###注释-Commets)
2. 组件
    1. 引擎
    2. 模板
    3. 上下文
    4. 加载器
***
### 一个简单的Django模板
```python
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}

```
### 变量 Variables
> {{ variable }} 变量两边用两个大括号
***
### 标签 Tags
***

### 过滤器 Filters
***
### 注释 Commets
***






















