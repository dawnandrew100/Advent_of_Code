from itertools import permutations

def main():
    with open("..\\input.txt") as file:
      inputs = []
      for line in file.readlines():
        inputs.append(line.strip())

    rules = {}
    updates = []
    for input in inputs:
      if "|" in input:
        before, after = input.split("|")
        rules.setdefault(after, []).append(before) #list of chapters required to be before key value chapter
      else:
        updates.append(input.split(","))

    valid, invalid = [], []
    for item in range(1, len(updates)):
        if is_valid_order(rules, updates[item]):
            valid.append(updates[item])
            continue
        invalid.append(updates[item])

    print(f"The sum of middle page numbers from correctly sorted updates is {sum(map(find_middle, valid))}!")

    corrected = rule_swap_sort(rules, invalid)
    print(f"The sum of middle page numbers from incorrectly sorted (later sorted) "
          f"updates is {sum(map(find_middle, corrected))}!")

    """
    #DO NOT USE THIS UNLESS YOU HAVE DAYS TO RUN THIS OR HAVE A GOD TIER LAPTOP
    #THERE ARE UP TO 25! OPTIONS FOR ONE INPUT, LET ALONE THE ~200 IN THE MAIN INPUT
    #test input takes 0.001 to 0.000001 seconds to sort
    #main input takes _________ seconds to sort
    corrected = perumutation_sort(rules, invalid)
    print(f"The sum of middle page numbers from incorrectly sorted (later sorted) "
          f"updates is {sum(map(find_middle, corrected))}!")
    """

def is_valid_order(rule_dict: dict[str, list[str]], chapters: list[str] | tuple[str, ...]) -> bool:
    for i, page in enumerate(chapters):
        if any(invalid in rule_dict.get(page, []) for invalid in chapters[i:]):
            return False
    return True

def find_middle(valid_chaps: list[str]) -> int:
    return int(valid_chaps[len(valid_chaps)//2])

#Who needs efficiency when we have time on our side
def perumutation_sort(rule_dict: dict[str, list[str]], invalid_chaps:list[list[str]]) -> list[str]:
    corrected_order = []
    for items in invalid_chaps:
        for chapters in permutations(items):
            if is_valid_order(rule_dict, chapters):
                corrected_order.append(chapters)
                break
    return corrected_order

def rule_swap_sort(rule_dict: dict[str, list[str]], invalid_chaps:list[list[str]]) -> list[str]:
    sorted_chaps = []
    for items in invalid_chaps:
        is_sorted = False
        while not is_sorted:
            updated_items = items[:]
            for i, chap in enumerate(items):
                if any([invalid in rule_dict.get(chap, []) for invalid in items[i:]]):
                    options = [word for word in items if word in rule_dict.get(chap, [])]
                    for option in options:
                        if items.index(option) > i:
                            updated_items[i], updated_items[items.index(option)] = updated_items[items.index(option)], updated_items[i]
                    items = updated_items
                    break
            if is_valid_order(rule_dict, items):
                sorted_chaps.append(items)
                is_sorted = True
    return sorted_chaps

if __name__ == "__main__":
    main()
