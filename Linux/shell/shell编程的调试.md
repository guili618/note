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