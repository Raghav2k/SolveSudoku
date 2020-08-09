

# Check if it is valid to put a value in the board
def valid(row, col, val, grid):

    columns = []
    for i in range(0, len(grid)):
        columns.append(grid[i][col])

    x_sub = int(row/3) * 3
    y_sub = int(col/3) * 3

    sub_grid = True

    if val in grid[row]:
        sub_grid = False

    elif val in columns:
        sub_grid = False

    else:
        for i in range(x_sub, x_sub+3):
            for j in range(y_sub, y_sub+3):
                if grid[i][j] == val:
                    sub_grid = False

    return sub_grid


# Solves the grid
def solve(grid):

    board_is_full = True

    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == 0:
                board_is_full = False

    completed = board_is_full

    if completed:
        return True

    else:

        for i in range(0, len(grid)):
            for j in range(0, len(grid)):

                if grid[i][j] == 0:

                    nums = 1
                    can_place = True

                    while nums <= 9:
                        can_place = valid(i, j, nums, grid)
                        if can_place:
                            grid[i][j] = nums

                            if solve(grid):
                                return True

                            grid[i][j] = 0

                        nums = nums + 1

                    return False


# Creates the board
def create_grid(grid):

    solve(grid)
    divider = ['-------------------------------------------------------']

    for i in range(0, len(grid)):
        if i != 0:

            print('\n')

            if i == 3 or i == 6:
                print(divider[0])

        for j in range(0, len(grid)):

            if j == 2 or j == 5 or j == 8:
                print(grid[i][j], '  |  ', end='')
            else:
                print(grid[i][j], '    ', end='')

    print('\n')

board = [

    [0, 0, 0, 0, 4, 9, 1, 0, 0],
    [5, 0, 4, 6, 0, 0, 0, 0, 0],
    [6, 0, 9, 0, 8, 0, 0, 3, 0],
    [9, 2, 0, 0, 0, 6, 0, 0, 3],
    [0, 0, 5, 2, 3, 7, 9, 0, 0],
    [8, 3, 0, 5, 0, 0, 0, 7, 2],
    [0, 0, 0, 0, 0, 0, 3, 1, 9],
    [0, 4, 3, 0, 0, 0, 7, 5, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0]

                                ]

print('Sudoku Solver', '\n')

create_grid(board)
