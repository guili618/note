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

```bash
find . -name '*.py' -print0 | xargs -0 grep 'something' > output.txt


find . -name '*.py' -exec grep 'something' {} \; > output.txt
```