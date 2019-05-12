## wait 学习笔记
---

### wait 用来异步执行任务
- 目的---是可以让子脚本在父脚本运行时执行其他额外的任务
- 问题---保持父子脚本之间的协调一致是一个问题，比如一个脚本必须等待另一个脚本任务完成之后才能继续进行自己的任务
```sh
#!/bin/bash
# async-parent : Asynchronous execution demo (parent)
echo "Parent: starting..."
echo "Parent: launching child script..."
./async-child.sh & #假设两个文件同一个目录
pid=$!
echo "Parent: child (PID= $pid) launched."
echo "Parent: continuing..."
sleep 2
echo "Parent: pausing to wait for child to finish..."
wait $pid #此时父脚本暂停
echo "Parent: child is finished. Continuing..."
echo "Parent: parent is done. Exiting."

```


```sh
#!/bin/bash
# async-child : Asynchronous execution demo (child)
echo "Child: child is running..."
sleep 5
echo "Child: child is done. Exiting."

```

```sh
$ ./async-parent.sh 
===========================
Parent: starting...
Parent: launching child script...
Parent: child (PID= 29611) launched.
Parent: continuing...
Child: child is running...
Parent: pausing to wait for child to finish...
Child: child is done. Exiting.
Parent: child is finished. Continuing...
Parent: parent is done. Exiting.

```