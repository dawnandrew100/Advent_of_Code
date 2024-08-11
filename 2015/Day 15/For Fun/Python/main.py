import numpy as np
from numpy.random import multinomial

def main():
  with open("input.txt", "r") as file:
    contents = file.readlines()
  ingredients = {}
  
  for line in contents:
    filtered = "".join(filter(lambda char: char not in ":,", line))
    components = filtered.split()
    for i in range(1, len(components), 2):
      ingredients.setdefault(components[0], {})[components[i]] = int(components[i+1])
  best_score, best_amount = 0, []
  i=0
  checked = []
  while i < 30:
    amount = multinomial(100, [1/len(ingredients)] * len(ingredients))
    while any(np.array_equal(a, amount) for a in checked):
      amount = multinomial(100, [1/len(ingredients)] * len(ingredients))
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for n, ingredient in enumerate(ingredients):
      capacity += amount[n] * ingredients[ingredient]["capacity"]
      durability += amount[n] * ingredients[ingredient]["durability"]
      flavor += amount[n] * ingredients[ingredient]["flavor"]
      texture += amount[n] * ingredients[ingredient]["texture"]
    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)
    current_score = capacity*durability*flavor*texture
    best_score = max(0, current_score, best_score)
    if current_score == best_score:
      best_amount = amount
    i += 1
    checked.append(amount)

  print(best_score)
  print(best_amount)
    
if __name__ == "__main__":
  main()
