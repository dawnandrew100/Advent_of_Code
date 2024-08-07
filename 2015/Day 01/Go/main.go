package main

import (
	"fmt"
	"os"
	"log"
)

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
			log.Fatal(err)
	}

	var floor uint8 = final_floor(content)
	var basement_position = basement(content)

	fmt.Printf("Final floor: %d\nFirst basement position: %d", floor, basement_position)
}

func final_floor(content_string []byte)uint8{
	var floor uint8 = 0

	for i:=0;i<len(content_string);i++ {
		if content_string[i] == '('{
			floor++
		} else if content_string[i] == ')' {
			floor--
		}
	}
	return floor
}

func basement(content_string []byte)int{
	var floor int8 = 0

	for i:=0;i<len(content_string);i++ {
		if content_string[i] == '('{
			floor++
		} else if content_string[i] == ')' {
			floor--
		}
		if floor == -1{
			return i+1
		}
	}
	return -1
}
