def get_coin(matrix, row, col):
    goldNum = 0
    for r in range(row + 3):
        for c in range(col + 3):
            if matrix[r][c] == 1:
                goldNum += 1
    return goldNum

# Initialize
n = int(input())
matrix = []
money = 0
max_money = 0

# Input
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Naive approach
for r in range(n - 2):
    for c in range(n - 2):
        money = get_coin(matrix, r, c)
        max_money = max(money, max_money)

print (max_money)
