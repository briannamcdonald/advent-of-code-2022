def chars_unique(string):
    unique = True
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                unique = False
    return unique


def main():
    data = open("day06/input.txt", "r")
    data = [line for line in data]

    marker = ""
    string_so_far = ""

    for line in data:
        for char in line:
            string_so_far += char
            
            if len(marker) < 14:
                marker += char
            else:
                marker = marker[1:] + char
                if chars_unique(marker):
                    print(string_so_far.rfind(marker[-1]) + 1)
                    break


if __name__ == "__main__":
    main()