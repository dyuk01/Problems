n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def find_csc(row):
    prev_num = -1
    csc = 1
    for num in row:
        if prev_num == num:
            csc += 1
            if csc >= m:
                return True
        else:
            csc = 1
        prev_num = num
    return False

if m == 1:
    print (2 * n)
else:
    rowCount = 0 
    colCount = 0
    for row in matrix:
        if find_csc(row):
            rowCount += 1

    for col in zip(*matrix):
        if find_csc(col):
            colCount += 1

    print(rowCount + colCount)