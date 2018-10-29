## logrotate 学习笔记
---
### logrotate配置文件的参数
| 参数 | 含义 |
| ------ | ------ |
|missingok | 如果日志文件丢失，则忽略，然后返回（不对日志文件进行轮替）|
|notifempty | 仅当源日志文件非空时才对其进行轮替|
|size 30k  | 限制实施轮替的日志文件大小，1M表示1MB|
|compress | 允许用gzip压缩旧的日志|
|weekly | 指定进行轮替的时间间隔，可以是  yearly, monthly，weekly或者 daily|
|rotate 5 | 需要保留的旧日志文件的归档数量|
| create 0600 root root | 指定所要创建的归档文件的模式，用户和用户组|
### 示例1
```bash
/etc/logrotate.d/program
/var/log/program.log {
missingok
notifempty
size 30k
compress
weekly
rotate 5
create 0600 root root
}

```
### 非root用户进行logrotate，详情见
- https://askubuntu.com/questions/405663/configuring-logrotate-without-root-access-per-user-log-rotation