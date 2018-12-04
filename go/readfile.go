package main

import (
	"bufio"
	"fmt"
	"os"
	"log"
)

func main() {

file, err := os.Open("D:snake.py")
if err != nil {
    log.Fatal(err)
}
defer file.Close()

scanner := bufio.NewScanner(file)
for scanner.Scan() {
    fmt.Println(scanner.Text())
}

if err := scanner.Err(); err != nil {
    log.Fatal(err)
}
}