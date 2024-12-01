

def part1():
    with open("input.txt", "r") as f:
        data = f.readlines()

    total_distance = 0
    llist = []
    rlist = []

    for line in data:
        tokens = line.split()
        llist.append((tokens[0]))
        rlist.append((tokens[1]))

    llist.sort()
    rlist.sort()

    for i in range(len(llist)):
        total_distance += abs(int(llist[i]) - int(rlist[i]))
    
    print(total_distance)

def part2():
    with open("input.txt", "r") as f:
        data = f.readlines()

    similarity = 0
    left = []
    right = []

    for line in data:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    for i in range(len(left)):
        count = right.count(left[i])
        if count > 0:
            similarity += left[i] * count
            right.remove(left[i])
    
    print(similarity)



if __name__ == "__main__":
    part1()
    part2()