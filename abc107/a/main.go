package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

type Input struct {
	n int
	i int
}

func ReadInput(reader io.Reader) (*Input, error) {
	input := Input{}
	fmt.Fscan(reader, &input.n, &input.i)
	return &input, nil
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	input, err := ReadInput(reader)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	result := input.n - input.i + 1
	fmt.Println(result)
}
