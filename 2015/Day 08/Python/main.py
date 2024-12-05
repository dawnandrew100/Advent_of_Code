def main():
  with open("..\\input.txt", "r") as file:
    contents = file.read().split("\n")
  solution_1 = sum([len(content)-len(eval(content)) for content in contents])
  solution_2 = 0
  for content in contents:
    content_plus = content.replace('\\','\\\\').replace('"','\\\"')
    content_plus = f'\"{content_plus}\"'
    solution_2 += len(content_plus) - len(content)
  print(f"The difference using part one's rules is {solution_1} "
        f"and the difference using part two's rules is {solution_2}!")

if __name__ == "__main__":
  main()
