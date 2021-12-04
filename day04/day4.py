#!/usr/bin/env python3

# https://adventofcode.com/2021/day/4


def mark_number(number, board):
    # if the number is found, change it to 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == number:
                board[r][c] = -1

def check_winner(board):
    # winner row
    for row in board:
        if row.count(-1) == len(row):
            return True
    # winner column
    for c in range(len(board)):
        col = []
        for r in range(len(board)):
            col.append(board[r][c])
        if col.count(-1) == len(col):
            return True
    return False


def play_bingo_game(numbers, boards):
    for number in numbers:
        for board in boards:
            mark_number(number, board)
            if check_winner(board):
                return board, number
    return None,None

def main():
    with open('input.txt') as my_file:
        lines = my_file.readlines()

    # read numbers
    numbers = [int(n) for n in lines[0].split(',')]
    print(numbers)


    # read boards
    boards = []
    board = None
    lines.append('')
    for i in range(1, len(lines)):
        if lines[i].strip() == '':
            if board:
                boards.append(board)
            # start a new bingo board next
            board = []
        else:
            row = [int(n) for n in lines[i].split()]
            board.append(row)

    winning_board, number = play_bingo_game(numbers, boards)

    print(boards)
    print(winning_board)

    sum = 0
    if winning_board:
        for r in range(len(winning_board)):
            for c in range(len(winning_board[r])):
                num = winning_board[r][c]
                if num != -1:
                    sum += num

        print(f'sum = {sum} * number {number} = {sum * number}')

if __name__ == "__main__":
    main()
