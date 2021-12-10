#!/usr/bin/env python3

# https://adventofcode.com/2021/day/10#part2


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
    return None

def get_remainder(row):
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
    return q


def main():
    data = load_data('input.txt', parser)
   # print(data)

    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
        }

    row_scores = []
    for row in data:
      #  print(row)
        row_score = 0
        illegal = is_corrupt(row)
        if not illegal:
            seq = get_remainder(row)
            print(seq)
            while len(seq):
                c = seq[-1]
                row_score *= 5
                row_score += points[c]
                del seq[-1:] # pop
            print(f'score = {row_score}')
            # insert sorted
            i = 0
            for i in range(len(row_scores)):
                if row_scores[i] > row_score:
                    break
            row_scores.insert(i, row_score)

    print(row_scores)
    print(row_scores[len(row_scores)//2])

if __name__ == "__main__":
    main()
