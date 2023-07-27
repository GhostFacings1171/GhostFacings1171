import random

def create_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-1)
        if board[row][col] != 'X':
            board[row][col] = 'X'
            mines_placed += 1
    return board

def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(max(0, row-1), min(row+2, len(board))):
        for j in range(max(0, col-1), min(col+2, len(board[0]))):
            if board[i][j] == 'X':
                count += 1
    return count

def reveal_cell(board, row, col, visited):
    if board[row][col] == 'X' or visited[row][col]:
        return
    visited[row][col] = True
    num_mines = count_adjacent_mines(board, row, col)
    if num_mines > 0:
        board[row][col] = str(num_mines)
    else:
        board[row][col] = ' '
        for i in range(max(0, row-1), min(row+2, len(board))):
            for j in range(max(0, col-1), min(col+2, len(board[0]))):
                reveal_cell(board, i, j, visited)

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * (4 * len(row) - 3))

def play_game():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    num_mines = int(input("Enter number of mines: "))

    board = create_board(rows, cols, num_mines)
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    while True:
        print_board(board)
        row = int(input("Enter row number (0 to {}): ".format(rows-1)))
        col = int(input("Enter column number (0 to {}): ".format(cols-1)))

        if board[row][col] == 'X':
            print("Game Over!")
            break

        reveal_cell(board, row, col, visited)

        if all(all(visited[row][col] or board[row][col] == 'X' for col in range(cols)) for row in range(rows)):
            print("Congratulations! You won!")
            break

play_game()
