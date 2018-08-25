package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

type Input struct {
	n int
	a []int
}

func ReadInput(reader io.Reader) (*Input, error) {
	input := Input{}
	fmt.Fscan(reader, &input.n)

	for i := 0; i < input.n; i++ {
		var v int
		fmt.Fscan(reader, &v)
		input.a = append(input.a, v)
	}
	return &input, nil
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	input, err := ReadInput(reader)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(input)

	// var output string
	// product := input.a * input.b
	// if product%2 == 0 {
	// 	output = "Even"
	// } else {
	// 	output = "Odd"
	// }
	//
	// fmt.Println(output)
}
