## ps命令学习笔记
---
### ps 命令用来监测系统上面的进程 Linux系统中的GNS ps命令支持3种不同类型的命令行参数
- Unix风格参数，前面加单破折号
- BSD风格参数，前面不加破折号
- GNU风格的长参数，前面加双破折号

### Unix 风格的ps命令参数

| 参数    | 描述 |
| ------ | ------ |
|  -A    | 显示所有进程|
|  -N    | 显示与指定参数不符的进程|
|  -a    | 显示除了控制进程和无终端进程外的所有进程|
|  -d    | 显示除了控制进程外的所有进程|
|  -e    | 显示所有进程|
|  -C  cmslist | 显示  包含在  cmdlist 列表中的进程  |
|  -G  grplist | 显示  组 ID 在 grplist 列表中的进程  |
|  -U  userlist| 显示  属主的用户 ID 在 userlist 列表中的进程  |
|  -g  grplist | 显示  会话或组 ID 在 grplist 列表中的进程  |
|  -p  pidlist | 显示  PID 在 pidlist 列表中的进程  |
|  -s  sesslist| 显示  会话 ID 在 sesslist 列表中的进程  |
|  -t  ttylist | 显示  终端 ID 在 ttylist 列表中的进程  |
|  -u  userlist| 显示  有效用户 ID 在 userlist 列表中的进程  |
|  -F    | 显示更多的额外输出(相对于 -f 参数)|
|  -O  format | 显示默认的输出列以及由 format 列表指定的特定列|
|  -M    | 显示进程的安全信息|
|  -c    | 显示进程的额外调度器信息|
|  -f    | 显示完整的格式输出|
|  -j    | 显示任务信息|
|  -l    | 显示长列表 |
|  -o    | 仅显示format指定的列 |
|  -y    | 不要显示进程标签|
|  -Z    | 显示安全标签信息|
|  -H    | 用层级格式来显示进程(树型，用来显示父进程)|
|  -n    | 定义了 WCHAN 列显示的值|
|  -w    | 采用宽输出模式，不限宽度显示|
|  -L    | 显示进程中的线程|
|  -V    | 显示 PS 命令的版本号|

### ps -ef 输出字段说明
```sh
ps -ef
UID         PID   PPID  C STIME TTY          TIME CMD
root          1      0  0 14:49 ?        00:00:02 /sbin/init
root          2      0  0 14:49 ?        00:00:00 [kthreadd]
root          3      2  0 14:49 ?        00:00:00 [ksoftirqd/0]
root          5      2  0 14:49 ?        00:00:00 [kworker/0:0H]
```
| 输出           | 描述 |
| ------        | ------ |
| UID        |启动进程的用户 |
| PID      | 进程的id |
| PPID | 父进程的进程号 |
| C	        | 进程周期中的CPU利用率 |
| STIME	        | 进程启动时候的系统时间 |
| TTY 	        | 进程启动时的终端设备 |
| TIME        | 运行进程需要的CPU累积时间 |
| CMD      | 启动的程序名称 |
