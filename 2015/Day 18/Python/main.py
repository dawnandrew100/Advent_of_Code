import numpy as np
from numba import njit

def main():
  with open("..\\input.txt", "r") as file:
    contents = file.readlines()
  light_array, temporary_array = convert_to_binary_array(contents)
  new_light_array = animate_lights(light_array, temporary_array, 100)
  final = count_on_lights(new_light_array)
  
  new_stuck_light_array = animate_stuck_lights(light_array, temporary_array, 100)
  stuck_final = count_on_lights(new_stuck_light_array)
  print(f"The number of 'on' lights originally is: {final}!")
  print(f"After noticing that some lights are stuck, that number changes to: {stuck_final}!")

def convert_to_binary_array(input):
  temp_main_array = [list(line.strip()) for line in input]
  main_array = np.zeros((len(temp_main_array[0])+2,len(temp_main_array)+2), dtype=np.int8)
  for i in range(len(temp_main_array[0])):
    for j in range(len(temp_main_array[0])):
      if temp_main_array[i][j] == "#":
        main_array[i+1][j+1] = 1
  temp_array = np.zeros_like(main_array)
  return main_array, temp_array

@njit
def animate_lights(main_array, temp_array, steps):
  current_step = 0
  while current_step < steps:
    for i in range(1, len(main_array)-1):
      for j in range(1, len(main_array)-1):
        total = 0
        top_bottom = main_array[i][j+1] + main_array[i][j-1]
        left_right = main_array[i-1][j] + main_array[i+1][j]
        four_corners = main_array[i-1][j-1] + main_array[i+1][j-1] + main_array[i-1][j+1] + main_array[i+1][j+1]
        total = top_bottom + left_right + four_corners
        if main_array[i][j] == 1 and (total < 2 or total > 3):
          temp_array[i][j] = 0
        elif main_array[i][j] == 0 and total == 3:
          temp_array[i][j] = 1
        else:
          temp_array[i][j] = main_array[i][j]
    main_array = temp_array
    temp_array = np.zeros_like(main_array)
    current_step += 1
  return main_array

@njit
def animate_stuck_lights(main_array, temp_array, steps):
  current_step = 0
  while current_step < steps:
    for i in range(1, len(main_array)-1):
      for j in range(1, len(main_array)-1):
        if i == 1 and j == 1 or i == len(main_array)-2 and j == 1 or i == 1 and j == len(main_array)-2 or i == len(main_array)-2 and j == len(main_array)-2:
          temp_array[i][j] = 1
          continue
        total = 0
        top_bottom = main_array[i][j+1] + main_array[i][j-1]
        left_right = main_array[i-1][j] + main_array[i+1][j]
        four_corners = main_array[i-1][j-1] + main_array[i+1][j-1] + main_array[i-1][j+1] + main_array[i+1][j+1]
        total = top_bottom + left_right + four_corners
        if main_array[i][j] == 1 and (total < 2 or total > 3):
          temp_array[i][j] = 0
        elif main_array[i][j] == 0 and total == 3:
          temp_array[i][j] = 1
        else:
          temp_array[i][j] = main_array[i][j]
    main_array = temp_array
    temp_array = np.zeros_like(main_array)
    current_step += 1
  return main_array

def count_on_lights(main_array):
  return np.count_nonzero(main_array)
  
if __name__ == "__main__":
  main()
