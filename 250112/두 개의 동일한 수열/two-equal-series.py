n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = {}
i = 0

# Iter through a and add its elements into d.
for num in a:
    if num not in d:
        d[num] = True
    i += 1

j = 0
# Iter through b and check if its value exits in d.
for num in b:
    if num not in d:
        print("No")
        break
    j += 1

if i == j:
    print("Yes")



# # Sort both arrays.
# a.sort()
# b.sort()

# # Running two pointers. i on a, j on b.
# i, j = 0, 0
# while i < n and j < n:
#     # Case 1. a[i] == b[j].
#     if a[i] == b[j]:
#         # Case 1-1. i < n.
#         if i < n:
#             i += 1

#         # Case 1-2. j < n.
#         if j < n:
#             j += 1  

#     # Case 2. a[i] != b[j].
#     else:
#         # Case 2-1. a[i] > b[j]
#         if a[i] > b[j]:
#             j += 1

#         # Case 2-2. a[i] < b[j]
#         else:
#             i += 1