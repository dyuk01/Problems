n = int(input())
seats = input()

# Please write your code here.
# occupied = []
# for idx, s in enumerate(seats): 
#     if s == '1':
#         occupied.append(idx)

# max_min_dist = -1

# for i in range(len(occupied) - 2):
#     l = occupied[i]
#     r = occupied[i + 1]

#     if r - l > 1:
#         mid = (l + r) // 2
    
#     min_dist = mid - l
#     max_min_dist = max(max_min_dist, min_dist)


# if occupied[0] > 0:
#     min_dist = occupied[0]
#     max_min_dist = max(max_min_dist, min_dist)

# if occupied[-1] < n - 1:
#     min_dist = n - 1 - occupied[-1]
#     max_min_dist = max(max_min_dist, min_dist)

# print(max_min_dist)



def solution() -> int:
    occupied = [i for i, s in enumerate(seats) if s == "1"]
    
    max_dist = -float('inf')
    for i in range(n):
        if seats[i] == 1:
            continue
        
        test = occupied + [i]
        test.sort()
        min_dist = min(test[j + 1] - test[j] for j in range(len(test) - 1))
        max_dist = max(max_dist, min_dist)

    return max_dist

print(solution())
