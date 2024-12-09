from itertools import combinations, combinations_with_replacement

with open("Day7\Python\input.txt", 'r') as file:
    data = file.readlines()


def part1():
    for i in range(len(data)):
        target = data[i].split(":")[0]
        numbers = data[i].strip().split(":")[1].split(" ")[1:]
        num_of_operators = len(numbers) - 1
        combinations = combinations_with_replacement([0, 1], num_of_operators)

        current_combinations = list(combinations)
        for combo in current_combinations:
            left = int(numbers[0])
            for operators in combo:
                right = int(numbers[i+1])

                if combo[i] == 0:
                    left = left + right
                if combo[i] == 1:
                    left = left * right

            if left == target:
                print(target)
        # for combo in list(current_combinations):
        #     left = int(numbers[0])
        #     for i in range(len(combo)):
        #         right = int(numbers[i+1])

        #         if combo[i] == 0:
        #             left = left + right
        #         if combo[i] == 1:
        #             left = left * right

        #     if left == target:
        #         print(target)

if __name__ == "__main__":
    part1()
