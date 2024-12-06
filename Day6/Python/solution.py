with open("Day6\Python\input.txt") as file:
    map = []
    for line in file:
        tmp = []
        for char in line:
            tmp.append(char)
        map.append(tmp)

origin = [0, 0]
obstacles = []
MAX_ROWS = 0
MAX_COLS = len(map[0])
for i in range(len(map)):
    for j in range(len(map)):
        if map[i][j] == "^":
            origin = [i, j]
        if map[i][j] == "#":
            obstacles.append([i,j])
    MAX_ROWS += 1

def part1():
    direction = 0 # 0 = North, 1 = East, 2 = South, 3 = West
    current = origin
    positions = []
    positions.append(current)

    while True:
        match direction:
            case 0:
                current[0] -= 1
                if [current[0]-1, current[1]] in obstacles:
                    direction = 1
            case 1:
                current[1] += 1
                if [current[0], current[1]+1] in obstacles:
                    direction = 2
            case 2:
                current[0] += 1
                if [current[0]+1, current[1]] in obstacles:
                    direction = 3
            case 3:
                current[1] -= 1
                if [current[0], current[1]-1] in obstacles:
                    direction = 0

        if current[0] < 0 or current[0] > MAX_ROWS - 1 or current[1] < 0 or current[1] > MAX_COLS - 1:
            break

        positions.append([current[0], current[1]])

    result = len(list(set(tuple(x) for x in positions)))
    ### Bruh what
    print(result - 1)




if __name__ == "__main__":
    part1()
