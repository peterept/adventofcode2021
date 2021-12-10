#!/usr/bin/env python3

# https://adventofcode.com/2021/day/10


def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data


def parser(s) -> int:
    return s.strip()

def is_corrupt(row):
    op = ['<','[','{','(']
    cl = ['>',']','}',')']

    q = []
    for c in row:
        if len(q) == 0:
            if c in cl:
                # invalid end
                return c
            q.append(c)
        else:
            if c in cl:
                if q[-1] == op[cl.index(c)]:
                    del q[-1:] # pop
                else:
                    # corrupt bc close not matching start
                    return c
            else:
                q.append(c)
    print(q)
    return None



def main():
    data = load_data('input.txt', parser)
   # print(data)

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
        }


    count = 0
    for row in data:
      #  print(row)
        illegal = is_corrupt(row)
        if illegal:
            print(f'Corrupt: {row}')
            count += points[illegal]
    print(count)

if __name__ == "__main__":
    main()
