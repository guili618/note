## lsof -- list open files 学习笔记
---
### lsof 的作用
- 列出被进程所打开的文件名
- 需要查出某个进程所打开或者使用的文件和设备
***
### lsof 常用参数说明
| 参数           | 说明 |
| ------        | ------ |
| -a         | 多项数据需要 **同时成立** 才显示出结果时|
| -U      | 仅列出 Unix-like 系统的 socket 文件类型 |
| -u | **后面接 username**,列出该用户相关进程所打开的文件 |
| +d        | **后面接目录**,即找出某个目录下面已经被打开的文件 |
***
### 查找某个文件相关的进程

```bash
$ lsof /bin/bash
COMMAND   PID   USER  FD   TYPE DEVICE SIZE/OFF    NODE NAME
bash    11914 oracle txt    REG    8,3   942200 2752551 /bin/bash
bash    13407 oracle txt    REG    8,3   942200 2752551 /bin/bash

```
***
### 列出某个用户打开的文件信息

```bash
$ lsof -u username

-u 选项，u是user的缩写
```
***
### 列出某个程序进程所打开的文件信息

```bash
$ lsof -c redis
COMMAND    PID  USER   FD      TYPE DEVICE SIZE/OFF NODE NAME
redis-ser 2879 redis  cwd   unknown                      /proc/2879/cwd (readlink: Permission denied)
redis-ser 2879 redis  rtd   unknown                      /proc/2879/root (readlink: Permission denied)
redis-ser 2879 redis  txt   unknown                      /proc/2879/exe (readlink: Permission denied)
redis-ser 2879 redis NOFD                                /proc/2879/fd (opendir: Permission denied)
redis-ser 4920 redis  cwd   unknown                      /proc/4920/cwd (readlink: Permission denied)
redis-ser 4920 redis  rtd   unknown                      /proc/4920/root (readlink: Permission denied)

```
***
### 列出某个用户以及某个进程所打开的文件信息
```bash
$lsof  -u redis -c redis
```
***
### 通过某个进程号显示该进程打开的文件

```bash
$lsof -p pid

```
***
### 列出所有的网络连接

```bash
$ lsof -i
```
***
### 列出所有tcp 网络连接信息

```bash
$ lsof -t
```
***
### 列出谁在使用某个端口

```bash
$ lsof -i :1521
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
oracle  13456 oracle   22u  IPv4  54493      0t0  TCP ol6-112.localdomain:48676->ol6-112.localdomain:ncube-lm (ESTABLISHED)
tnslsnr 14270 oracle    8u  IPv6  52902      0t0  TCP *:ncube-lm (LISTEN)
tnslsnr 14270 oracle   12u  IPv6  53542      0t0  TCP ol6-112.localdomain:ncube-lm->ol6-112.localdomain:48676 (ESTABLISHED)
oracle  14274 oracle   12u  IPv6  52915      0t0  TCP ol6-112.localdomain:ncube-lm->192.168.245.1:65246 (ESTABLISHED)
oracle  14278 oracle   12u  IPv6  52935      0t0  TCP ol6-112.localdomain:ncube-lm->192.168.245.1:65248 (ESTABLISHED)
```
***