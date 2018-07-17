## Django 中的view
---

### Writing views
视图函数或视图简而言之就是一个Python函数，它接受一个Web请求并返回一个Web响应。此响应可以是网页的HTML内容，重定向或404错误，XML文档或图像。 。 。或者其他什么，真的。视图本身包含返回该响应所需的任意逻辑。这段代码可以在任何你想要的地方生存，只要它在你的Python路径上。没有其他要求 - 没有“魔术”，可以这么说。为了将代码放在某个地方，惯例是将视图放在一个名为views.py的文件中，放置在您的项目或应用程序目录中

下面这是一个返回当前日期和时间的视图，作为HTML文档：
```python 
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```
让我们一次一行地执行此代码
- 首先，我们从django.http模块导入HttpResponse类以及P​​ython的日期时间库。
- 接下来，我们定义一个名为current_datetime的函数。这是视图函数。每个视图函数都将HttpRequest对象作为其第一个参数，通常将其命名为request。
- 请注意，视图函数的名称无关紧要;它不必以某种方式命名，以便Django能够识别它。我们在这里将它称为current_datetime，因为该名称清楚地表明它的功能。
- 该视图返回一个包含生成响应的HttpResponse对象。每个视图函数负责返回一个HttpResponse对象。 （也有例外，但我们稍后会介绍。）

### Returning errors

在Django中返回HTTP错误代码很容易。 HttpResponse的子类可以用于许多不同于200的常见HTTP状态码（这意味着“OK”）。您可以在请求/响应文档中找到可用子类的完整列表。只需返回其中一个子类的实例，而不是正常的HttpResponse以表示错误。例如：

```python 
from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')
```
每个可能的HTTP响应代码都没有专门的子类，因为它们中的许多都不会那么常见。但是，如HttpResponse文档中所述，您还可以将HTTP状态代码传递给HttpResponse的构造函数，以便为您喜欢的任何状态代码创建返回类。例如：
```python 
from django.http import HttpResponse

def my_view(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)
```
### The Http404 exception

当您返回错误（例如HttpResponseNotFound）时，您负责定义生成的错误页面的HTML：
```python 
return HttpResponseNotFound('<h1>Page not found</h1>')

```
为了方便起见，并且由于在您的站点中存在一致的404错误页面是一个好主意，Django提供了一个Http404异常。如果你在视图函数中的任何一点都提出Http404，Django会捕获它并返回你的应用程序的标准错误页面以及HTTP错误代码404。
```python 
from django.http import Http404
from django.shortcuts import render
from polls.models import Poll

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'poll': p})
```

为了在Django返回404时显示自定义HTML，您可以创建一个名为404.html的HTML模板，并将其放置在模板树的顶层。此模板将在DEBUG设置为False时提供

当DEBUG为True时，您可以提供一条消息给Http404，它将出现在标准的404调试模板中。将这些消息用于调试目的;它们通常不适合用于生产404模板。

### Customizing error views

Django中的默认错误视图应该足以满足大多数Web应用程序的需求，但是如果您需要任何自定义行为，则可以轻松覆盖它们。只需在URLconf中指定如下所示的处理程序（在其他地方将其设置为无效）

```python 
The page_not_found() view is overridden by handler404:

handler404 = 'mysite.views.my_custom_page_not_found_view'
The server_error() view is overridden by handler500:

handler500 = 'mysite.views.my_custom_error_view'
The permission_denied() view is overridden by handler403:

handler403 = 'mysite.views.my_custom_permission_denied_view'
The bad_request() view is overridden by handler400:

handler400 = 'mysite.views.my_custom_bad_request_view'
```
### Django shortcut functions
包django.shortcuts收集帮助函数和“跨越”多级MVC的类。换句话说，为方便起见，这些函数/类引入了受控耦合。

#### render()

> render(request, template_name, context=None, content_type=None, status=None, using=None)

将给定的模板与给定的上下文字典组合起来，并返回带有该呈现文本的HttpResponse对象。 Django不提供返回TemplateResponse的快捷方式函数，因为TemplateResponse的构造函数提供了与render（）相同的便利级别。

```python 
from django.shortcuts import render

def my_view(request):
    # View code here...
    return render(request, 'myapp/index.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml') 
```

```python 
from django.http import HttpResponse
from django.template import loader

def my_view(request):
    # View code here...
    t = loader.get_template('myapp/index.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')
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