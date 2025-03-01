n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
scores = {i: 0 for i in range(1,4)}

for a,b,c in moves:
    if c == 3:
        continue
    elif c == 1:
        scores[b] += 1
    elif c == 2:
        scores[a] += 1

max_key = max(scores, key=scores.get)
print(scores[max_key])
