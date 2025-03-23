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

def check_dist(d: int) -> bool:
    i = 0
    cnt = 0
    last_seat = -d # This is to allow when 0th index is a possible seat.
    while i < n and cnt < NUM_PEOPLE:
        if seats[i] == "0":
            # Check with existing 1s.
            valid = True
            if min([abs(p - i) for p in pos]) < d:
                valid = False
                
            # Check with newly added 1s.
            if valid and i - last_seat >= d:
                cnt += 1
                last_seat = i
        
        i += 1
                
    return cnt == NUM_PEOPLE

# Utilize binary search to maximize the possible minimum distance between 1s.
def solution() -> int:
    lo, hi = 0, n
    result = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if check_dist(mid):
            result = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    return result

print(solution())

