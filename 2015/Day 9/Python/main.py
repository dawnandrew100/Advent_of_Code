from collections import defaultdict
def main():
  with open("input.txt", "r") as file:
    contents = file.read().split("\n")
  routes = {}
  sorted_routes = {}
  for content in contents:
    component = content.split(" = ")
    routes[component[0]] = int(component[1])
  sorted_routes = dict(sorted(routes.items(), key=lambda item: item[1]))
  options = [route.split(" to ") for route in sorted_routes]

  total = []
  for one in options:
    for two in one:
      total.append(two)
  total = set(total)

  final = []
  destination_count = defaultdict(int)
  for option in options:
    repeat = False
    if final and (destination_count[final[0][0]] == 2 or destination_count[final[0][1]] == 2):
      for opt in option:
        if (opt == final[0][0] or opt == final[0][1]) and len(final) != len(total)-1:
          repeat = True
      if repeat:
        continue
    if destination_count[option[0]] >= 2 or destination_count[option[1]] >= 2:
      continue
    destination_count[option[0]] += 1
    destination_count[option[1]] += 1
    if option not in final:
      final.append(option)
      
  print(final)
  total = 0
  for place in final:
    flight = " to ".join(place)
    total += routes[flight]
  print(total)

if __name__ == "__main__":
  main()
