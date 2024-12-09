def main():
    with open("..\\input.txt") as file:
      inputs = []
      for line in file.readlines():
        inputs.append(line.strip())

if __name__ == "__main__":
    main()
