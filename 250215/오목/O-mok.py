n = 19
board = [list(map(int, input().split())) for _ in range(n)]

def is_in_bound(i, j):
    return 0 <= i < n and 0 <= j < n

def iterate(i, j):
    directions = {
        'right': (0,1),
        'down_right': (1,1),
        'down' : (1,0),
        'down_left': (1,-1),
    }

    for (direction, (di, dj)) in directions.items():
        new_i = i 
        new_j = j
        consec = 0
        for _ in range(5):
            # print(board[i][j], new_i, new_j)   
            if is_in_bound(new_i, new_j) and board[i][j] == board[new_i][new_j]:
                consec += 1
            else:
                break

            new_i += di
            new_j += dj
               
        if consec == 5:
            return direction
    return 'not_found'

def solution():
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                direction = iterate(i, j)
                if direction == 'not_found':
                    continue
                
                if direction == 'right':
                    return board[i][j], i, j + 2
                elif direction == 'down_right':
                    return board[i][j], i + 2, j + 2
                elif direction == 'down':
                    return board[i][j], i + 2, j
                elif direction == 'down_left':
                    return board[i][j], i + 2, j - 2
    return 0, -1, -1



rock, i, j = solution()

print(rock)
if rock != 0:
    print(i + 1, j + 1)
    