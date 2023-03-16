package main

import (
    "fmt"
)

func main() {
	var list []string
	fmt.Scan(&list)

	m := make(map[string]struct{})
    newList := make([]string, 0)

    for _, element := range list {
        
        if _, ok := m[element]; !ok {
            m[element] = struct{}{}
            newList = append(newList, element)
        }
    }
}
