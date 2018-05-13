## xargs 笔记
***

### 

```bash

ps aux | grep PROCESS | grep -v grep | awk '{print $2}' | xargs kill -9

```

### 

```bash
$ echo 'hello hello hello hello hello hello' | xargs -n 2
hello hello
hello hello
hello hello

```