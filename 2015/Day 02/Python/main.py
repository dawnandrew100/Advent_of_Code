def main():
  gifts: list[list[str]] = []
  with open("..\\input.txt", "r") as file:
    for line in file:
      gifts.append(line.strip().split("x"))

  total_paper = wrapping_paper_size(gifts)
  total_ribbon = ribbon_size(gifts)
  print(f"Paper needed: {total_paper:,} sqft\nRibbon needed: {total_ribbon:,} ft")


def wrapping_paper_size(contents: list[list[str]])->int:
  total_surface_area = 0
  for dimension in contents:
    dimension = [int(x) for x in dimension]
    length, width, height = dimension[0], dimension[1], dimension[2]

    surface_area1, surface_area2, surface_area3 = length*width, width*height, height*length
    extra = min(surface_area1, surface_area2, surface_area3)
    
    total_surface_area += (2*surface_area1)+(2*surface_area2)+(2*surface_area3)+extra
  return total_surface_area

def ribbon_size(contents: list[list[str]])->int:
  total_feet = 0
  for dimension in contents:
    dimension = [int(x) for x in dimension]
    length, width, height = dimension[0], dimension[1], dimension[2]
    dimension = sorted(dimension)
    short_side_1, short_side_2 = dimension[0], dimension[1]

    bow = length*width*height
    ribbon = (2*short_side_1)+(2*short_side_2)
    total_feet += (ribbon+bow)
  return total_feet


if __name__ == "__main__":
  main()
