from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n','<br>\n')
    return '<p>{0}</p>'.format(content)
@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0}</pre>'.format(n)


@htmlize.register(tuple)  # <5>
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize({1, 2, 3}))  
print(htmlize(abs))
print(htmlize(42))
print(htmlize(['alpha', 66, {3, 2, 1}]))
