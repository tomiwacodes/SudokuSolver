
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def find_empty_space(myBoard):
    for row in range(0, 8):
        for col in range(0, 8):
            if(myBoard[row][col] == 0):
                return row, col

    return None, None

def check_guess_validity(myBoard, guess, row, column):
    column_vals = []
    for row_val in myBoard[row]:
        if guess == row_val:
            return False
    for i in range(len(myBoard)):
        column_vals += myBoard[i][column]
    if guess in column_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (column // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if myBoard[r][c] == guess:
                return False

    return True

def actually_solve(myBoard):
    row, col = find_empty_space(myBoard)
    guess = 1
    if row==None:
        return True

    if check_guess_validity(myBoard, guess, row, col):
        myBoard[row][col] = guess
        if actually_solve(myBoard):
            return True
        else:
            guess += 1
            return False
    myBoard[row][col] = 0


print(actually_solve(board))
