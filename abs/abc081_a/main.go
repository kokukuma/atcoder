package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	bytes, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	target := string(bytes)

	fmt.Println(strings.Count(target, "1"))
}
