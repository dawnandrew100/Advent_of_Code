with open("input.txt", "r") as file:
  input = file.read()

floor = 0
position = 0
for char in input:
  match char:
    case "(":
      floor +=1
      position += 1
    case ")":
      floor -=1
      position += 1

  if floor == -1:
    print(position)

print(floor)
