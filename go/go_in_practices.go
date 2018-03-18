package main

import "fmt"


var msg  = `smt`
var char = 's'
func main() {
	fmt.Println("Hello," + "world "+string(char))
	fmt.Println(msg[0])
	fmt.Println(string("Hello"[1]))              // ASCII only
    fmt.Println(string([]rune("Hello, 世界")[1])) // UTF-8
    fmt.Println(string([]rune("Hello, 世界")[8])) // UTF-8
}


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