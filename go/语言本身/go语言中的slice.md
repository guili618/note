## Go语言中的slice
---
### 思考slice的角度

### Go语言中slice的特点

- slice的底层也是连续分配，因此可以获得索引，迭代以及为gc优化的好处
- 是一种引用类型
- append函数对slice的操作是就地修改（in-place），原slice的内存地址不变
  

### slice的定义
slice是一种数据结构，围绕动态数组的概念构建，可以自动增长和缩小

#### slice的内部实现
slice有3个字段的数据结构
- 指向底层数组的指针
- slice元素的个数（即长度）
- 底层数组容量
  
```go
type slice struct {
	array unsafe.Pointer   
	len   int
	cap   int
}
``` 

#### 声明一个长度为2的空slice

```go
package main
import "fmt"

func main(){
	var names = make([]string,2)
	names[0] = "lilei"
	names[1] = "hanmeimei"
	fmt.Println("添加元素q前：")
    fmt.Println(names)
    fmt.Printf("切片的地址是 %p \n", &names)
	names = append(names,"third")
    fmt.Println("添加元素后：")
    fmt.Printf("切片的地址是 %p \n", &names)
    fmt.Println(names)
    names = append(names[:2])
    fmt.Println(names)
}
==============输出====================
添加元素q前：
[lilei hanmeimei]
切片的地址是 0xc000050400
添加元素后：
切片的地址是 0xc000050400
[lilei hanmeimei third]
```
#### 删除slice中的元素
