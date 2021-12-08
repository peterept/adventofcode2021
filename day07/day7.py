#!/usr/bin/env python3

# https://adventofcode.com/2021/day/7


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

def calc_fuel(data, i):
    fuel = 0
    for pos in data:
        f = abs(i-pos)
        print(f'Move from {pos} to {i}: {f} fuel')
        fuel += f
    return fuel

def main():
    data = load_data('input.txt', parser)
    #print(data)
    crabs = data[0]
    #crabs = [16,1,2,0,4,2,7,1,2,14]

    # try each position
    fuel = 0
    fuel_i = 0

    for i in range(max(crabs)):
        temp_fuel = calc_fuel(crabs, i)
        print(f'Total fuel: {temp_fuel}')
        if fuel == 0 or temp_fuel < fuel:
            fuel = temp_fuel 
            fuel_i = i

    print(f'move to position {fuel_i} uses fuel {fuel}')

if __name__ == "__main__":
    main()
