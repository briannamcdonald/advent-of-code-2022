def main():
    data = open("day07/input.txt", "r")
    data = [line.strip() for line in data]

    path = "/"
    dirs = {"/": 0}
    for line in data:
        if line[0] == "$":
            c, cmd, *args = line.split(" ")
            if cmd == "cd":
                if args[0] != ".." and args[0] != "/":
                    # add new dir to path
                    path += "/" + args[0]
                elif args[0] != "/":
                    # remove last dir from path
                    index = path.rfind("/")
                    path = path[:index]

        else:
            size, name = line.split(" ")
            index = path.rfind("/")

            if size == "dir":
                dirs[path + "/" + name] = 0
            else:
                new_path = path
                while new_path != "":
                    dirs[new_path] += int(size)
                    index = new_path.rfind("/")
                    new_path = new_path[:index]

    unused_space = 70000000 - int(dirs["/"])
    needed_space = 30000000 - unused_space

    options = {}
    for key in dirs:
        if dirs[key] >= needed_space:
            options[key] = dirs[key]
    
    print(dirs[min(options, key=options.get)])


if __name__ == "__main__":
    main()