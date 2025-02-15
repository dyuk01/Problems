n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# coin : 1
# No coin : 0
# Need to overlap 1 * 3 blocks to find max coin
# block is 3-wide, 1-tall

# output will be 0~6, where you can just return immediately at 6

# Function that checks coordinate's out of bound
def is_out_of_bound(i, j):
    return i < 0 or j < 0 or i >= n or j >= n

# Function that checks amount of coins in 1*3 block 
def check_coin(i, j):
    coin = 0
    for dj in range(3):
        new_j = j + dj
        if is_out_of_bound(i, new_j):
            return 0
        elif board[i][new_j] == 1:
            coin += 1
    
    return coin

coin1 = 0
coin2 = 0
for i in range(n):
    for j in range(n):
        if coin1 < check_coin(i,j):
            coin1 = check_coin(i,j)
            continue
        
        if coin2 < check_coin(i,j):
            coin2 = check_coin(i,j)

print(coin1 + coin2)
