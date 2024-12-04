
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

def helper2(report: list, depth):
    inc = 0
    dec = 0
    last = 0

    if depth > 1:
        return 0

    for i in range(len(report)):
        number = int(report[i])

        if last == 0:
            last = number
            continue
        if last == number:
            report_copy = report.copy()
            report_copy.pop(i)
            if helper2(report_copy, depth+1) == 1:
                continue
            else:
                return 0
        if last > number:
            dec += 1
            if (last - 3) > number:
                report_copy = report.copy()
                report_copy.pop(i)
                if helper2(report_copy, depth+1) == 1:
                    continue
                else:
                    return 0
        if last < number:
            inc += 1
            if (last + 3) < number:
                report_copy = report.copy()
                report_copy.pop(i)
                if helper2(report_copy, depth+1) == 1:
                    continue
                else:
                    return 0
        last = number

    if inc > 0 and dec > 0:
        return 0   
    return 1


def part1():
    safe = 0
    for line in data:
        if (helper1(line.split(" ")) == 1):
            safe += 1
    print(safe)

def part2():
    safe = 0
    for line in data:
        if (helper2(line.split(" "), 0) == 1):
            safe += 1
    print(safe)
            



if __name__ == "__main__":
    part1()
    # part2()