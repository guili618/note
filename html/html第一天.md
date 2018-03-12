## HTML 笔记 day1
---
### 什么是 HTML
- HTML 是 HyperText Markup Language 超文本标记语言的缩写
- HTML 是创建网页的标准标记语言
- HTML 用标记描述了网页的基础结构
 
### HTML 一个最基本的结构
```HTML
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

```
- <!DOCTYPE html> 声明定义了该文档是HTML5
- <html> 元素是 HTML 页面的根元素
- <head> 元素包含这个文档的元信息 
- <title> 元素 为文档指定一个标题
- <body> 元素 包含了该文档的可见内容 
- <h1> 元素 定义一个大的标题
- <p> 元素 定义一个段落
---
### HTML 的标签由简括包裹住元素名称
```html
<tagname>内容</tagname>
```

- HTML 的标签一般总是成对出现，比如说  <p> and </p>
- 第一个标签表示开始，第二个标签表示结束
The end tag is written like the start tag, but with a forward slash inserted before the tag name