#!/usr/bin/env python3

# https://adventofcode.com/2021/day/1#part2

from typing import Optional

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data


def parser(s) -> int:
    return int(s)


def get_window_measurment(data: [int], i: int, size: int) -> Optional[int]:
    if i >= 0 and i+size <= len(data):
        return sum([data[i] for i in range(i,i+size)])


def main():
    data = load_data('input.txt', parser)
    # print(data)

    window_size = 3
    increases = 0
    for i in range(0, len(data)):
        first = get_window_measurment(data, i-1, window_size)
        second = get_window_measurment(data, i, window_size)
        # print(f"first: {first} second: {second}")
        if first and second and second > first:
            increases += 1
            # print("increases")

    print(f'Increments found: {increases}')

if __name__ == "__main__":
    main()
