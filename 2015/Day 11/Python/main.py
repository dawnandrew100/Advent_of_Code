def main():
  password = 'hepxcrrq'
  part_one_pw = find_next_pw(password)
  part_two_pw = find_next_pw(part_one_pw)
  print(f"The first valid password for Santa is '{part_one_pw}' "
        f"and the second valid password for Santra is '{part_two_pw}'!")

def find_next_pw(input: str) -> str:
  output = input
  while True:
    if output[-1] == "z":
      output = z_propagate(output)
    output = output[:-1] + next_char(output[-1])
    if len(output) > 4 and not no_banned_letters(output[:-4]):
      output = rectify(output)
    if no_banned_letters(output) and straight_of_three(output) and double_double(output):
      return output

def next_char(input: str) -> str:
  return chr((((ord(input)+1) - 97) % 26) + 97)

def z_propagate(input: str) -> str:
  output = input
  pre_change = "z"
  for n in range(-2, -(len(output)+1), -1):
    if pre_change != 'z':
      break
    pre_change = output[n]
    output = output[:n] + next_char(output[n]) + output[n+1:]
  if output[0] == 'a' and pre_change == 'z':
    output = 'a' + output
  return output

def rectify(input: str) -> str:
  output = input
  banned = ["i","o","l"]
  for letter in banned:
    if letter in output:
      chosen_one = output.index(letter)
      diff = len(output) - len(output[:chosen_one]) - 1
      output = list(output[:chosen_one]) + [next_char(output[chosen_one])] +(["a"]*diff)
  return "".join(output)

def straight_of_three(input: str) -> bool:
  for i in range(len(input)-2):
    if input[i+1] == chr(ord(input[i])+1) and input[i+2] == chr(ord(input[i+1])+1):
      return True
  return False

def double_double(input: str) -> bool:
  prev_letter = ""
  double_count = 0
  for letter in input:
    if letter == prev_letter:
      double_count += 1
      prev_letter = ""
      if double_count == 2:
        return True
      continue
    prev_letter = letter
  return False

def no_banned_letters(input: str) -> bool:
  if "i" in input or "o" in input or "l" in input:
    return False
  return True

if __name__ == "__main__":
  main()
