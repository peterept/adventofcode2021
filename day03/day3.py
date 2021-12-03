#!/usr/bin/env python3

# https://adventofcode.com/2021/day/3


def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data


def main():
    data = load_data('input.txt')
    # print(data)

    width = len(data[0])

    # iterate through each digits
    result_ones = ''
    result_zeros = '0'
    records = len(data)
    for i in range(0, width):
        ones = 0
        for record in data:
            if record[i] == '1':
                ones += 1
        if ones > (records/2):
            result_ones += '1'
            result_zeros += '0'
        else:
            result_ones += '0'
            result_zeros += '1'

    ones = int(result_ones, 2)
    zeros = int(result_zeros, 2)

    print(f'ones: {result_ones} = {ones}')
    print(f'zeros: {result_zeros} = {zeros}')
    print(f'Result is: {ones} * {zeros} = {ones * zeros}')

if __name__ == "__main__":
    main()
