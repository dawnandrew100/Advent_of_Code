from itertools import combinations

def main():
  with open("input.txt", "r") as file:
    contents = file.readlines()
  contents = [int(line.strip()) for line in contents]

  total = 0
  minimum_num = float('inf')
  min_container_total = 0
  min_combo = []
  for i in range(1, len(contents)):
    for combo in combinations(contents, i):
      if sum(combo) == 150:
        total += 1
        if i < minimum_num:
          minimum_num = i

  for combo in combinations(contents, minimum_num):
    if sum(combo) == 150:
      min_container_total += 1
      min_combo.append(combo)

  print(f"The total number of container combinations that equal 150 is {total}!")
  print(f"Using the least number of containers, which is {minimum_num}, there are {min_container_total} combinations!")    
  print(f"The {min_container_total} combinations are: {min_combo}")
  
if __name__ == "__main__":
  main()
