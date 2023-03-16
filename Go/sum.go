package main

import "fmt"

func sum() {
	var a int
	var b int
	fmt.Scan(&a)
	fmt.Scan(&b)

	if a+b == 21 {
		fmt.Println("Win")
	} else {
		fmt.Println(a + b)
	}
}
