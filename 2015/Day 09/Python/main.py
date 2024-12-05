from itertools import permutations

def main():
    with open("..\\input.txt", "r") as file:
        contents = file.read().split("\n")
    locations = set()
    routes = {}
    for content in contents:
        (source, _, destination, _, distance) = content.split()
        distance = int(distance)
        locations.add(source)
        locations.add(destination)
        routes.setdefault(source, dict())[destination]= distance
        routes.setdefault(destination, dict())[source]= distance

    shortest_dist, longest_dist = float('inf'), float('-inf')
    shortest_path, longest_path = "", ""
    for places in permutations(routes):
        dist = sum(map(lambda x, y: routes[x][y], places, places[1:]))
        if dist < shortest_dist:
            shortest_path = map(lambda x, y: f"{x} -> {y}", places, places[1:])
            shortest_dist = dist
        if dist > longest_dist:
            longest_path = map(lambda x, y: f"{x} -> {y}", places, places[1:])
            longest_dist = dist
    shortest_path = ' | '.join([str(x) for x in shortest_path])
    longest_path = ' | '.join([str(x) for x in longest_path])

    if shortest_path and longest_path:
        print(f"The shortest path is {shortest_path} that covers {shortest_dist} miles!\n")
        print(f"The longest path is {longest_path} that covers {longest_dist} miles!\n")

if __name__ == "__main__":
  main()
