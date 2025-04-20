n = int(input())
arr = list(input().split())

# Please write your code here.
# sorted_arr = []
# for ch in arr:
#     sorted_arr.append(ord(ch))

# sorted_arr.sort()

# max_moves = -1
# for i in range(n):
#     max_moves = max(max_moves, abs(ord(arr[i]) - sorted_arr[i]))

# print(max_moves)

swap_count = 0

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap_count += 1

print(swap_count)