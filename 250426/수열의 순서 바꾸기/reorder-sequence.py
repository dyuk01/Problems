n = int(input())
seq = list(map(int, input().split()))

# Please write your code here.

# Type of insertion sort -> sort in non-decreasing order

# Pick a number at beginning

sorted_tail = 1

for i in range(n - 2, -1, -1):
    if seq[i] < seq[i + 1]:
        sorted_tail += 1
    else:
        break

print(n - sorted_tail)



