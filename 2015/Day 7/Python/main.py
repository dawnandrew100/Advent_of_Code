def main():
  with open("input.txt", "r") as file:
    contents = file.read().split("\n")
  #part one
  registers = {}
  final_results = {}
  for line in contents:
    from_to = line.split(" -> ")
    registers[from_to[1]] = from_to[0].split(" ")
  solution1 = solve("a", registers, final_results)
  #part two
  final_results = {}
  registers["b"] = [solution1]
  solution2 = solve("a", registers, final_results)
  print(f"The value stored in 'a' is initially {solution1}."
        " Changing the 'b' register value from 44430 to 3176 gives the 'a' register a value of {solution2}.")

def solve(register: str|int, register_dict: dict[str, list[str]], results: dict[str, int]) -> int:
  try:
    return int(register)
  except ValueError:
    pass

  if register not in results:
    tokens = register_dict[register]
    if len(tokens) == 1:
      res = solve(tokens[0], register_dict, results)
    else:
      operand = tokens[-2]
      match operand:
        case "NOT":
          res = ~solve(tokens[1], register_dict, results) & 0xffff
        case "AND":
          res = solve(tokens[0], register_dict, results) & solve(tokens[2], register_dict, results)
        case "OR":
          res = solve(tokens[0], register_dict, results) | solve(tokens[2], register_dict, results)
        case "RSHIFT":
          res = solve(tokens[0], register_dict, results) >> int(tokens[2])
        case "LSHIFT":
          res = solve(tokens[0], register_dict, results) << int(tokens[2])
    results[register] = res
  return results[register]

if __name__ == "__main__":
  main()
