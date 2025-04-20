n = int(input())
seats = input()

# Please write your code here.
# occupied_seats = []
# for i in range(n):
#     if seats[i] == '1':
#         occupied_seats.append(i)

# min_distance = float('inf')

# for curr_pos in range(n):
#     # Skip
#     if seats[curr_pos] == '1':
#         continue
    
#     curr_min_distance = float('inf')
#     for seat in occupied_seats:
#         distance = abs(curr_pos - seat)
#         curr_min_distance = min(curr_min_distance, distance)
    
#     min_distance = min(min_distance, curr_min_distance)

# print(min_distance + 1)

# distances = []
# i, j = 0, 1
# while j < n:
#     if seats[j] == '0':
#         j += 1
#     else:
#         distances.append(j - i)
#         i = j
#         j += 1

# min_dist = float('inf')
# max_dist = max(distances)
# for dist in distances:
#     if dist == max_dist:
#         min_dist = min(min_dist, dist // 2)
#     else:
#         min_dist = min(min_dist, dist)

# print(min_dist)def solution() -> int:
def solution() -> int:
    occupied = []
    for idx, s in enumerate(seats):
        if s == "1":
            occupied.append(idx)

    dist = []
    for i in range(1, len(occupied)):
        dist.append(occupied[i] - occupied[i-1])

    if min(dist) == 1:
        return 1

    max_dist = -float("inf")
    for _ in range(len(dist)):
        cur_dist = dist.pop(0)
        dist.append(cur_dist // 2)
        max_dist = max(max_dist, min(dist))
        dist.pop(-1)
        dist.append(cur_dist)

    return max_dist

print(solution())
