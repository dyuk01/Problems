# T, a, b = map(int, input().split())
# c = []
# x = []
# for _ in range(T):
#     char, pos = input().split()
#     c.append(char)
#     x.append(int(pos))

# Please write your code here.
#  d1(k to S) <= d2(k to N)  --> Special distance
#       d1 = abs(S - k)
#       d2 = abs(N - k)
#  d1(k to S) > d2(k to N) --> Not Special distance
#  x = a ~ b


# def find_min_s(k):
#     min_dist = float('inf')
#     for key, value in dimension.items():
#         if value == 'S':
#             min_dist = min(min_dist, abs(key - k))
    
#     return min_dist


# def find_min_n(k):
#     min_dist = float('inf')
#     for key, value in dimension.items():
#         if value == 'N':
#             min_dist = min(min_dist, abs(key - k))
    
#     return min_dist


# # Find special distance
# def is_special_dist(k):
#     return find_min_s(k) <= find_min_n(k)


# dimension = {}
# for letter, dist in zip(c, x):
#     dimension[dist] = letter 
# res = 0

# # Iterate through a and b
# for d in range(a, b + 1):
#     if is_special_dist(d):
#         res += 1

# print(res)

# dimension = {}
# for letter, dist in zip(c, x):
#     dimension[dist] = letter 

# sorted_dimension = sorted(dimension.items(), key=lambda x: x[0])
# keys = list(sorted_dimension.keys())

# index = a
# l,r = a,a
# special_distances = []
# while (l <= b):
#     key = keys[l]
#     value = sorted_dimension[key]

#     if index <= l and value == 'N':
#         continue
    
#     if l < index:
#         while not keys[l]:
#             l += 1


#     special_distances.append[index]
#     index += 1

T, a, b = map(int, input().split())
line = [""] * (1000)
for _ in range(T):
    char, pos = input().split()
    line[int(pos) - 1] = char

max_val = float("inf")

def is_in_bound(idx: int) -> bool:
    return 0 <= idx and idx < 1000

def get_dist(idx: int, d1: int, d2: int, dis: int, dir: int) -> (int, int):
    new_pos = idx + dir * dis
    if is_in_bound(new_pos):
        char = line[new_pos]
        if char == "S" and d1 == max_val:
            d1 = dir * (new_pos - idx)
        elif char == "N" and d2 == max_val:
            d2 = dir * (new_pos - idx)
    return d1, d2

def find_nearest(idx: int) -> (int, int):
    d1, d2 = max_val, max_val
    dis = 0
    while d1 == max_val or d2 == max_val:
        d1, d2 = get_dist(idx, d1, d2, dis, 1)
        d1, d2 = get_dist(idx, d1, d2, dis, -1)
        dis += 1
    
    return d1, d2

def solution():
    cnt = 0
    for i in range(a - 1, b):
        d1, d2 = find_nearest(i)
        if d1 <= d2:
            cnt += 1
    return cnt

print(solution())

    
