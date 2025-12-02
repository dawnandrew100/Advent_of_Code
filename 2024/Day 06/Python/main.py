def main():
    with open("..\\test.txt") as file:
        input = []
        for line in file.readlines():
            input.append(list(line.strip()))

    print(input)

if __name__ == "__main__":
    main()
