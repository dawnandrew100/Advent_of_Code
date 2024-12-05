import re
import numpy as np
import numpy.typing as npt
from numba import njit

def main():
  with open("..\\input.txt", "r") as file:
    contents = file.read().split("\n")

  christmas_display = np.zeros((1000,1000))
  total_on = part_one(christmas_display, contents)
  christmas_display = np.zeros((1000,1000))
  total_brightness = part_two(christmas_display, contents)
  print(f"There are {total_on:,} lights on in total following the first set of instructions.")
  print(f"The total brightness of these lights is {total_brightness:,} light units following the second set of instructions.")

def part_one(light_array: npt.ArrayLike, file_contents: list[str]) -> int:
  for word in file_contents:
    action = re.search(r"([a-z]+\s[a-z]+|\w+)", word).group()
    from_x, from_y  = int(re.findall(r"\d+", word)[0]), int(re.findall(r"\d+", word)[1])
    to_x, to_y = int(re.findall(r"\d+", word)[2]), int(re.findall(r"\d+", word)[3])
    match action:
      case "toggle":
        toggle(light_array, from_x, from_y, to_x, to_y)
      case "turn on":
        turn_on(light_array, from_x, from_y, to_x, to_y)
      case "turn off":
        turn_off(light_array, from_x, from_y, to_x, to_y)
  return np.count_nonzero(light_array)

@njit
def toggle(light_array: npt.ArrayLike, start_x: int, start_y: int, end_x: int, end_y: int):
  for i in range(start_x, end_x+1):
    for j in range(start_y, end_y+1):
      if light_array[i][j] == 0:
        light_array[i][j] = 1
      else:
        light_array[i][j] = 0

def turn_on(light_array: npt.ArrayLike, start_x: int, start_y: int, end_x: int, end_y: int):
  light_array[start_x:end_x+1, start_y:end_y+1] = 1


def turn_off(light_array: npt.ArrayLike, start_x: int, start_y: int, end_x: int, end_y: int):
  light_array[start_x:end_x+1, start_y:end_y+1] = 0

def part_two(light_array: npt.ArrayLike, file_contents: list[str]) -> int:
  for word in file_contents:
    action = re.search(r"([a-z]+\s[a-z]+|\w+)", word).group()
    from_x, from_y  = int(re.findall(r"\d+", word)[0]), int(re.findall(r"\d+", word)[1])
    to_x, to_y = int(re.findall(r"\d+", word)[2]), int(re.findall(r"\d+", word)[3])
    match action:
      case "toggle":
        toggle_brightness(light_array, from_x, from_y, to_x, to_y)
      case "turn on":
        turn_on_brightness(light_array, from_x, from_y, to_x, to_y)
      case "turn off":
        turn_off_brightness(light_array, from_x, from_y, to_x, to_y)
  return np.sum(light_array)

def toggle_brightness(light_array: npt.ArrayLike, start_x: int, start_y: int, end_x: int, end_y: int):
  light_array[start_x:end_x+1, start_y:end_y+1] += 2

def turn_on_brightness(light_array: npt.ArrayLike, start_x: int, start_y: int, end_x: int, end_y: int):
  light_array[start_x:end_x+1, start_y:end_y+1] += 1

@njit
def turn_off_brightness(light_array: npt.ArrayLike, start_x: int, start_y: int, end_x: int, end_y: int):
  for i in range(start_x, end_x+1):
    for j in range(start_y, end_y+1):
      if light_array[i][j] == 0:
        continue
      light_array[i][j] -= 1

if __name__ == "__main__":
  main()
