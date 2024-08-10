from itertools import permutations

def main():
  with open("input.txt", "r") as file:
    contents = file.readlines()
  hap_table = {}
  guests = set()
  plus_minus = {"gain":1,"lose":-1}
  for line in contents:
    component = line.strip(".\n").split(" ")
    happiness, mood = component[3], component[2]
    happiness_change = int(happiness) * plus_minus[mood]
    hap_table.setdefault(component[0], {})[component[-1]] = happiness_change
    guests.add(component[0])
    guests.add(component[-1])
  #part 1
  optimum, _ = calc_opt_seat_arrangement(hap_table)
  print(f"The total happiness for the optimum seating arrangement is {optimum}!")
  #part 2
  for guest in guests:
    hap_table.setdefault("Me", {})[guest] = 0
    hap_table.setdefault(guest, {})["Me"] = 0
  optimum, _ = calc_opt_seat_arrangement(hap_table)
  print(f"With me added, total happiness for the optimum seating arrangement is {optimum}!")
  
def calc_opt_seat_arrangement(happiness_table: dict[str, dict[str, int]]) -> tuple[int, str]:
  most_happy = float('-inf')
  seating_arrangement = ""
  for relation in permutations(happiness_table):
    missing_link = relation[0]
    relation_comp = list(relation[1:]) + [missing_link]
    happiness_score = sum(map(lambda x, y: happiness_table[x][y], relation, relation_comp))
    happiness_score += sum(map(lambda x, y: happiness_table[y][x], relation, relation_comp))
    if happiness_score > most_happy:
      seating_arrangement = map(lambda x, y: f"{x} with {y}", relation, relation[1:])
      most_happy = happiness_score
  return most_happy, " ".join(seating_arrangement)
  
if __name__ == "__main__":
  main()
