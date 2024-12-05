import re

with open("input.txt", "r") as file:
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
        stop = puzzle.find("do()", start) + 3

        if (start == -1) or (stop == -1):
            break

        else:
            # puzzle = puzzle[:start] + puzzle[stop:]
            print(puzzle[start:stop])
            break

    print(data)


if __name__ == "__main__":
    # part1()
    part2()