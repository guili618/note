## Jinja2学习笔记
---
### Jinja2 常见定界符
- {% ... %},用于语句，如if判断，for循环
- {{ ... }},用于表达式，如字符串，变量，函数调用
- {# ... #},用于注释

>另外，Jinja2中支持使用 "." 来获取变量的属性，比如，user字典中的username键值可以通过 "."
>取得,即 user.username,效果上等同于user['username']

### Jinja2内置变量过滤器列表

| 过滤器名称   | 源码函数名 |  说明  |
| ------ | ------ |  ------ | 
|    'abs'        |  abs    |
|    'attr'       |  do_attr    |
|    'batch'      |  do_batch    |
|    'capitalize' |  do_capitalize    |
|    'center'     |  do_center    |
|    'count'      |  len    |
|    'd'          |  do_default    |
|    'default'    |  do_default    |
|    'dictsort'   |  do_dictsort    |
|    'e'          |  escape    |
|    'escape'     |  escape    |
|    'filesizeformat' |  do_filesizeformat   |
|    'first'      |  do_first    |
|    'float'      |  do_float    |
|    'forceescape'： | do_forceescape    |
|    'format'     |  do_format    |
|    'groupby'    |  do_groupby    |
|    'indent'     |  do_indent    |
|    'int'        |  do_int    |
|    'join'       |  do_join    |
|    'last'       |  do_last    |
|    'length'     |  len    |
|    'list'       |  do_list    |
|    'lower'      |  do_lower    |
|    'map'        |  do_map    |
|    'min'        |  do_min    |
|    'max'        |  do_max    |
|    'pprint'     |  do_pprint    |
|    'random'     |  do_random    |
|    'reject'     |  do_reject    |
|    'rejectattr' |  do_rejectattr    |
|    'replace'    |  do_replace    |
|    'reverse'    |  do_reverse    |
|    'round'      |  do_round    |
|    'safe'       |  do_mark_safe    |
|    'select'     |  do_select    |
|    'selectattr' |  do_selectattr    |
|    'slice'      |  do_slice    |
|    'sort'       |  do_sort    |
|    'string'     |  soft_unicode    |
|    'striptags'  |  do_striptags    |
|    'sum'        |  do_sum    |
|    'title'      |  do_title    |
|    'trim'       |  do_trim    |
|    'truncate'   |  do_truncate    |
|    'unique'     |  do_unique    |
|    'upper'      |  do_upper    |
|    'urlencode'  |  do_urlencode    |
|    'urlize'     |  do_urlize    |
|    'wordcount'  |  do_wordcount    |
|    'wordwrap'   |  do_wordwrap    |
|    'xmlattr'    |  do_xmlattr    |
|    'tojson'     |  do_tojson    |


### Jinja2内置测试器列表

| 测试器名   | 源码函数名 |  说明  |
| ------ | ------ |  ------ | 
| 'odd'         |  test_odd |
| 'even'        |  test_even |
| 'divisibleby' |  test_divisibleby |
| 'defined'     |  test_defined |
| 'undefined'   |  test_undefined |
| 'none'        |  test_none |
| 'lower'       |  test_lower |
| 'upper'       |  test_upper |
| 'string'      |  test_string |
| 'mapping'     |  test_mapping |
| 'number'      |  test_number |
| 'sequence'    |  test_sequence |
| 'iterable'    |  test_iterable |
| 'callable'    |  test_callable |
| 'sameas'      |  test_sameas |
| 'escaped'     |  test_escaped |
| 'in'          |  test_in |
| '=='          |  operator.eq |
| 'eq'          |  operator.eq |
| 'equalto'     |  operator.eq |
| '!='          |  operator.ne |
| 'ne'          |  operator.ne |
| '>'           |  operator.gt |
| 'gt'          |  operator.gt |
| 'greaterthan' |  operator.gt |
| 'ge'          |  operator.ge |
| '>='          |  operator.ge |
| '<'           |  operator.lt |
| 'lt'          |  operator.lt |
| 'lessthan'    |  operator.lt |
| '<='          |  operator.le |
| 'le'          |  operator.le |

### Jinja2 for循环特殊变量

| 变量名   |   说明  |
| ------ | ------ |  
| loop.index	| The current iteration of the loop. (1 indexed) |
| loop.index0	| The current iteration of the loop. (0 indexed) |
| loop.revindex	| The number of iterations from the end of the loop (1 indexed) |
| loop.revindex0	| The number of iterations from the end of the loop (0 indexed) |
| loop.first	| True if first iteration. |
| loop.last	    | True if last iteration. |
| loop.length	| The number of items in the sequence. |
| loop.cycle	 | A helper function to cycle between a list of sequences. See the explanation below. |
| loop.depth	| Indicates how deep in a recursive loop the rendering currently is. Starts at level 1 |
| loop.depth0	| Indicates how deep in a recursive loop the rendering currently is. Starts at level 0 |
| loop.previtem	| The item from the previous iteration of the loop. Undefined during the first iteration. |
| loop.nextitem	| The item from the following iteration of the loop. Undefined during the last iteration. |
| loop.changed(*val) |	True if previously called with a different value (or not called at all). |
