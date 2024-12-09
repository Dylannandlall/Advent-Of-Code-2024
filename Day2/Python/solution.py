
with open("/home/dylan/Code/Advent-Of-Code/Day2/Python/input.txt", "r") as file:
    data = file.readlines()


def helper1(report: list):
    inc = 0
    dec = 0
    last = 0
    for index in report:
        number = int(index)

        if last == 0:
            last = number
            continue
        if last == number:
            return 0
        if last > number:
            if (last - 3) > number:
                return 0
            dec += 1
        if last < number:
            inc += 1
            if (last + 3) < number:
                return 0
        last = number

    if inc > 0 and dec > 0:
        return 0
    return 1

def helper2(report: list):
    def checker(arr: list):
        inc = 0
        dec = 0
        last = 0
        for i in range(len(report)):
            number = report[i]

            if last == 0:
                last = number
                continue
            if last == number:
                return [0, i]
            if last > number:
                if (last - 3) > number:
                    return [0, i]
                dec += 1
            if last < number:
                inc += 1
                if (last + 3) < number:
                    return [0, i]
            last = number

            if inc > 0 and dec > 0:
                return 0
            return [1, -1]


def part1():
    safe = 0
    for line in data:
        result = helper1(line.split(" "))
        if (result == 1):
            safe += 1

    print(safe)

def part2():
    safe = 0
    for line in data:
        if (helper2(line.split(" ")) == 1):
            safe += 1
    print(safe)



if __name__ == "__main__":
    # part1()
    part2()
