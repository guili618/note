package main

import (
    "fmt"
    "net/http"
)

func index(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "<h1>Hello Go</h1>")
}

func main() {
    http.HandleFunc("/", index)
    fmt.Println("web server start at port 8080")
    http.ListenAndServe(":8080", nil)
}