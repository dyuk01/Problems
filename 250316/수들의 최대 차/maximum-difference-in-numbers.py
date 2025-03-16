# n, k = map(int, input().split())
# arr = [int(input()) for _ in range(n)]

# arr.sort()

# arr_min = []
# arr_max = []
# for a in arr:
#     arr_min.append(a)
#     arr_max.append(a)

# # Please write your code here.
# def remove_min(s):
#     diff = max(s) - min(s)

#     while diff > k:
#         s.pop(0)
#         diff = max(s) - min(s)

#     return len(s)


# def remove_max(s):
#     diff = max(s) - min(s)

#     while diff > k:
#         s.pop(-1)
#         diff = max(s) - min(s)

#     return len(s)

# res_min = remove_min(arr_min)
# res_max = remove_max(arr_max)

# print(max(res_min, res_max))

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

def solution() -> int:
    best_len = -float("inf")
    for l in range(n - 1):
        for r in range(l + 1, n):
            if arr[r] - arr[l] <= k:
                best_len = max(best_len, r - l + 1)
    return best_len

print(solution())