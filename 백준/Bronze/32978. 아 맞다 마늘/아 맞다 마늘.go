package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(line))

	line, _ = reader.ReadString('\n')
	ingredients := strings.Fields(line)
	sort.Strings(ingredients)

	line, _ = reader.ReadString('\n')
	used := strings.Fields(line)
	sort.Strings(used)

	for i := 0; i < n; i++ {
		if ingredients[i] != used[i] {
			fmt.Println(ingredients[i])
			break
		}
	}
}
