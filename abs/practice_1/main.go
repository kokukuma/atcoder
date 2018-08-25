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
	c int
	s string
}

func ReadInput(reader io.Reader) (*Input, error) {
	input := Input{}
	fmt.Fscan(reader, &input.a)
	fmt.Fscan(reader, &input.b, &input.c)
	fmt.Fscan(reader, &input.s)
	return &input, nil
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	input, err := ReadInput(reader)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	sum := input.a + input.b + input.c
	fmt.Printf("%d %s\n", sum, input.s)
}
