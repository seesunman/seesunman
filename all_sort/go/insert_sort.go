package main

import "fmt"

func insert_sort(seq []int) {
	l := len(seq)
	for i := 1; i < l; i++ {
		pos := i
		value := seq[pos]
		for {
			if pos > 0 && seq[pos-1] > value {
				seq[pos] = seq[pos-1]
				pos--
			} else {
				break
			}
		}
		seq[pos] = value
	}

}

func main() {
	var lst = []int{3, 1, 2, 5, 6, 7, 9, 0}
	insert_sort(lst)
	fmt.Printf("lst: %v\n", lst)
}

