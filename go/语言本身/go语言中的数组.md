## Go语言中的数组
---
### 思考数组的角度

### Go语言中数组的特点
- 占用内存连续分配，因此CPU可以把正在使用的数据缓存更久
- 内存连续容易计算索引，可以快速迭代数组里的所有元素
### 数组的定义与声明
go语言中，数组是一个长度固定的数据类型，用于存储一段具有相同类型的元素的连续块.
数组的存储类型可以是内置类型，如整型或者字符串，也可以是某种结构类型

数组声明需要制定内部元素的数据类型，以及存储的元素总量，即数组长度
- 一旦声明，数组里的数据类型和长度就不能更改
- 数组初始化时，会把每个元素初始化为对应类型的0值
 

go数组的声明格式如下：
```go
//声明包含5个整型元素的数组
var array [5]int 
```
#### 使用数组字面量声明数组
```go
package main
import "fmt"

func main(){
    array := [5]int{1,2,3,4,5}
    fmt.Println(array)   //用变量名本身，打印所有元素
}
==============输出====================
[1 2 3 4 5]
```
#### go自动计算数组长度
```go
package main
import "fmt"

func main(){
    array := [...]int{1,2,3,4,5,90}
    fmt.Println(array)   //用变量名本身，打印所有元素
}
==============输出====================
[1 2 3 4 5 90]
```
#### 声明数组并指定特定元素的值
```go
package main
import "fmt"

func main(){
    array := [5]int{0:1,2:2,3:3}
    fmt.Println(array)   //用变量名本身，打印所有元素
}
==============输出====================
[1 0 2 3 0]
```

### 使用数组
#### 访问数组元素
```go
package main
import "fmt"

var array = [5]int{0,1,2,3,4}
func main(){
    for i:=0;i<5;i++{
        fmt.Println(array[i])
    }
    array[2] = 56
    fmt.Println(array)
}
==============输出====================
0
1
2
3
4
[0 1 56 3 4]
```
#### 数组整体赋值
- go语言中，数组是一个值，这意味着数组可以用在赋值操作中
- 数组变量的类型包括数组的长度和每个元素的类型，这个两个部分都相同的数组才是同类型数组，才能相互赋值

```go
package main
import "fmt"

var array  [5]int
var array2 [5]int
func main(){
	array := [...]int{1,2,3,4,5}
	array2 = array
	fmt.Println(array)
	fmt.Println(array2)
}
==============输出====================
[1 2 3 4 5]
[1 2 3 4 5]
```
数组类型不同，赋值会报错
```go
package main
import "fmt"

var array  [5]int
var array2 [4]int
func main(){
	array := [...]int{1,2,3,4,5}
	array2 = array
	fmt.Println(array)
	fmt.Println(array2)
}
==============输出====================
cannot use array (type [5]int) as type [4]int in assignment
```