n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def get_coin(i, j):
    coin = 0
    for dj in range(3):
        new_j = j + dj
        if board[i][new_j] == 1:
            coin += 1
    
    return coin

# Get first block's max coin
max_coin1 = 0
coin1_i, coin1_j = 0, 0
for i in range(n):
    for j in range(n - 2):
        if max_coin1 < get_coin(i, j):
            max_coin1 = get_coin(i, j)
            coin1_i, coin1_j = i, j

# Get second block's max coin
max_coin2 = 0
for i in range(n):
    for j in range(n - 2):
        if i == coin1_i and coin1_j - 2 <= j <= coin1_j + 2:
            continue
        max_coin2 = max(max_coin2, get_coin(i, j))

print(max_coin1 + max_coin2)