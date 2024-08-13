def main():
  with open("input.txt", "r") as file:
    contents = file.readlines()
  contents = [int(line.strip()) for line in contents]

  ptr1, ptr2, ptr3 = 0,1,1
  counter = 1
  eggnog_combinations = 0
  eggnog = []
  eggnog.append(contents[0])
  while ptr1 < len(contents):
    if sum(eggnog) < 150 and ptr2 < len(contents):
      eggnog.append(contents[ptr2])
      ptr2 += 1
      continue
    if sum(eggnog) > 150:
      eggnog = [contents[ptr1]]
      counter += 1
      ptr2 = ptr1 + counter
      ptr3 += 1
      continue
    if ptr3 >= len(contents)-1:
      if ptr1 >= len(contents) - 1:
        break
      ptr1 += 1
      eggnog = [contents[ptr1]]
      ptr3 = ptr1 + 1
      ptr2 = ptr1 + 1
      continue
    if ptr2 > len(contents)-1:
      eggnog = [contents[ptr1]]
      ptr2 = ptr3 + 1
      ptr3 += 1
      continue
    eggnog_combinations += 1
    print(sum(eggnog))
    print(eggnog_combinations)
    print(eggnog)
    eggnog = [contents[ptr1]]
  
if __name__ == "__main__":
  main()
