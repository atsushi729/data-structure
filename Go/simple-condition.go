package main

import "fmt"

func condition() {
	var a string
	fmt.Scan(&a)

	if a == "candy" || a == "chocolate" {
		fmt.Println("Thanks!")
	} else {
		fmt.Println("No!")
	}
}
