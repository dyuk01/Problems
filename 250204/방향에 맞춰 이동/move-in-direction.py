n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Write your code here!
x, y = 0, 0
for i in range(n):
    if dir[i] == "E": 
        x += 1 * dist[i]
    elif dir[i] == "W":
        x -= 1 * dist[i]
    elif dir[i] == "N":
        y += 1 * dist[i]
    else:
        y -= 1 * dist[i]

print(x, y)
