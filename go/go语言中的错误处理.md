# Go语言中的错误处理
---
## 内容提要
- go处理error的方式
- 理解error类型
- 创建error
- 设置error的格式
- 从函数中返回error
- error和可用性
- panic的使用

## go处理error的方式
- Go将error作为一种类型，这意味着可以将错误传递给函数和方法,那么在调用他们的时候，可以返回一个类型为error的值
- 在Go语言中，有一种约定是，如果没有发生错误，返回的错误值为nil。
- Rob Pike的博文《Errors are values》对此有更深的表述，https://blog.golang.org/errors-are-values
```go
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	//var file []byte
	//var err error
	file, err := ioutil.ReadFile("foo.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("%s", file)
}
```

## 理解error类型
- 在Go语言中，error是一个值，标准库声明了接口error

```go
type error interface{
    Error() string
}
```

## 创建error

```go
package main

import (
	"errors"
	"fmt"
)

func main() {
	err := errors.New("Something went wrong")
	if err != nil {
		fmt.Println(err)
	}
}
```

## 设置error的格式

```go
package main

import (
	"fmt"
)

func main() {
	name, role := "Li Zhi", "Singer"
	err := fmt.Errorf("The %v %v quit", role, name)
	if err != nil {
		fmt.Println(err)
	}
}
```

## 从函数中返回error

```go
package main

import (
	"fmt"
)

// Half takes an integer and returns half the value
func Half(numberToHalf int) (int, error) {
	if numberToHalf%2 != 0 {
		return -1, fmt.Errorf("Cannot half %v", numberToHalf)
	}
	return numberToHalf / 2, nil
}

func main() {
	n, err := Half(19)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(n)
}
```