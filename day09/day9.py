#!/usr/bin/env python3

# https://adventofcode.com/2021/day/9


def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data


def parser(s) -> int:
    return [int(n) for n in list(s.strip())]


def is_lowest(data, x, y):
    dirs = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]
    val = data[y][x]
    # print(f'{x},{y} = {val}')
    for d in dirs:
        dv = data[y+d[1]][x+d[0]]
        if dv != 10 and dv <= val:
            return False            

    return True

def main():
    data = load_data('input.txt', parser)
    border = 10
    data.insert(0, [border for n in range(len(data[0]))])
    data.append([border for n in range(len(data[0]))])
    for n in range(len(data)):
        data[n] = [border, *data[n], border]
    # print(data)

    lowest = []
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):
            if is_lowest(data, x, y):
                if data[y][x] == 9:
                    print(f'9 found at {x},{y}')
                    print(f' {data[y-1][x]}\n{data[y][x-1]}{data[y][x]}{data[y][x+1]}\n {data[y+1][x]}')
                lowest.append(data[y][x])
    print(lowest)

    risk = sum([n+1 for n in lowest])
    print(f'Risk = {risk}')


if __name__ == "__main__":
    main()
