package main

import "fmt"

func main() {
	a := 0
	b := 1
	temp := 0
	sum := 0
	for b < 4e6 {
		temp = b
		b = b + a
		a = temp
		if b % 2 == 0 { sum += b }
	}
	fmt.Printf("Sum of all even fibonnaci seq terms < 4e6 = %d\n", sum)
}
