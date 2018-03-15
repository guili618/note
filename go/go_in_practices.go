package main

import "fmt"


var msg  = `smt`
var char = 's'
func main() {
	fmt.Println("Hello," + "world "+string(char))
	fmt.Println(string(msg[0])
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