## wait 学习笔记
---

### 
```sh
#!/bin/bash
# async-parent : Asynchronous execution demo (parent)
echo "Parent: starting..."
Exotica 429echo "Parent: launching child script..."
async-child &
pid=$!
echo "Parent: child (PID= $pid) launched."
echo "Parent: continuing..."
sleep 2
echo "Parent: pausing to wait for child to finish..."
wait $pid
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