## shell编程中的条件语句
---
### if条件语句的一般格式

```sh
if command
then 
        command
        command
elif command
then 
        command
        command
else
fi

```
---

### case条件语句的一般格式
**pattern 中可以使用shell的通配符**
- ? 代表任意单个字符
- \* 代表0或多个任意字符
- [...] 可以用来指定中括号里面出现的任意单个字符
- | 用在两个模式之间，其效果等同于逻辑  "或"
```sh
case value  
in
        pattern1) command;;  
        pattern2) command;;
        pattern3) command;;
        pattern4) command;;
        pattern5|pattern6) command;;
esac

```
---