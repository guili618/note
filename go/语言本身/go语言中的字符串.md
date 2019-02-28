## Go语言中的字符串
---
### 思考字符串的角度
- 字符串的转换（）
- 字符串的拼接（concatenation）-- 如何高效拼接

### Go语言中字符串的特点

- 字符串是不可变的字节（byte）序列，本身是一个复合结构
- 头部指针指向字节数组，但是没有NULL结尾
- 字符串默认值为 ""，而不是nil
- 默认以UTF-8存储Unicode字符，字面量里允许使用十六进制，八进制和UTF编码格式
- 
  

### 字符串的定义



### 字符串的拼接

#### 使用 + 和 += 拼接字符串
```go
package main

import (
	"fmt"
)
func main(){
	s1 := "hello"
	s2 := "world"
	fmt.Println(s1 + " " + s2)
	fmt.Printf("s1的内存地址为： %p\n",&s1)
	s1 +=s2	   //由输出看出， +=执行的是就地修改
	fmt.Println(s1)
	fmt.Printf("s1的内存地址为： %p\n",&s1)
}
==============输出====================
hello world
s1的内存地址为： 0xc0000461c0
helloworld
s1的内存地址为： 0xc0000461c0
```
#### 使用strconv来拼接整型变量和字符串
```go
package main

import (
	"fmt"
	"strconv"
)
func main(){
	i := 2
	s := "pig"
	fmt.Println(strconv.Itoa(i) + s)

}
==============输出====================
2pig
```