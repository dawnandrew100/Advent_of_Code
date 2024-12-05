def main():
    with open("..\\input.txt") as file:
      word_search_grid = []
      for line in file.readlines():
        word_search_grid.append(list(line.strip()))
      word_search_grid = word_search_grid

    xmas = xmas_finder(word_search_grid)
    x_mas = x_mas_finder(word_search_grid)
    print(f"First we mistakenly found {xmas} xmases, but then we correctly found {x_mas} x_masses!")

def is_in_bounds(xlen: int, ylen: int, i, j) -> bool:
  return  0 <= i < xlen and 0 <= j < ylen

def xmas_finder(input_grid: list[list[str]]) -> int:
    count = 0
    ilen, jlen = len(input_grid), len(input_grid[0])
    for i, _ in enumerate(input_grid):
        for j, _ in enumerate(input_grid):
            if input_grid[i][j] == "X":
                for di in [-1, 0, 1]: #di and dj search + and x
                    for dj in [-1, 0, 1]:
                        if (di, dj) == (0, 0):
                            continue
                        if is_in_bounds(ilen, jlen, i+3*di, j+3*dj):
                            if ''.join(input_grid[i+k*di][j+k*dj] for k in range(4)) == 'XMAS':
                                count += 1
    return count

def x_mas_finder(input_grid: list[list[str]]) -> int:
    count = 0
    ilen, jlen = len(input_grid), len(input_grid[0])
    for i, _ in enumerate(input_grid):
        for j, _ in enumerate(input_grid):
            if i == 0 or j == 0:
                continue #handles A in first row or column
            if input_grid[i][j] == "A":
                temp = 0
                for di in [-1, 1]:  #di, dj search diagonally only
                    for dj in [-1, 1]:
                        if (di, dj) == (1, 1) or (di, dj) == (1, -1):
                            continue
                        if is_in_bounds(ilen, jlen, i+1, j+1): #handles A in last row or column
                            poss_match = ''.join(input_grid[i+k*di][j+k*dj] for k in range(-1,2))
                            if poss_match == 'MAS' or poss_match == 'SAM': #-1 in range makes 'A' middle
                                temp += 1
                                if temp-2 == 0:
                                    count += 1
    return count

if __name__ == "__main__":
    main()
