import re
from collections import defaultdict
def main():
  with open("input.txt", "r") as file:
    contents = file.readlines()

  deer_contestants = {}
  for line in contents:
    match = re.findall(r"\d+", line)
    deer = line.split(" ")[0]
    deer_contestants[deer] = [int(x) for x in match]
    
  race_time = 2503
  print(part_one(deer_contestants, race_time))
  points_winner, all_points = part_two(deer_contestants, race_time)
  print(f"{points_winner} got the most points with {max(all_points.values())} points!")

def part_two(contestants: dict[str, list[int]], time: int) -> tuple[str, dict[str, int]]:
  points = defaultdict(int)
  deer_dist = defaultdict(int)
  most_points, furthest_dist = "", 0
  for i in range(1, time+1):
    for reindeer in contestants:
      speed = contestants[reindeer][0]
      duration = contestants[reindeer][1]
      rest = contestants[reindeer][2]
      time_per_dist = duration + rest
      max_dist = speed * duration
      
      dist = i//time_per_dist * max_dist
      if i%time_per_dist < duration:
        dist += (i%time_per_dist) * speed
      if i%time_per_dist >= duration:
        dist = (i//time_per_dist+1)* max_dist
      if dist > furthest_dist:
        furthest_dist = dist
      deer_dist[reindeer] = dist   
    for deer in deer_dist:
      if deer_dist[deer] == furthest_dist:
        points[deer] += 1
        
  for deer in points:
    if max(points.values()) == points[deer]:
      most_points = deer
  return most_points, dict(points)
      

def part_one(contestants: dict[str, list[int]], time: int) -> str:
  furthest, furthest_dist = "", 0
  for reindeer in contestants:
    speed = contestants[reindeer][0]
    duration = contestants[reindeer][1]
    rest = contestants[reindeer][2]

    time_per_dist = duration + rest
    max_dist = speed * duration
    full_cycles = time//time_per_dist
    extra = time%time_per_dist
    if extra > duration:
      total_dist = (full_cycles * max_dist) + max_dist
    else:
      total_dist = (full_cycles * max_dist) + (speed * extra)
    if total_dist > furthest_dist:
      furthest = reindeer
      furthest_dist = total_dist
  return f"{furthest} went the furthest at {furthest_dist}km!"
  
if __name__ == "__main__":
  main()
