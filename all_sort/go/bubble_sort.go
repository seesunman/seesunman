package main

import "fmt"

func bubble_sort(seq []int){
	l := len(seq)
	for i := 0; i < l-1; i++{
		for j := 0; j < l-i-1; j++{
		if seq[j] > seq[j+1]{
			seq[j], seq[j+1] = seq[j+1], seq[j]
		}
		}
	}
}

func main(){
	var lst = []int{1, 3, 2, 4, 5, 7, 6}
	bubble_sort(lst)
	fmt.Printf("%v", lst)
}
