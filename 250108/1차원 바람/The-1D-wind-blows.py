n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r) - 1, d) for r, d in [input().split() for _ in range(q)]]

# # Change wind's direction.
# def change_dir(dir):
#     if dir == "L":
#         return "R"
#     return "L"

# # Left rotation.
# def left_rotation(row: int):
#     temp = grid[row][0]
#     for i in range(0, m - 1):
#         grid[row][i] = grid[row][i + 1]
#     grid[row][m - 1] = temp

# # Right rotation.
# def right_rotation(row: int):
#     temp = grid[row][-1]
#     for i in range(m - 1, 0, -1):
#         grid[row][i] = grid[row][i - 1]
#     grid[row][0] = temp

# # Determine rotation.
# def rotate(row: int, dir: int):
#     if dir == 'L':
#         right_rotation(row)
#     else:
#         left_rotation(row)

# # Check duplicate waves.
# def is_duplicate(row1: int, row2: int) -> bool:
#     for i in range(m):
#         if grid[row1][i] == grid[row2][i]:
#             return True
#     return False

# # Main algorithm.
# def solution(row, dir):

#     # Change current row.
#     rotate(row, dir)

#     dir = change_dir(dir)

#     # Row up.
#     upRow = row
#     while upRow - 1 >= 0:
#         if is_duplicate(upRow, upRow - 1):
#             rotate(upRow - 1, dir)
#         dir = change_dir(dir)
#         upRow -= 1 

#     # Row down.
#     downRow = row
#     while downRow + 1 < n:
#         if is_duplicate(downRow, downRow + 1):
#             rotate(downRow + 1, dir)
#         dir = change_dir(dir)
#         downRow += 1 



# for r, d in winds:
#     solution(r,d)

# for row in grid:
#     print(" ".join(map(str, row)))



def invert_dir(dir):
    return "L" if dir == "R" else "R"

# rotation, determin the dir
def rot(arr, dir):
    new_arr = []

    if dir == "L":
        new_arr = arr[1:]
        new_arr.append(arr[0])
    
    if dir == "R":
        new_arr = arr[:-1]
        new_arr.insert(0, arr[-1])
    
    return new_arr

# check duplicate
def check_dup(r1: int, r2: int) -> bool:
    for j in range(m):
        if grid[r1][j] == grid[r2][j]:
            return True
    return False


# solution
def solution(row, dir, vdir):
    inv_dir = invert_dir(dir)
    grid[row] = rot(grid[row], inv_dir)
    # print(grid[row])

    if not vdir:
        # go up
        if row - 1 >= 0 and check_dup(row, row - 1):
            solution(row - 1, inv_dir, "U")
        
        # go down
        if row + 1 < n and check_dup(row, row + 1):
            solution(row + 1, inv_dir, "D")
    
    elif vdir == "U":
        # go up
        if row - 1 >= 0 and check_dup(row, row - 1):
            solution(row - 1, inv_dir, "U")

    elif vdir == "D":
        # go down
        if row + 1 < n and check_dup(row, row + 1):
            solution(row + 1, inv_dir, "D")


for r, d in winds:
    solution(r,d, "")

for row in grid:
    print(" ".join(map(str, row)))