## shell中的时间 
---
### 日期格式参考表
|日期内容 | 格式 |
|---     |---  |
|Weekday 星期 |%a (例如： Sat)|
|        |%A (例如： Saturday)|
|Month 月  |%b (例如： Nov)|
|        |%B (例如： November)|
|Day  日    |%d (例如： 31)|
|固定格式日期 (mm/dd/yy) |%D (例如： 10/18/10)|
|Year  年  |%y (例如： 10)|
|        |%Y (例如： 2010)|
|Hour 小时  | %I or %H (例如： 08)|
|Minute 分钟 |%M (例如： 33)|
|Second  秒 |%S (例如： 10)|
|Nano second 纳秒|%N (例如： 695208515)|
|Epoch Unix time in seconds -Uinx 纪元时|%s (例如： 1290049486)|
---
### 检测脚本运行时间
```sh

#!/bin/bash
START_TIME=$(date +%s)
IP_POOL=$(echo 192.168.245.{1..255})
for ip in $IP_POOL;
do 
	(
		ping $ip -c 2 &> /dev/null;
		if [ $? -eq 0 ];
		then 
			echo ip $ip 已经被使用
		fi
	)&
done
wait
END_TIME=$(date +%s)
COST_TIME=$(( END_TIME - START_TIME ))
echo "这个脚本花费了$COST_TIME秒"

```
---
### 程序延时
```sh
$ sleep 6 #延时6秒
```
---

### 计算命令执行时间
|Parameter| Description|
|---|----|
| %C | 进行计时的命令名称以及命令行参数.|
| %D | 进程非共享数据区域的大小，以KB为单位|
| %E | 进程使用的real时间，显示各位为 [hours:]minutes:seconds.|
| %x | 命令的退出状态.|
| %k | 进程接收到的信号数量.|
| %W | 进程被交换出主存的次数.|
| %Z | System's page size in bytes. This is a per-system constant, but varies between systems.|
| %P | Percentage of the CPU that this job got. This is just user + system times divided by the total running time. It also prints a percentage sign.|
| %K | Average total (data + stack + text) memory usage of the 进程, in Kilobytes.|
| %w |程序主动进行上下文切换的次数, 例如等待IO操作完成.|
| %c |程序被迫进行上下文切换的次数 (由于时间片到期).|
- 用build-in的time(默认)
- 用/usr/bin/time(功能更多，需要显式的指定路径，有的发行版需要安装，再用which time查看路径)

```sh
$ time ./fast_ping.sh 
ip 192.168.245.2 已经被使用
ip 192.168.245.1 已经被使用
ip 192.168.245.131 已经被使用
ip 192.168.245.132 已经被使用
这个脚本花费了 12 秒

real	0m11.544s
user	0m0.008s
sys	0m0.060s
```
- Real时间指的是挂钟时间，就是命令从开始执行到结束的时间
- User时间指的是花费在用户模式（内核之外）的cpu时间。这是唯一真正用于执行进程所花费的时间
- Sys时间指的是进程花费在内核中的cpu时间

#### 使用参照 %Z 显示系统页面大小 
```sh

$ /usr/bin/time -f "Page size: %Z bytes" ./fast_ping.sh> /dev/null
Page size: 4096 bytes

```