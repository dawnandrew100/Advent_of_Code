input_nums = '3113322113'

def look_and_say(input: str, count: int) -> str:
  if count == 0:
    return input
  previous: str = "-1"
  num_count: int = 0
  output: list[str] = []
  for num in input:
    if num != previous and previous != "-1":
        output.extend([str(num_count), previous])
        previous = num
        num_count = 1
        continue
    previous = num
    num_count += 1
  output.extend([str(num_count), previous])
  return look_and_say("".join(output), count-1)

part1 = look_and_say(input_nums, 40)
part2 = look_and_say(input_nums, 50)
print(f"The length of the output for part 1 is {len(part1)}.\n"
      f"The length of the output for part 2 is {len(part2)}.")
