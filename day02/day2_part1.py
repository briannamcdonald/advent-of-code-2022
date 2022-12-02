def main():
    data = open("day02/input.txt", "r")
    data = [num for num in data]

    select_scores = []
    result_scores = []
    for line in data:
        if line[2] == "X":
            select_scores.append(1)
        elif line[2] == "Y":
            select_scores.append(2)
        elif line[2] == "Z":
            select_scores.append(3)

        if (
            (line[0] == "A" and line[2] == "X")
            or (line[0] == "B" and line[2] == "Y")
            or (line[0] == "C" and line[2] == "Z")
        ):
            result_scores.append(3)
        elif (
            (line[2] == "X" and line[0] == "C")
            or (line[2] == "Y" and line[0] == "A")
            or (line[2] == "Z" and line[0] == "B")
        ):
            result_scores.append(6)

    print(sum(select_scores) + sum(result_scores))


if __name__ == "__main__":
    main()
