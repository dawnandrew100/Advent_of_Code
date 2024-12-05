import json

def main():
  with open("..\\input.json", "r") as file:
    j_content = json.load(file)
    content = json.dumps(j_content)
  print(f"The sum of all of the numbers in the JSON input is {sum_all_json(content)}!\n"
        f"The sum of all of the numbers with all of the instances of 'red' being turned to zero is {sum_minus_red(j_content)}!")

def sum_all_json(input: str) -> int:
  num_place = []
  total = 0
  for line in input:
    try:
      if line == "-" or isinstance(int(line), int):
        num_place.append(line)
    except ValueError:
      if num_place:
        total += int("".join(num_place))
      num_place = []
  return total

def sum_minus_red(input: object) -> int:
  if isinstance(input, dict):
    if "red" in input.values():
        return 0
    return sum(map(sum_minus_red, input.values()))
  if isinstance(input, list):
    return sum(map(sum_minus_red, input))
  if isinstance(input, int):
    return input
  return 0
  
if __name__ == "__main__":
  main()
