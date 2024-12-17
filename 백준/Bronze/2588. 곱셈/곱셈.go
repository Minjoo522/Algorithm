package main

import "fmt"

func main() {
	var a, b int

	fmt.Scanln(&a)
	fmt.Scanln(&b)
	number := b

	for number > 0 {
		digit := number % 10
		fmt.Println(a * digit)
		number /= 10
	}
	fmt.Println(a * b)
}