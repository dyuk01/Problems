n = int(input())
arr = list(input().split())


# swap_count = 0

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             swap_count += 1

# print(swap_count)

def cnt_inversions(a):
    if len(a) <= 1:
        return a, 0
    
    mid = len(a) // 2
    l, inv_l = cnt_inversions(a[:mid])
    r, inv_r = cnt_inversions(a[mid:])
    result, inv = merge(l, r)
    return result, inv + inv_l + inv_r

def merge(l, r):
    result = []
    i, j, inv = 0, 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
            inv += len(l) - i
    result += l[i:] + r[j:]
    return result, inv

def solution() -> int:
    _, inv = cnt_inversions(arr)
    return inv

print(solution())