n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r) - 1, d) for r, d in [input().split() for _ in range(q)]]

# Change wind's direction.
def change_dir(dir):
    if dir == "L":
        return "R"
    return "L"

# Left rotation.
def left_rotation(row: int):
    temp = grid[row][0]
    for i in range(0, m - 1):
        grid[row][i] = grid[row][i + 1]
    grid[row][m - 1] = temp

# Right rotation.
def right_rotation(row: int):
    temp = grid[row][-1]
    for i in range(m - 1, 0, -1):
        grid[row][i] = grid[row][i - 1]
    grid[row][0] = temp

# Determine rotation.
def rotate(row: int, dir: int):
    if dir == 'L':
        right_rotation(row)
    else:
        left_rotation(row)

# Check duplicate waves.
def is_duplicate(row1: int, row2: int) -> bool:
    for j in range(m):
        if grid[row1][j] == grid[row2][j]:
            return True
    return False

# Main algorithm.
def solution(row, dir):

    # Change current row.
    rotate(row, dir)
    
    # Row up.
    upDir = change_dir(dir)
    upRow = row
    while upRow - 1 >= 0 and is_duplicate(upRow, upRow - 1):
        rotate(upRow - 1, upDir)
        upDir = change_dir(upDir)
        upRow -= 1 

    # Row down.
    downDir = change_dir(dir)
    downRow = row
    while downRow + 1 < n and is_duplicate(downRow, downRow + 1):
        rotate(downRow + 1, downDir)
        downDir = change_dir(downDir)
        downRow += 1 

for r, d in winds:
    solution(r,d)

for row in grid:
    print(" ".join(map(str, row)))
