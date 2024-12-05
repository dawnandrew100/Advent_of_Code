from collections import defaultdict

def main():
  with open("..\\input.txt", "r") as file:
    contents = file.readline()
  print(f"Santa single-handedly delievered presents to {solo_santa(contents)} houses.")
  print(f"Santa with the help of Robo-Santa delievered presents to {robo_santa_plus(contents)} houses.")

def solo_santa(directions: str) -> int:
  presents_delivered = defaultdict(int)
  x, y = 0, 0
  presents_delivered["0, 0"] += 1
  
  for direction in directions:
    match direction:
      case "^":
        y += 1
        coord = f"{x}, {y}"
        presents_delivered[coord] += 1
      case "v":
        y -= 1
        coord = f"{x}, {y}"
        presents_delivered[coord] += 1
      case ">":
        x += 1
        coord = f"{x}, {y}"
        presents_delivered[coord] += 1
      case "<":
        x -= 1
        coord = f"{x}, {y}"
        presents_delivered[coord] += 1
  return len(presents_delivered)

def robo_santa_plus(directions: str) -> int:
  presents_delivered = defaultdict(int)
  santa_x, santa_y = 0, 0
  robo_x, robo_y = 0, 0
  
  presents_delivered["0, 0"] += 2
  compass = {"^":1,"v":-1,"<":-1,">":1}
  
  i = 0
  for direction in directions:
    if i%2 == 0:
      if direction == "^" or direction == "v":
        santa_y += compass[direction]
      elif direction == "<" or direction == ">":
        santa_x += compass[direction]
      coord = f"{santa_x}, {santa_y}"
      presents_delivered[coord] += 1
      i += 1
    elif i%2 != 0:
      if direction == "^" or direction == "v":
        robo_y += compass[direction]
      elif direction == "<" or direction == ">":
        robo_x += compass[direction]
      coord = f"{robo_x}, {robo_y}"
      presents_delivered[coord] += 1
      i += 1
  return len(presents_delivered)

if __name__ == "__main__":
  main()
