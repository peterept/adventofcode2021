#!/usr/bin/env python3

# https://adventofcode.com/2021/day/6#part2


def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data


def parser(s) -> int:
    return [int(n) for n in s.split(',')]


def main():
    data = load_data('input.txt', parser)
    # print(data)
    fishes = data[0]
   # fishes = [3,4,3,1,2]
#    print(fishes)

    # count how many of particular types and we can group them
    fishes_count_per_timer = [fishes.count(n) for n in range(10)]

    days = 256
    for day in range(days):
        if fishes_count_per_timer[0] > 0:
            fishes_count_per_timer[9] = fishes_count_per_timer[0]
            fishes_count_per_timer[7] += fishes_count_per_timer[0]

        # move all the fish to the left
        fishes_count_per_timer = fishes_count_per_timer[1:]
        fishes_count_per_timer.append(0)
        # print(fishes_count_per_timer)

        print(f'Number of fishes after {day+1} days: {sum(fishes_count_per_timer)}')

if __name__ == "__main__":
    main()
