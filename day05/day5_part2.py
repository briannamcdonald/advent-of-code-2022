def main():
    data = open("day05/input.txt", "r")
    data = [line for line in data]
    
    # parse stacks
    stacks = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    offset = 1
    for i in range(0, 8):
        line = data[i]
        for j in range(0, 9):
            if line[offset] != ' ':
                stacks[j].append(line[offset])
            offset += 4
        offset = 1

    # parse instructions
    instructions = []
    for i in range(10, len(data)):
        words = [word.strip("\n") for word in data[i].split(" ")]
        nums = [int(num) for num in words if num.isdigit()]
        instructions.append(nums)
    
    # take them off the top (starting at 0) multiple at a time from source and add to dest
    for i in range(len(instructions)):
        quant, source, dest = instructions[i]
        top_vals = stacks[source - 1][0:quant]
        stacks[dest - 1] = top_vals + stacks[dest - 1]
        stacks[source - 1] = stacks[source - 1][quant:]

    answer = "".join([stacks[i][0] for i in range(9)])
    print(answer)


if __name__ == "__main__":
    main()