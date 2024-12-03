import re

with open("input.txt") as file:
  data = file.readlines()

def multiply(input: str) -> int:
  res, _ = re.subn('[(,)]', ' ', input)
  _, a, b = res.split()
  ans = int(a) * int(b)
  return ans
  
#part one
muls = []
for line in data:
  muls.extend(re.findall("mul\(\\d{1,3},\\d{1,3}\)",line))
pt_1_sum = sum(map(multiply, muls))

#part two
maybe_muls = []
for line in data:
  maybe_muls.extend(re.findall("(do\(\)|don\'t\(\)|mul\(\\d{1,3},\\d{1,3}\))",line))

do_or_not = "do"
pt_2_sum = 0
for item in maybe_muls:
  if item == "do()" or item == "don't()":
    do_or_not = item
    continue
  if do_or_not == "do()":
    pt_2_sum += multiply(item)

print(f"Initially the multiply program summed to {pt_1_sum}!")
print(f"After adjusting for dos and don'ts, the program sums to {pt_2_sum}!")
