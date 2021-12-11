#!/usr/bin/env python3

# https://adventofcode.com/2021/day/11#part2


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


def flash(data, r, c):
    dirs = [
        [-1, -1],
        [ 0, -1],
        [ 1, -1],        
        [ 1,  0],
        [ 1,  1],
        [ 0,  1],        
        [-1,  1],        
        [-1,  0],        
    ]
    flashed = False
    for d in dirs:
        dr = r+d[1]
        dc = c+d[0]
        if dc >= 0 and dc < len(data[r]) and dr >= 0 and dr < len(data) and data[dr][dc] <= 9:
            data[dr][dc] += 1
            flashed = True
    return flashed


def step(data):
    # step 1: increment all
    for r in range(len(data)):
        for c  in range(len(data[r])):
            data[r][c] += 1
    # step 2: handle flashes
    flashed = True
    flash_count = 0
    # repeat for all again until none flash
    while flashed:
        flashed = False
        for r in range(len(data)):
            for c  in range(len(data[r])):
                if data[r][c] == 10:
                    flash(data, r, c)
                    data[r][c] += 1 # mark as already flashed
                    flashed = True
                    flash_count += 1
    # step 3: reset flashed
    for r in range(len(data)):
        for c  in range(len(data[r])):
            if data[r][c] > 9:
                data[r][c] = 0
    return flash_count



def main():
    data = load_data('input.txt', parser)
    print(data)

    flash_count = 0

    for i in range(10000000):
        flash_count += step(data)
        print(f'pass {i+1}')
        print(data)

        # did this flash all?
        l = []        
        for r in data:
            l += r
        if len(set(l)) == 1:
            print(f'**** FLASH ****')
            return

    print(f'flashes {flash_count}')


if __name__ == "__main__":
    main()
