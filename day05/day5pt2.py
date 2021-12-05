#!/usr/bin/env python3

# https://adventofcode.com/2021/day/5#part2

import re

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data


def parser(s) -> [dict]:
    pattern = ''.join([
        "([\d]*),([\d]*)"  # x1,y1
        "\s->\s"           # ->
        "([\d]*),([\d]*)"  # x2,y2
    ])
    m = re.search(pattern, s)
    if m != None:
       return {'s': s, 'x1': int(m.group(1)), 'y1': int(m.group(2)), 'x2': int(m.group(3)), 'y2': int(m.group(4))}

def get_max_x(lines): 
    x = 0
    for line in lines:
        print(line)
        if line['x1'] > x:
            x = line['x1']
        if line['x2']> x:
            x = line['x2']
    return x


def get_max_y(lines): 
    y = 0
    for line in lines:
        if line['y1'] > y:
            y = line['y1']
        if line['y2'] > y:
            y = line['y2']
    return y

def bres(line):
    # Setup initial conditions
    x1 = line['x1']
    y1 = line['y1']
    x2 = line['x2'] 
    y2 = line['y2']
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points
    # if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1    

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else(x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    if swapped:
        points.reverse()
    #print(points)
    return points


def draw_line(grid, points):
    for point in points:
        x,y = point
        grid[y][x] += 1
    pass

def main():

    lines = load_data('input.txt', parser)
    print(lines)

    width = get_max_x(lines) + 1
    height = get_max_y(lines) + 1
    print(f'width={width} height={height}')

    # create 2D grid
    grid = [[0 for x in range(0, width)] for y in range(0, height)]    

    # draw each line
    for line in lines:
        # only straight lines OR diagnonal
        if line['x1'] == line['x2'] or line['y1'] == line['y2'] or abs(line['y2'] - line['y1']) == abs(line['x2'] - line['x1']):
            points = bres(line)
            draw_line(grid, points)

    # print grid
    for row in grid:
        print(row)

    # count all points > 1
    overlap_count = 0
    for row in grid:
        for col in row:
            if col > 1:
                overlap_count += 1

    print(f'result = {overlap_count}')


if __name__ == "__main__":
    main()
