package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"sort"
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

func Median(values []int) int {
	sort.Slice(values, func(i, j int) bool { return values[i] < values[j] })
	v := math.Trunc(float64(len(values)) / 2)
	return values[int(v)]
}

func Abs(value int) int {
	return int(math.Abs(float64(value)))
}

//
// func GetMinMax(values []int) (int, int) {
// 	var max = 0
// 	var min = 0
// 	for _, v := range values {
// 		if v > max {
// 			max = v
// 		}
// 		if v < min {
// 			min = v
// 		}
// 	}
// 	return min, max
// }

func main() {
	reader := bufio.NewReader(os.Stdin)

	input, err := ReadInput(reader)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(input)
	fmt.Println(Median(input.a))

	// sort.Slice(input.x, func(i, j int) bool { return Abs(input.x[i]) < Abs(input.x[j]) })
	//
	// min, max := GetMinMax(input.x[:input.k])
	//
	// if Abs(min) < Abs(max) {
	// 	fmt.Println(Abs(min)*2 + Abs(max))
	// } else {
	// 	fmt.Println(Abs(max)*2 + Abs(min))
	// }
}
