## shell中的数组
---
### 数据的结构表
|结构|含义|
|---|---|
| ${array[i]}| 替换元素 i 的值 |
| $array | 替换为数组第一个元素的值 (array[0]) |
| ${array[*]}| 替换为所有元素的值 |
| ${#array[*]}| 替换为元素的个数 |
| array[i]=val | 将val的值保存到 array[i] |
###　数组的创建
- 用declare -a 创建
```sh
$ declare -a array

```
- 赋值时创建
```sh
$ array[0]=element1
$ echo ${array[0]}
element1


```
- 整数数组的声明
```sh
$ typeset -i array
$ array[1]=6
$ echo ${array[1]}
6


```
---
### 数组的赋值

- name[index]=value
```sh
$ array[1]=element2
$ echo ${array[1]}
element2


```
- name=(value1,value2,value3,...)
```sh
$ days=(mon tue web thu fri sat sun)
$ for i in {0..6};do echo "${days[$i]}"; done
mon
tue
web
thu
fri
sat
sun

```
- 指定索引赋值
```sh
$ days=([0]=Sun [1]=Mon [2]=Tue [3]=Wed [4]=Thu [5]=Fri [6]=Sat)
$ for i in {0..6};do echo "${days[$i]}"; done
Sun
Mon
Tue
Wed
Thu
Fri
Sat


```
---
### 数组操作
- 输出数组所有内容
```sh

$ animals=("a dog" "a cat" "a fish")
$ for i in ${animals[*]}; do echo $i; done
a
dog
a
cat
a
fish
#####################################
$ for i in ${animals[@]}; do echo $i; done
a
dog
a
cat
a
fish
#####################################
$ for i in "${animals[*]}"; do echo $i; done
a dog a cat a fish
#####################################
$ for i in "${animals[@]}"; do echo $i; done
a dog
a cat
a fish

```
- 确定数组的元素数量
  
```sh
$ animals=("a dog" "a cat" "a fish")
$ echo ${#animals[@]}
3

```
- 确定数组中某个元素的长度
```sh
$ animals=("a dog" "a cat" "a fish")
$ echo ${#animals[2]}
6

```

---
### 查找数组中使用的下标
- ${!array[*]}
- ${!array[@]}
```sh

$ foo=([2]=a [4]=b [6]=c)
$ for i in "${foo[@]}"; do echo $i; done
a
b
c
#######################################
$ foo=([2]=a [4]=b [6]=c)
guiax@ubuntu-guiax:~$ for i in "${!foo[@]}"; do echo $i; done
2
4
6

```

---
### 数组的尾部增加元素

```sh
$ foo=(a b c)
$ echo ${foo[@]}
a b c
$ foo+=(d e f "g h")
$ for i in "${foo[@]}"; do echo $i; done
a
b
c
d
e
f
g h


```

---
### 数组的排序

```sh
#!/bin/bash
# array-sort : Sort an array
a=(f e d c b a)
echo "Original array: ${a[@]}"
a_sorted=($(for i in "${a[@]}"; do echo $i; done | sort))
echo "Sorted array: ${a_sorted[@]}"

```

---
### 数组的删除

```sh


```