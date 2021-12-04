#!/usr/bin/env python3

# https://adventofcode.com/2021/day/4#part2


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
    winners = []
    for number in numbers:
        for b in range(len(boards)):
            if not check_winner(boards[b]):
                mark_number(number, boards[b])
                if check_winner(boards[b]):
                # record the winning board 
                    winners.append(b)
                    print(f'Winner: {b} with number {number}')
        if len(winners) == len(boards):
            break

    # return the last winning board, and number picked
    return boards[winners[-1]],number

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

    last_winning_board, number = play_bingo_game(numbers, boards)

    # print(boards)
    print(last_winning_board)

    sum = 0
    if last_winning_board:
        for r in range(len(last_winning_board)):
            for c in range(len(last_winning_board[r])):
                num = last_winning_board[r][c]
                if num != -1:
                    sum += num

        print(f'sum = {sum} * number {number} = {sum * number}')

if __name__ == "__main__":
    main()
