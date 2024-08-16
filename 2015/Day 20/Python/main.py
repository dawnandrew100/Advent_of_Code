from functools import reduce

def main():
  input = 33100000
  i, solution = 0, 0
  while solution < input:
    i += 1
    factors = part_one_factors(i)
    solution = sum(factors)    
  print(f"House number {i:,} was the first to get at least {input:,} presents!")

  i, solution = 0, 0
  while solution < input:
    i += 1
    factors = part_two_factors(i)
    solution = sum(factors)
  print(f"After some consideration, house number {i:,} was the first to get at least {input:,} presents!")

def part_one_factors(n: int) -> set[int]:    
  return set(reduce(list.__add__, 
              ([i* 10, (n//i)*10] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def part_two_factors(n: int) -> list[int]:    
  pre_50 = set(reduce(list.__add__,
    ([i, (n//i)] for i in range(1, int(n**0.5) + 1) if (n % i == 0))))
  return [i*11 for i in pre_50 if (i*50 >= n)]
if __name__ == "__main__":
  main()
