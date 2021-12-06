#!/usr/bin/env python3

# https://adventofcode.com/2021/day/6


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
#    fishes = [3,4,3,1,2]
#    print(fishes)

    days = 80
    for day in range(days):
        new_fishes = []
        temp = []
        for fish in fishes:
            fish -= 1
            if fish == -1:
                fish = 6
                new_fishes.append(8)
            temp.append(fish)
        fishes = temp + new_fishes       

        print(f'After  {day+1} day: {fishes}')

        print(f'Number of fishes after {day+1} days: {len(fishes)}')

if __name__ == "__main__":
    main()
