def main():
    data = open("day04/input.txt", "r")
    data = [line.strip() for line in data]
    
    count = 0
    for line in data:
        range1, range2 = line.split(",")
        r1x, r1y = [int(x) for x in range1.split("-")]
        r2x, r2y = [int(x) for x in range2.split("-")]

        if (r1x <= r2x and r2y <= r1y) or (r2x <= r1x and r1y <= r2y):
            count += 1

    print(count)


if __name__ == "__main__":
    main()