### subprocess 模块学习笔记

### subprocess 模块简介
> subprocess 模块最早在 Python 2.4版本中引入，用于创建和管理子进程。它提供高层次的接口，用来替换 os.system(),os.spawn\*(),os.popen\*(),popen2.\*() 和commands.\* 等模块与函数

>subprocess 提供了一个名为 Popen 的类来启动和设置子进程的参数，由于这个类比较复杂，subprocess 还提供了若干便利函数，这些便利函数都是对这个 Popen 类的分组，以便快速启动一个子进程并获取它们的输出结果

### Popen(args,**parms)
> 以子进程的形式执行一个新命令，然后返回代表新进程的 Popen 对象。命令在 args 中以字符串的形式指定，如 'ls -l'，或者字符串列表['ls','-l']. parms 表示关键字参数的集合，设置这些关键字以控制子进程的各种属性

```python
from subprocess import Popen, PIPE
 
#function that takes the sqlCommand and connectString and returns the queryReslut and errorMessage (if any)
def runSqlQuery(sqlCommand, connectString):
   session = Popen(['sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
   session.stdin.write(sqlCommand)
   print(session.communicate())


connectString = 'username/password'
sql = 'select sysdate from dual;'
sqlCommand = sql.encoding(encoding='utf-8')
queryResult, errorMessage = runSqlQuery(sqlCommand, connectString)

```

### subprocess 中 shell=True 导致的shell注入问题
- https://security.openstack.org/guidelines/dg_avoid-shell-true.html
- https://security.openstack.org/guidelines/dg_use-subprocess-securely.html
避免shell注入
```python

def count_lines(website):
    args = ['curl', website]
    args2 = ['wc', '-l']
    process_curl = subprocess.Popen(args, stdout=subprocess.PIPE,shell=False)
    process_wc = subprocess.Popen(args2, stdin=process_curl.stdout,stdout=subprocess.PIPE, shell=False)
    # Allow process_curl to receive a SIGPIPE if process_wc exits.
    process_curl.stdout.close()
    return process_wc.communicate()[0]

```