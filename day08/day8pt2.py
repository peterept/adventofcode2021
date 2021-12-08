#!/usr/bin/env python3

# https://adventofcode.com/2021/day/7#part2

import re

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

    # store the segments for each digit
    digits = [None for i in range(10)]

    results = []
    for row in data:
        # find 1,4,7,8
        # 1 has 2, 4 has 4, 7 has 3, and 8 has 7
        vals = {2:1, 4:4, 3:7, 7:8}
        for output in row[:10]:
            l = len(output)
            if l in vals:
                digits[vals[l]] = output
                print(output)
        print(f'found 1: {digits[1]}')
        print(f'found 4: {digits[4]}')
        print(f'found 7: {digits[7]}')
        print(f'found 8: {digits[8]}')

        # find 3
        for output in row[:10]:
            l = len(output)
            if l == 5 and len(re.findall(f'[{digits[1]}]', output)) == len(digits[1]):
                print(f'found 3: {output}')
                digits[3] = output
        # find 9
        for output in row[:10]:
            l = len(output)
            if l == 6 and len(re.findall(f'[{digits[3]}]', output)) == len(digits[3]):
                print(f'found 9: {output}')
                digits[9] = output
        # once we know 9 and 8, we can work out segment 'e' (bottom left)
        s = digits[8]
        for c in digits[9]:
            s = s.replace(c, '')
        ee_segment = s
        print(f'ee_segment: {ee_segment}') 
        # find the 3 horizontal lines aa, dd, gg
        s = digits[3]
        for c in digits[1]:
            s = s.replace(c, '')
        aa_dd_gg_segment = s
        print(f'aa_dd_gg_segments: {aa_dd_gg_segment}') 
        # find middle horizontal line dddd
        dd_segment = (re.findall(f'[{aa_dd_gg_segment}]', digits[4]))[0]  
        print(f'dd_segment: {dd_segment}') 
        # find 6
        for output in row[:10]:
            l = len(output)
            # 6  has horiz lines and ee segment
            if l == 6 and len(re.findall(f'[{aa_dd_gg_segment}]', output)) == len(aa_dd_gg_segment) and ee_segment in output:
                print(f'found 6: {output}')
                digits[6] = output
        # find 5
        digits[5] = digits[6].replace(ee_segment, '')
        print(f'found 5: {digits[5]}')
        # find 2
        for output in row[:10]:
            l = len(output)
            if l == 5 and len(re.findall(f'[{aa_dd_gg_segment}]', output)) == len(aa_dd_gg_segment) and ee_segment in output:
                print(f'found 2: {output}')
                digits[2] = output
        # find 0
        for output in row[:10]:
            l = len(output)
            if l == 6 and not dd_segment in output:
                print(f'found 0: {output}')
                digits[0] = output

        # Find OUTPUTS
        output_digits = []
        for output in row[-4:]:
            # find the matching digit
            for i in range(len(digits)):
                l = len(output)
                digit = digits[i]
                if l == len(digit) and len(re.findall(f'[{digit}]', output)) == len(digit):
                    output_digits.append(i)

        # add results
        results.append(int("".join([str(i) for i in output_digits])))

    print(results)

    print(f'sum = {sum(results)}')

if __name__ == "__main__":
    main()
