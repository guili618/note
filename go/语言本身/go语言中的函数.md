## Go语言中的函数
---
### 思考函数的角度
- 入参
- 实参到形参的传递
- 返回值
- 匿名函数
- 函数式编程
### Go语言中函数的特点
- 无需前置声明
- 支持不定长变参
- 支持多返回值
- 支持命名返回值
- 支持匿名函数和闭包

- 不支持命名嵌套定义（nested）
- 不支持同名函数重载
- 不支持默认参数
  
### 函数的定义与声明
go函数的声明格式如下：
```go
func funcName(param1 type1, param2 type2) (return1 type1, return2 type2) {
        // function body
        return value1, value2
}
``` 
- 函数首字母大写可被其他包访问，小写只能在包内使用
#### 多个相邻的相同类型参数可以使用简写模式
```go
func add(a,b int) int {
    return a + b
}
```
#### 函数签名
函数类型又叫函数签名，即函数的定义首行去掉函数名，参数名和{}，可以使用fmt.Printf的%T
格式化参数打印函数的类型
```go
package main

import fmt

func add(a,b int) int {
	return a + b
}

func main(){
	fmt.Printf("%T \n",add)
}
//函数签名：func(int, int) int
```
#### 不定参数
go支持可变数量的参数，但是注意以下几点：
- 所有不定参数的类型必须相同
- 不定参数必须是函数的最后一个参数
- 不定参数名在函数体内相当于 slice
- slice可以作为参数传递给指定不定参数，slice名后要加  "..."
- 形参为不定参数的函数与形参为slice的参数类型不相同
```go
package main

import "fmt"

func sumNumbers(numbers ...int) int {
	total := 0
	for _, number := range numbers {
		total += number
	}
	return total
}

func main() {
	result := sumNumbers(1, 2, 3, 4)
	fmt.Printf("The result is %v\n", result)
}
```
#### 命名返回值
```go
func sayHi() (x, y string){
    x = "hello"
    y = "world"
    return 
}
使用命名返回值时，无需显式的返回相应的变量--naked return
```
#### 多值返回
如果多值返回有error类型，一般将error类型作为最后一个返回值
```go
package main

import "fmt"

func getPrize() (int, string) {
	i := 2
	s := "goldfish"
	return i, s
}

func main() {
	quantity, prize := getPrize()
	fmt.Printf("You won %v %v\n", quantity, prize)
}
```

#### 函数赋值给变量
```go
package main
import f "fmt"

var p = f.Println

func main() {
	p("函数赋值给变量")
	f.Printf("%T \n",p)
}

==============输出====================
函数赋值给变量
func(...interface {}) (int, error)


```

### 匿名函数