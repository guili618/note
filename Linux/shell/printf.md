## printf命令笔记
---
### 示例

```sh
#!/bin/bash
#Filename: printf.sh
printf "%-5s %-10s %-4s\n" No Name Mark
printf "%-5s %-10s %-4.2f\n" 1 Sarath 80.3456
printf "%-5s %-10s %-4.2f\n" 2 James 90.9989
printf "%-5s %-10s %-4.2f\n" 3 Jeff 77.564

```
---
### printf 的格式规范字符
|字符 | 功能|
|--- |---|
| %d | 整数  |
| %u | 无符号 整数  |
| %o | 8进制 整数  |
| %x | 16进制 整数, 使用 a-f  |
| %X | 16进制 整数, 使用 A-F  |
| %c | 单个字符  |
| %s | 字符串字面量  |
| %b | 包含转义字符的字符串  |
| %% | 百分号  |
---
### printf 的格式规范修饰符
|修饰符 | 含义|
|--- |---|
| -  |  左对齐值|
| +  |  在整数前加上 + 或者 -.|
| (space) | 正数前加空格.|
| #  |8进制前加上 0,或者16进制前加上 0x or 0X.|
|width | 字段最小宽度; * 表示使用下一个参数作为宽度.|
|precision |显示整数时使用最小位数; 显示字符串时使用最大位数; * 表示使用下一个参数作为精度.|