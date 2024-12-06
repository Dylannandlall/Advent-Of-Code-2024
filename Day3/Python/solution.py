import re

with open("Day3\Python\input.txt", "r") as file:
    data = file.read()

def part1():
    sum_of_products = 0
    pattern = re.compile("mul\((\d+),(\d+)\)")
    tokens = pattern.findall(str(data))

    for multi in tokens:
        x, y = multi
        sum_of_products += (int(x) * int(y))

    print(sum_of_products)

def part2():
    sum_of_products = 0
    puzzle = data

    while True:
        start = puzzle.find("don't()")
        stop = puzzle.find("do()", start)

        if start > -1 and stop == -1:
            puzzle = puzzle[0:start]
            break
        else:
            puzzle = puzzle[0:start] + puzzle[stop:-1]

    sum_of_products = 0
    pattern = re.compile("mul\((\d+),(\d+)\)")
    tokens = pattern.findall(str(puzzle))

    for multi in tokens:
        x, y = multi
        sum_of_products += (int(x) * int(y))
    print(sum_of_products)


if __name__ == "__main__":
    # part1()
    part2()
