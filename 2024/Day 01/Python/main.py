from collections import defaultdict

with open("input.txt") as file:
  data = file.readlines()

firstlist, secondlist = [], []

for line in data:
  newdata, newdata2 = line.strip().split("  ")
  firstlist.append(int(newdata))
  secondlist.append(int(newdata2))

firstlist.sort()
secondlist.sort()

part_one = sum(map(lambda x, y: abs(x-y), firstlist, secondlist))
print(f"The total distance between the lists is {part_one}!")

firstdict, seconddict = defaultdict(int), defaultdict(int)

for i in range(1000):
  firstdict[firstlist[i]] += 1
  seconddict[secondlist[i]] += 1
  
part_two_total = 0
for element in firstdict:
  if element in seconddict:
    part_two_total += element * firstdict[element] * seconddict[element]

print(f"The similarity score between the two lists is {part_two_total}!")
