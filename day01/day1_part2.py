def main():
    data = open("day01/input.txt", "r")
    data = [num for num in data]
    
    calorie_sums = []
    curr_sum = 0
    for line in data:
        if line == "\n":
            calorie_sums.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)

    print(sum(sorted(calorie_sums, reverse=True)[0:3]))

if __name__ == "__main__":
    main()