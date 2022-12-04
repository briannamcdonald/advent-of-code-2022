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

    char_set = set()
    list_of_groups = zip(*(iter(data),) * 3)
    for group in list_of_groups:
        for char in group[0]:
            if char in group[1] and char in group[2] and char != "\n":
                char_set.add(char)
                continue
        chars.append(list(char_set)[0])
        char_set = set()

    total = 0
    for char in chars:
        total += priorities.index(char) + 1

    print(total)


if __name__ == "__main__":
    main()
