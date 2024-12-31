n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Finds the maximum amount of coin in a 3 x 3 square
def total_coin(r, c):
    max_coin = 0
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            max_coin += matrix[i][j]
    
    return max_coin

# Finds the maximum coin out of the given matrix
res = 0

for i in range(n - 2):
    for j in range(n - 2):
        mCoin = total_coin(i,j)
        if mCoin > res:
            res = mCoin

print(res)