import re

with open("Day4\Python\input.txt") as file:
    data = file.readlines()

def word_search(char_list: list) -> int:
    forward = ''.join(char_list)
    reverse = forward[::-1]

    return len(re.findall("XMAS", forward)) + len(re.findall("XMAS", reverse))

def part1():
    count = 0
    max_row = len(data[0])
    max_col = max_row

    fdiagonal = [[] for _ in range(max_row + max_col - 1)]
    bdiagonal = [[] for _ in range(len(fdiagonal))]
    min_bdiag = -max_row + 1


    for i in range(len(data)):
        horizontal = []
        vertical = []

        for j in range(len(data)):
            horizontal.append(data[i][j])
            vertical.append(data[j][i])
            fdiagonal[i+j].append(data[j][i])
            bdiagonal[i-j-min_bdiag].append(data[j][i])
        count += word_search(horizontal) + word_search(vertical)

    for i in range(len(fdiagonal)):
        count += word_search(fdiagonal[i]) + word_search(bdiagonal[i])
    print(count)

if __name__ == "__main__":
    part1()
