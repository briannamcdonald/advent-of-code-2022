def main():
    data = open("day07/input.txt", "r")
    data = [line.strip() for line in data]

    path = "/"
    dirs = {"/": 0}

    for line in data:
        if line.startswith("$ cd"):
            arg = line.split(" ")[2]
            
            if arg != ".." and arg != "/":
                path += "/" + arg  # add new dir to path
            elif arg != "/":
                index = path.rfind("/")
                path = path[:index]  # remove last dir from path

        elif line.startswith("$ ls"): continue
        else:
            size, name = line.split(" ")

            if size == "dir":
                dirs[path + "/" + name] = 0
            else:
                new_path = path
                while new_path != "":
                    dirs[new_path] += int(size)
                    index = new_path.rfind("/")
                    new_path = new_path[:index]

    needed_space = 30000000 - (70000000 - int(dirs["/"]))
    options = {}
    for key in dirs:
        if dirs[key] >= needed_space:
            options[key] = dirs[key]
    
    print(dirs[min(options, key=options.get)])


if __name__ == "__main__":
    main()