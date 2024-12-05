def main():
    with open("..\\input.txt") as file:
      data = file.readlines()

    stack_of_reports = []
    for line in data:
      stack_of_reports.append(list(map(int, line.strip().split(" "))))

    part_one = 0
    for report in stack_of_reports:
      if is_safe_report(report):
        part_one += 1

    part_two = 0
    for report in stack_of_reports:
      if is_safe_report(report, True):
        part_two += 1

    print(f"There were initially {part_one} safe reports! "
          f"After we turned on the 'Problem Dampener', there were {part_two} safe reports!")

def is_safe_report(input: list[int], dampen_active: bool = False, faults: int = 0) -> bool:
  temp_input = input[:] #creates copy of list rather than reference to list
  #handles edge-case of 0th element not matching rest of sequence
  prev_up_down = "ascending" if temp_input[2] > temp_input[1] else "descending"
  if faults > 1: #Base case for recursions
    return False
  for i in range(1, len(temp_input)):
    new_up_down = "ascending" if temp_input[i] > temp_input[i-1] else "descending"
    if new_up_down != prev_up_down:
      if dampen_active:
        faults += 1
        poss_faulty_value_1, poss_faulty_value_2 = temp_input[:], temp_input[:]
        poss_faulty_value_1.pop(i) #two pops test whether current or previous element is problem child
        poss_faulty_value_2.pop(i-1) #turns into new input without problem child element
        return is_safe_report(poss_faulty_value_1, dampen_active, faults) or is_safe_report(poss_faulty_value_2, dampen_active, faults)
      return False #numbers switched directions
    prev_up_down = new_up_down
    if abs(temp_input[i]-temp_input[i-1]) > 3 or abs(temp_input[i]-temp_input[i-1]) == 0:
      if dampen_active:
        faults += 1
        poss_faulty_value_1, poss_faulty_value_2 = temp_input[:], temp_input[:]
        poss_faulty_value_1.pop(i)
        poss_faulty_value_2.pop(i-1)
        return is_safe_report(poss_faulty_value_1, dampen_active, faults) or is_safe_report(poss_faulty_value_2, dampen_active, faults)
      return False #repeated number or jump of 4 or more
  return True #no problem child elements

if __name__ == "__main__":
    main()
