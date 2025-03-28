# Check for consecutive duplicate numbers in a row
def check_row(matrix, m, row, c1, n):
    dupNum = 0
    prevNum = -1
    for col in range(c1, n):
        num = matrix[row][col]
        if prevNum == num:
            dupNum += 1
        else:
            dupNum = 1
        prevNum = num
        if dupNum >= m:
            return True
    return False
    
# Check for consecutive duplicate numbers in a column
def check_col(matrix, m, col, r1, n):
    dupNum = 0
    prevNum = -1
    for row in range(r1, n):
        num = matrix[row][col]
        if prevNum == num:
            dupNum += 1
        else:
            dupNum = 1
        prevNum = num
        if dupNum >= m:
            return True
    return False


# Initialize
n, m = map(int, input().split())
matrix = []
happy_array = 0

# Matrix Input
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Happy Array
for i in range(n):
    if check_row(matrix, m, i, 0, n):
        happy_array += 1
    if check_col(matrix, m, i, 0, n):
        happy_array += 1

print(happy_array)