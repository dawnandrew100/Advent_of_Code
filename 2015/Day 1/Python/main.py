def main():
  with open("input.txt", "r") as file:
    input = file.read()

  basement, floor = floor_finder(input)
  print(f"Final floor: {floor}\nFirst basement position: {basement[0]}")

def floor_finder(contents):
  floor = 0
  position = 0
  basement = []
  for char in contents:
    match char:
      case "(":
        floor +=1
        position += 1
      case ")":
        floor -=1
        position += 1
  
    if floor == -1:
      basement.append(position)
  return basement, floor

if __name__ == "__main__":
  main()
