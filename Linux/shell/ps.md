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
|  -C  cmslist | Shows processes contained in the list cmdlist  |
|  -G  grplist | Shows processes with a group ID listed in grplist  |
|  -U  userlist|  Shows processes owned by a userid listed in userlist  |
|  -g  grplist | Shows processes by session or by groupid contained in grplist  |
|  -p  pidlist | Shows processes with PIDs in the list pidlist  |
|  -s  sesslist|  Shows processes with session ID in the list sesslist  |
|  -t  ttylist | Shows processes with terminal ID in the list ttylist  |
|  -u  userlist|  Shows processes by effective userid in the list userlist  |
|  -F    | Uses extra full output|
|  -O    | format Displays speciic columns in the list format, along with the defaultcolumns|
|  -M    | Displays security information about the process|
|  -c    | Shows additional scheduler information about the process|
|  -f    | Displays a full format listing|
|  -j    | Shows job information|
|  -l    | Displays a long listing|
|  -o    | format Displays only speciic columns listed in format|
|  -y    | Prevents display of process lags|
|  -Z    | Displays the security context information|
|  -H    | Displays processes in a hierarchical format (showing parent processes)|
|  -n    | namelist Deines the values to display in the WCHAN column|
|  -w    | Uses wide output format, for unlimited width displays|
|  -L    | Shows process threads|
|  -V    | Displays the version of ps|

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
