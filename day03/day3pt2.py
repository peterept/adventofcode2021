#!/usr/bin/env python3

# https://adventofcode.com/2021/day/3#part2


def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line.strip())
    return data


def main():
    data = load_data('input.txt')
    #print(data)

    width = len(data[0])
    print(width)

    # oxygen

    # iterate through each digits
    results = data
    for i in range(0, width):
        ones = 0
        results_ones = []
        results_zeros = []
        print('here')
        for record in results:
            if record[i] == '1':
                ones += 1
                results_ones.append(record)
            else:
                results_zeros.append(record)

        if ones >=  (len(results)/2):
            results = results_ones 
        else:
            results = results_zeros 

        if len(results) == 1:
            break

    oxygen = int('0' + results[0], 2)

    # co2

    # iterate through each digits
    results = data
    for i in range(0, width):
        ones = 0
        results_ones = []
        results_zeros = []
        for record in results:
            if record[i] == '1':
                ones += 1
                results_ones.append(record)
            else:
                results_zeros.append(record)

        if ones < (len(results)/2):
            results = results_ones 
        else:
            results = results_zeros 

        if len(results) == 1:
            break

    co2 = int('0' + results[0], 2)

    print(f'{oxygen} * {co2} = {oxygen * co2}')


if __name__ == "__main__":
    main()
