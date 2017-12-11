Types & Declarations
```go
age := 80
name := "daffy"
weight := 62.3
loons := []string{"bugs", "daffy", "taz"}
ages := map[string]int{ // Correct for 2017
    "daffy": 80,
    "bugs":  79,
    "taz":   63,
}

```
Define A Function
```go
// Add adds a to b
func Add(a, b int) int {
    return a + b
}

```

list/slice
```go
names := []string{"bugs", "taz", "tweety"}
fmt.Println(names[0]) // bugs
names = append(names, "elmer")
fmt.Println(len(names)) // 4
fmt.Println(names[2:])  // [tweety elmer]
for _, name := range names {
    fmt.Println(name)
}
for i, name := range names {
    fmt.Printf("%s at %d\n", name, i)
}

```
dict/map
```go
ages := map[string]int{ // Correct for 2017
    "daffy": 80,
    "bugs":  79,
    "taz":   63,
}
ages["elmer"] = 80
fmt.Println(ages["bugs"]) // 79
_, ok := ages["daffy"]
fmt.Println(ok) // true
delete(ages, "taz")
for name := range ages { // Keys
    fmt.Println(name)
}
for name, age := range ages { // Keys & values
    fmt.Printf("%s is %d years old\n", name, age)
}

```

while loop
```go
// Largest Fibonacci under 10,000
a, b := 1, 1
for b < 10000 {
    a, b = b, a+b
}


```


Files
```go
file, err := os.Open("song.txt")
if err != nil {
    return err
}
defer file.Close()
// Iterate over lines
scanner := bufio.NewScanner(file) // file is an io.Reader
for scanner.Scan() {
    fmt.Println(scanner.Text())
}
return scanner.Err()

```
Exceptions/Return Error
```go
func div(a, b int) (int, error) {
    if b == 0 {
        return 0, fmt.Errorf("b can't be 0")
    }
    return a / b, nil
}

// ...

val, err := div(1, 0)
if err != nil {
    fmt.Printf("error: %s\n", err)
}

```
Concurrency
```go
go add(1, 2)
```
Communicating between threads/goroutines
```go

ch := make(chan int)

// ...

// Send message from a goroutine
// (this will block is there no one reading)
ch <- 353

// ...

// Read message in a goroutine
// (this will block is nothing in channel)
val := <-ch

```
Sorting
```go

// ByLen implements sort.Interface
type ByLen []string

func (a ByLen) Len() int           { return len(a) }
func (a ByLen) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByLen) Less(i, j int) bool { return len(a[i]) < len(a[j]) }

// ...

names := []string{"taz", "bugs", "daffy"}
// Lexicographical order
sort.Strings(names)
// Reverse lexicographical order
sort.Sort(sort.Reverse(sort.StringSlice(names)))
// Sort by length
sort.Sort(ByLen(names))

```

Web Server
```go
package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello Go")
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
```
HTTP Request
```go
url := "https://httpbin.org/ip"
resp, err := http.Get(url)
if err != nil {
    log.Fatalf("error: can't get %q - %s", url, err)
}
defer resp.Body.Close()
dec := json.NewDecoder(resp.Body)
reply := make(map[string]interface{})
if err := dec.Decode(&reply); err != nil {
    log.Fatalf("error: can't decode reply - %s", err)
}
fmt.Println(reply["origin"])
```

Encode/Decode JSON
```go
// We can also use anonymous struct
type Loon struct {
    Name string `json:"name"`
    Age  int    `json:"age"`
}

// ...

var data = []byte(`{
    "name": "bugs",
    "age": 79
}`)
loon := Loon{}
if err := json.Unmarshal(data, &loon); err != nil {
    return err
}
enc := json.NewEncoder(os.Stdout)
if err := enc.Encode(loon); err != nil {
    return err
}


```
Print Object for Debug/Log
```go
daffy := Actor{
    Name: "Daffy",
    Age:  80,
}
fmt.Printf("%#v\n", daffy)


```

Object Oriented
```go
type Cat struct {
    name string
}

func NewCat(name string) *Cat {
    return &Cat{name: name}
}

func (c *Cat) Greet(other string) {
    fmt.Printf("Meow %s, I'm %s\n", other, c.name)
}

// ...

c := NewCat("Grumpy")
c.Greet("Grafield")
```


```go

```


```go

```


```go

```