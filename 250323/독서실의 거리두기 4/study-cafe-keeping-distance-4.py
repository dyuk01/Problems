# n = int(input())
# seats = input()

# # Please write your code here.
# occupied = []

# for i in range(n):
#     if seats[i] == '1':
#         occupied.append(i)

# max_min_dist = 0

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if seats[i] == '0' and seats[j] == '0':
#             temp_occupied = occupied + [i] + [j]
#             temp_occupied.sort()

#             min_dist = float('inf')
#             for k in range(1, len(temp_occupied)):
#                 dist = temp_occupied[k] - temp_occupied[k - 1]
#                 min_dist = min(min_dist, dist)
            
#             max_min_dist = max(max_min_dist, min_dist)

# print(max_min_dist)

n = int(input())
seats = input()
NUM_PEOPLE = 2

pos = [i for i, o in enumerate(seats) if o == "1"]
default_min_dist = n
for i in range(1, len(pos)):
    default_min_dist = min(default_min_dist, pos[i] - pos[i-1])

# def get_min_both(i: int) -> int:
#     # Left min dist.
#     left_dist = float("inf")
#     right_dist = float("inf")
#     for j in range(i - 1, -1, -1):
#         if seats[j] == "1":
#             left_dist = i - j
#             break
#     for j in range(i + 1, n):
#         if seats[j] == "1":
#             left_dist = j - i
#             break

#     return min(left_dist, right_dist)

def check_dist(d: int) -> bool:
    i = 0
    cnt = 0
    last_seat = -d # This is to allow when 0th index is a possible seat.
    while i < n and cnt < NUM_PEOPLE:
        if seats[i] == "0":
            # Check with existing 1s.
            valid = True
            if min([abs(p - i) for p in pos] + [default_min_dist]) < d:
                valid = False
                
            # Check with newly added 1s.
            if valid and i - last_seat >= d:
                cnt += 1
                last_seat = i
        
        i += 1
                
    return cnt == NUM_PEOPLE

# Utilize binary search to maximize the possible minimum distance between 1s.
def solution() -> int:
    lo, hi = 1, n
    result = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid > default_min_dist or not check_dist(mid):
            hi = mid - 1
        else:
            result = mid
            lo = mid + 1
    return result

print(solution())

