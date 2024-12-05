def main():
  with open("..\\input.txt", "r") as file:
    contents = file.readlines()

  ingredients = {}
  for line in contents:
    filtered = "".join(filter(lambda char: char not in ":,", line))
    components = filtered.split()
    for i in range(1, len(components), 2):
      ingredients.setdefault(components[0], {})[components[i]] = int(components[i+1])
  best_score, best_amount = 0, ""

  for i in range(100):
    for j in range(100-i):
      for k in range(100-i-j):
        h = 100-i-j-k
        capacity = ingredients["Frosting"]["capacity"]*i + ingredients["Candy"]["capacity"]*j + ingredients["Butterscotch"]["capacity"]*k + ingredients["Sugar"]["capacity"]*h
        durability = ingredients["Frosting"]["durability"]*i + ingredients["Candy"]["durability"]*j + ingredients["Butterscotch"]["durability"]*k + ingredients["Sugar"]["durability"]*h
        flavor = ingredients["Frosting"]["flavor"]*i + ingredients["Candy"]["flavor"]*j + ingredients["Butterscotch"]["flavor"]*k + ingredients["Sugar"]["flavor"]*h
        texture = ingredients["Frosting"]["texture"]*i + ingredients["Candy"]["texture"]*j + ingredients["Butterscotch"]["texture"]*k + ingredients["Sugar"]["texture"]*h
        calories = ingredients["Frosting"]["calories"]*i + ingredients["Candy"]["calories"]*j + ingredients["Butterscotch"]["calories"]*k + ingredients["Sugar"]["calories"]*h
        #UNCOMMENT BELOW FOR PART TWO ANSWER
        #if calories != 500:
          #continue
        capacity = max(0, capacity)
        durability = max(0, durability)
        flavor = max(0, flavor)
        texture = max(0, texture)
        total_score = capacity*durability*flavor*texture
        best_score = max(0, total_score, best_score)
        if total_score == best_score:
          best_amount = f"{i} teaspoons of Frosting, {j} teaspoons of Candy, {k} teaspoons of Butterscotch, {h} teaspoons of Sugar"

  print(f"The best score is {best_score} which can be obtained with the followings amounts: ")
  print(best_amount)

if __name__ == "__main__":
  main()
