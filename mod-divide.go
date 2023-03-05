package main

import "fmt"

func mod() {
	var a int
	var b int
	fmt.Scan(&a)
	fmt.Scan(&b)

	fmt.Println(b / a)
	fmt.Println(b % a)
}
