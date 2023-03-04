package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

func arithmetic() {
	sc := bufio.NewScanner(os.Stdin)

	sc.Scan()
	number, _ := strconv.Atoi(sc.Text())
	fmt.Println(number * 100)
}
