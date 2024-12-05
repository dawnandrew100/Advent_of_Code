def main():
  with open("..\\input.txt", "r") as file:
    contents = file.readlines()

  best_Sue = []
  aunt_500 = {}
  for line in contents:
    temp = line.strip().split(", ")
    temp = [x.split(": ") for x in temp]
    aunt_500.setdefault(temp[0][0], {})[temp[0][1]]=int(temp[0][2])
    for i in range(2):
      aunt_500.setdefault(temp[0][0], {})[temp[i+1][0]]=int(temp[i+1][1])

  aunt_traits = {"children": 3,
                "cats": 7,
                "samoyeds": 2,
                "pomeranians": 3,
                "akitas": 0,
                "vizslas": 0,
                "goldfish": 5,
                "trees": 3,
                "cars": 2,
                "perfumes": 1}

  for sue in aunt_500:
    aunt_match = 0 
    for trait in aunt_500[sue]:
      if aunt_500[sue][trait] == aunt_traits[trait]:
        aunt_match += 1
    if aunt_match == 3:
      best_Sue.append(sue)

  greater_traits = ["cats", "trees"]
  lesser_traits = ["pomeranians", "goldfish"]
  for sue in aunt_500:
    aunt_match = 0 
    for trait in aunt_500[sue]:
      if trait in greater_traits and aunt_500[sue][trait] > aunt_traits[trait]:
        aunt_match += 1
      elif trait in lesser_traits and aunt_500[sue][trait] < aunt_traits[trait]:
        aunt_match += 1
      elif trait not in greater_traits and trait not in lesser_traits and aunt_500[sue][trait] == aunt_traits[trait]:
        aunt_match += 1
    if aunt_match == 3:
      best_Sue.append(sue)

  print(f"The fake best Aunt Sue was Aunt {best_Sue[0]}, but now we know that the real one is Aunt {best_Sue[1]}!")
  
if __name__ == "__main__":
  main()
