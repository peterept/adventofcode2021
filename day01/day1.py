#!/usr/bin/env python3

# https://adventofcode.com/2021/day/1


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


def main():
    data = load_data('input.txt', parser)
    # print(data)

    increases = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            increases += 1

    print(f'Increments found: {increases}')

if __name__ == "__main__":
    main()
