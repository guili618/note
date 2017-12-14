### python-docx 模块学习笔记

### 

```python
>>> import docx
>>> doc = docx.Document(r'D:\\example.docx')
>>> len(doc.paragraphs)
1
>>> doc.paragraphs[0].text
'This is a test word file'


```