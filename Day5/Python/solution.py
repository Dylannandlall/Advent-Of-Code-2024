with open("Day5\Python\input.txt", "r") as file:
    data = file.read()

rules = {}
for line in data.split("\n\n")[0].split("\n"):
    x, y = line.split("|")
    if x in rules.keys():
        rules[x].append(int(y))
    else:
        rules[x] = [int(y)]

update = []
for line in data.split("\n\n")[1].split("\n")[:-1]:
    update.append([int(n) for n in line.split(",")])

def part1():
    middle_numbers = 0
    for line in update:
        order = True
        for index, number in enumerate(line):
            before = str(number)
            if before in rules.keys():
                afterList = rules[before]

                for num in afterList:
                    try:
                        i = line.index(num)
                        if index > i:
                            order = False
                    except ValueError:
                        continue

        if order == True:
            middle_numbers += line[len(line) // 2]

    print(middle_numbers)

def part2():
    pass


if __name__ == "__main__":
    # part1()
    part2()
