n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

# # Please write your code here.
# max_score = -1
# for index in range(1, 4):
#     cups = [0] * 4
#     cups[0] = -1
#     cups[index] = 1
#     score = 0
#     for a,b,c in moves:
#         cups[a], cups[b] = cups[b], cups[a]
#         score += cups[c]
    
#     max_score = max(max_score, score)

# print(max_score)

cup_map = {
    1: 1,
    2: 2,
    3: 3,
}

point_map = {
    1: 0,
    2: 0,
    3: 0,
}

for a, b, c in moves:
    cup_map[a], cup_map[b] = cup_map[b], cup_map[a]
    point_map[cup_map[c]] += 1
print(max(point_map.values()))