n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# coin : 1
# No coin : 0
# Need to overlap 1 * 3 blocks to find max coin
# block is 3-wide, 1-tall

# output will be 0~6, where you can just return immediately at 6

def get_coin(i,j):
    coin = 0
    for dj in range(3):
        new_j = j + dj
        if board[i][new_j] == 1:
            coin += 1
    return coin

# Find the first block with the most coin
max_coin1 = 0
coin1_i, coin1_j = 0, 0
for i in range(n):
    for j in range(n - 2):
        if max_coin1 < get_coin(i,j):
            max_coin1 = get_coin(i,j)
            coin1_i, coin1_j = i, j

# Then, find the second block with the most coin
max_coin2 = 0
for i in range(n):
    for j in range(n - 2):
        if coin1_i == i and coin1_j <= j <= coin1_j + 2 :
            continue
        
        max_coin2 = max(max_coin2, get_coin(i,j))


print(max_coin1 + max_coin2)