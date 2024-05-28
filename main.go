package main

import (
	"fmt"
	"sort"
)

func main() {

	testUserIDs := []int{1, 4, 5, 22, 212, 213, 116, 227, 229, 230, 147, 150, 210, 301, 337, 316, 325}
	sort_array := sort.IntSlice(testUserIDs)
	fmt.Print(`[`)
	for _, v := range sort_array {
		fmt.Print(v)
		if v != sort_array[len(sort_array)-1] {
			fmt.Print(`, `)
		}
	}
	fmt.Print(`]`)

}
