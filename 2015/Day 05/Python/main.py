from collections import defaultdict
import re

def main():
  with open("..\\input.txt", "r") as file:
    contents = file.read().split('\n')
  print(f"There are {nice_part_one(contents)} nice words matching part one's rule set!")
  print(f"There are {nice_part_two(contents)} nice words matching part two's rule set!")

def nice_part_one(word_list: list[str]) -> int:
  nice_word_count = 0
  for word in word_list:
    if pass_rule_set_one(word):
      nice_word_count += 1
  return nice_word_count

def pass_rule_set_one(seq: str) -> bool:
  bad_combo_dict = {"b":"a", "d":"c", "q":"p","y":"x"}
  vowel_count = 0
  double_letter, naughty_word = False, False
  prev_letter = ""
  for letter in seq:
    if letter in bad_combo_dict and prev_letter == bad_combo_dict[letter]:
        naughty_word = True
        break
    if prev_letter == letter:
      double_letter = True
    prev_letter = letter
    if letter in ["a","e","i","o","u"]:
      vowel_count += 1
  return vowel_count >= 3 and double_letter and not naughty_word

def nice_part_two(word_list: list[str]) -> int:
  nice_word_count = 0
  for word in word_list:
    if double_rainbow(word) and space_between(word):
      nice_word_count += 1
  return nice_word_count

def double_rainbow(seq: str) -> bool:
  count = 2
  charactermatches: dict[str, int] = defaultdict(int)
  for start in range(0, len(seq)):
    end = start+count
    if end > len(seq):
      break
    key: str = seq[start:end]
    charactermatches[key] += 1
  if any(v >= 2 for v in charactermatches.values()):
    double = [x for x in charactermatches if charactermatches[x]>=2]
    for key in double:
      if len(re.findall(key, seq)) >= 2:
        return True
  return False

def space_between(seq: str) -> bool:
  for i, letter in enumerate(seq):
    if seq.count(letter) >= 2 and i <= len(seq)-3 and seq[i+2] == letter:
      return True
  return False

if __name__ == "__main__":
  main()
