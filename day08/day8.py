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


def parser(s) -> [str]:
    return s.split()


def main():
    data = load_data('input.txt', parser)
    # print(data)

    # 1 has 2, 4 has 4, 7 has 3, and 8 has 7
    vals = {1:2, 4:4, 7:3, 8:7}

    count = 0
    for row in data:
        print(row[-4:])        
        for output in row[-4:]:
            if len(output) in vals.values():
                count += 1
                print(output)

    print(count)


if __name__ == "__main__":
    main()
