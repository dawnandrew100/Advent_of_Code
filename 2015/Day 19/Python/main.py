from random import shuffle

def main():
  with open("input.txt", "r") as file:
    contents = file.readlines()
  substitution_dict = {}
  inverse_substitution_dict = {}
  doubles = set()
  for i in range(len(contents)-2):
    subs = contents[i].strip().split(" => ")
    substitution_dict.setdefault(subs[0], []).append(subs[1])
    inverse_substitution_dict[subs[1]] = subs[0]
    if len(subs[0]) == 2:
      letters = list(subs[0])
      doubles.add(letters[0])
  string = contents[-1]

  combos = part_one(string, substitution_dict, doubles)
  print(f"After calibration, the number of distinct combinations after one step of the molecule is {combos}!")

  from_e = part_two(string, inverse_substitution_dict)
  print(f"It takes {from_e} iterations to get from an electron to the final molecule!")

def part_one(sub_string, substitutions, double_letters):
  distinct_combos = set()
  for i, letter in enumerate(sub_string):
    stack = []
    stack.append(letter)
    if letter in double_letters:
      stack.append(sub_string[i+1])
    test_string = "".join(stack)
    if test_string in substitutions:
      for sub in substitutions[test_string]:
        new_string = sub_string[:i] + sub + sub_string[i+len(test_string):]
        distinct_combos.add(new_string)
  return len(distinct_combos)

def part_two(sub_string, inv_substitutions):
  solution = 0
  while not solution:
    count = 0
    local_string = sub_string
    s = ""
    keys = list(inv_substitutions.keys())
    shuffle(keys)
    while s != local_string:
      s = local_string
      for key in keys:
        if key in local_string:
          count += local_string.count(key)
          local_string = local_string.replace(key, inv_substitutions[key])
    solution = int(local_string == 'e') * count
  return solution
    
if __name__ == "__main__":
  main()
