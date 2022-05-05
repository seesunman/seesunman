package main

import "fmt"

func select_sort(seq []int) {
	l := len(seq)
	for i := 0; i < l-1; i++ {
		min_idx := i
		for j := i; j < l; j++ {
			if seq[j] < seq[min_idx] {
				min_idx = j
			}
		}
		if i != min_idx {
			seq[i], seq[min_idx] = seq[min_idx], seq[i]
		}
	}
}

func main() {
	var lst = []int{3, 1, 2, 5, 6, 7, 4}
	select_sort(lst)
	fmt.Printf("lst: %v\n", lst)
}

