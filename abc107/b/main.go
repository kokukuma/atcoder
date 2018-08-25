package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

type Input struct {
	h int
	w int
}

func ReadInput(reader io.Reader) (*Input, [][]string, error) {
	input := Input{}
	fmt.Fscan(reader, &input.h, &input.w)

	larger := input.h
	if input.h < input.w {
		larger = input.w
	}
	grid := make([][]string, larger)

	for i := 0; i < input.h; i++ {
		var v string
		fmt.Fscan(reader, &v)

		for _, char := range strings.Split(v, "") {
			grid[i] = append(grid[i], char)
		}
	}

	return &input, grid, nil
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	input, grid, err := ReadInput(reader)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(input, grid)

	// result := input.n - input.i + 1
	// fmt.Println(result)
}
