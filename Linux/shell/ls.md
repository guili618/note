## ls 命令学习笔记
---
### 示例1--列出当前路径下的目录

```sh
$ ls -d */
```
```sh
$ ls -F | grep "/$"
```
```sh
$ ls -l | grep "^d"
```
```sh
$ find . -type d -maxdepth 1 -print
```