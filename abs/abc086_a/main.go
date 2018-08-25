package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

type Input struct {
	a int
	b int
}

func ReadInput(reader io.Reader) (*Input, error) {
	input := Input{}
	fmt.Fscan(reader, &input.a, &input.b)
	return &input, nil
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	input, err := ReadInput(reader)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var output string
	product := input.a * input.b
	if product%2 == 0 {
		output = "Even"
	} else {
		output = "Odd"
	}

	fmt.Println(output)
}
