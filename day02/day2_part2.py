def main():
    data = open("day02/input.txt", "r")
    data = [num for num in data]

    select_scores = []
    result_scores = []
    for line in data:
        # if you need to lose
        if line[2] == "X":
            if line[0] == "A":
                select_scores.append(3)
            elif line[0] == "B":
                select_scores.append(1)
            elif line[0] == "C":
                select_scores.append(2)
        # if you need to draw
        elif line[2] == "Y":
            result_scores.append(3)
            if line[0] == "A":
                select_scores.append(1)
            elif line[0] == "B":
                select_scores.append(2)
            elif line[0] == "C":
                select_scores.append(3)
        # if you need to win
        elif line[2] == "Z":
            result_scores.append(6)
            if line[0] == "A":
                select_scores.append(2)
            elif line[0] == "B":
                select_scores.append(3)
            elif line[0] == "C":
                select_scores.append(1)

    print(sum(select_scores) + sum(result_scores))


if __name__ == "__main__":
    main()
