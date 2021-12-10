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

def find_basin(data, x, y):
    print(f' {x},{y} = {data[y][x]}')
    if data[y][x] == 9:
        return 0
    dirs = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]
    count = 1
    data[y][x] = 9
    for d in dirs:
        sx = x+d[0]
        sy = y+d[1]
        if sx >= 0 and sx < len(data[y]) and sy >= 0 and sy < len(data):
            # mark this one as done
            dv = data[sy][sx]
            count += find_basin(data, sx, sy)
    return count


def main():
    data = load_data('input.txt', parser)
    # border = 10
    # data.insert(0, [border for n in range(len(data[0]))])
    # data.append([border for n in range(len(data[0]))])
    # for n in range(len(data)):
    #     data[n] = [border, *data[n], border]
    # print(data)

    # use dfs to find 
    basins = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            basin_size = find_basin(data, x, y)
            if basin_size > 0:
                # insert size sorted
                if len(basins) == 0:
                    basins.append(basin_size)
                else:
                    for i in range(len(basins)):
                        if basin_size >= basins[i]:
                            basins.insert(i, basin_size)
                            break
#                basins.append(basin_size)
    print(basins)
    print(basins[:3])

    prod = 1
    for n in basins[:3]:
        prod = prod * n

    print(prod)



if __name__ == "__main__":
    main()
