## shell编程中的函数
---
### 函数的定义
- 定义方式1
```sh
function name {
        commands
        return #可选
}
```
- 定义方式2
```sh
name() {
        commands
        return #可选
}
```
>注意：若函数体和花括号在一行中，则{和第一个命令，最后一个命令和}之间都需要一个空格
### 函数中变量的作用域