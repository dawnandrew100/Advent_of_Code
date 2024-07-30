package main

import (
	"fmt"
	"os"
	"log"
	"strings"
	"strconv"
)
type box struct {
	length int
	width int
	height int
}

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
			log.Fatal(err)
	}
	var tbd_wrapped []box = parse_data(content)
	var total_paper_sqft int = wrapping_paper(tbd_wrapped)
	var total_ribbon_ft int = ribbon(tbd_wrapped)
	fmt.Printf("Wraping paper needed: %d sqft\nRibbon needed: %d ft\n", total_paper_sqft, total_ribbon_ft)
}

func parse_data(data []byte)[]box{
	content_string := string(data)
	content_array := strings.Split(content_string, "\n")

	var presents []box
	for i:=0;i<len(content_array);i++ {
		temp := strings.Split(content_array[i], "x")
		length, err:= strconv.Atoi(temp[0])
		if err != nil {
			log.Fatal(err)
		}
		width, err:= strconv.Atoi(temp[1])
		if err != nil {
			log.Fatal(err)
		}
		height, err:= strconv.Atoi(temp[2])
		if err != nil {
			log.Fatal(err)
		}
		present := box{length: length, width: width, height: height}
		presents = append(presents, present)
	}
	return presents
}

func second_smallest(dimensions []int)int{
	var min int = dimensions[0]
	var min2 int = dimensions[1]
	for i:=1;i<len(dimensions);i++{
		if dimensions[i] < min {
			min2 = min
			min = dimensions[i]
		} else if dimensions[i] >= min && dimensions[i] <= min2 {
			min2 = dimensions[i]
		}
	}
	return min2
}

func wrapping_paper(dimenstions []box)int{
	var total int = 0
	for i:=0;i<len(dimenstions);i++{
		side1 := dimenstions[i].length*dimenstions[i].width
		side2 := dimenstions[i].width*dimenstions[i].height
		side3 := dimenstions[i].height*dimenstions[i].length
		smallest_side := min(side1,side2,side3)
		total += (2*side1) + (2*side2) + (2*side3) + smallest_side 
	}
	return total
}

func ribbon(dimensions []box)int{
	var total int = 0
	for i:=0;i<len(dimensions);i++{
		var dimension_array []int = []int{dimensions[i].height,dimensions[i].length,dimensions[i].width}
		area1 := min(dimensions[i].height,dimensions[i].length,dimensions[i].width)
		area2 := second_smallest(dimension_array)
		bow := dimensions[i].height*dimensions[i].length*dimensions[i].width
		ribbon := (2*area1) + (2*area2)
		total += ribbon + bow
	}
	return total
}
