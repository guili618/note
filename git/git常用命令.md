## Git 常用命令笔记
---
### 
- 创建仓库
```sh
$ git init .
Initialised empty Git repository in /.../superlists/.git/
```
- 忽略文件
```sh
$ echo "db.sqlite3" >> .gitignore
$ echo "__pycache__" >> .gitignore
$ echo "*.pyc" >> .gitignore
```
- 添加内容
```sh
$ git add .
```
- 删除内容
```sh
$ git rm -r --cached superlists/__pycache__

```
- 查看状态
```sh
$ git status 
On branch master
Initial commit
Changes to be committed:
(use "git rm --cached <file>..." to unstage)
new file: .gitignore
new file: functional_tests.py
new file: manage.py
new file: superlists/__init__.py
new file: superlists/__pycache__/__init__.cpython-36.pyc
new file: superlists/__pycache__/settings.cpython-36.pyc
new file: superlists/__pycache__/urls.cpython-36.pyc
new file: superlists/__pycache__/wsgi.cpython-36.pyc
new file: superlists/settings.py
new file: superlists/urls.py
new file: superlists/wsgi.py
```
- 查看差异内容

```sh
$ git diff
diff --git a/functional_tests.py b/functional_tests.py
index d333591..b0f22dc 100644
--- a/functional_tests.py
+++ b/functional_tests.py
@@ -1,6 +1,45 @@
from selenium import webdriver
+import unittest
-browser = webdriver.Firefox()
-browser.get('http://localhost:8000')
+class NewVisitorTest(unittest.TestCase):
-assert 'Django' in browser.title
+ def setUp(self):
+ self.browser = webdriver.Firefox()
+
+ def tearDown(self):
+ self.browser.quit()
[...]

```
- 提交,-a表示自动添加已追踪文件（即已经提交的各文件）中的改动
```sh
$ git commit -a

```
> git -am表示添加所有已跟踪文件中的改动，并且使用命令行输入消息，该方式最快捷，但是提交内容的反馈最少，所以在之前最好执行git status 和 git diff，弄清楚要把哪些改动放入仓库
```sh
$ git commit -am "Basic view now returns minimal HTML"
```
