def main():
    data = open("day03/input.txt", "r")
    data = [num for num in data]

    chars = []
    priorities = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    for line in data:
        comp1 = line[0 : len(line) / 2]
        comp2 = line[len(line) / 2 :]
        char_set = set()
        for char in comp1:
            if char in comp2:
                char_set.add(char)
        chars.append(list(char_set)[0])

    total = 0
    for char in chars:
        total += priorities.index(char) + 1

    print(total)


if __name__ == "__main__":
    main()
