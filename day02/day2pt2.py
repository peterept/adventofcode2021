#!/usr/bin/env python3

# https://adventofcode.com/2021/day/2

import re
from enum import Enum

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data


class CmdCode(Enum):
    forward = 0
    up = 1
    down = 2


def parser(s):
    """ Each line is in format of [cmd number]"""
    pattern = ''.join([
        "([a-z ]*)\s"  # cmd
        "([\d]*)", # numeric value
    ])
    m = re.search(pattern, s)
    if m != None:
        # print(f"Parsed: {m.group(1)}, {m.group(2)}")
        valid_cmds = list(map(lambda cmd: cmd.name, CmdCode))
        if m.group(1) in valid_cmds:
            return [CmdCode[m.group(1)], int(m.group(2))]

    raise Exception(f"invalid data: {s}")    


def main():
    data = load_data('input.txt', parser)
    #print(data)

    # [aim, horiz, depth]
    dirs = dict()
    dirs[CmdCode.forward] = [ 0, 1,  1]
    dirs[CmdCode.down] = [ 1,  0, None]
    dirs[CmdCode.up] = [ -1, 0, None]

    position = [0, 0, 0]
    for cmd in data:
        # aim
        position[0] += dirs[cmd[0]][0] * cmd[1]
        # forward horiz
        position[1] += dirs[cmd[0]][1] * cmd[1]
        # forward aim
        if dirs[cmd[0]][2]:
            position[2] += position[0] * cmd[1]

    print(position)
    print(f'final multiplied: {position[1] * position[2]}')

if __name__ == "__main__":
    main()
