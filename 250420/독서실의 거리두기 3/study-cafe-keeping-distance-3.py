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

distances = []
i, j = 0, 1
while j < n:
    if seats[j] == '0':
        j += 1
    else:
        if j - i - 1 != 0:
            distances.append(j - i - 1)
        i = j
        j += 1


print(distances)
min_dist = float('inf')
for dist in distances:
    min_dist = min(min_dist, dist)

if min_dist == '1' or min_dist % 2 == 0:
    print(min_dist)
else:
    print(min_dist // 2)
# 10001001001
# 3 2 2

# 110001001000101
# 3 2 3 1
# pos = 0,1,5,8,12,14
# dist = 

    