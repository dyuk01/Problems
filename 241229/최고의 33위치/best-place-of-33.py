def get_coin(matrix, r1, c1, r2, c2):
    goldNum = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            goldNum += matrix[r][c]
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
for row in range(n - 2):
    for col in range(n - 2):
        max_money = max(max_money, get_coin(matrix,row,col,row+2, col+2)) 


print (max_money)
