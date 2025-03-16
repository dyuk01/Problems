n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr_min = []
for a in arr:
    arr_min.append(a)

arr_max = []
for a in arr:
    arr_max.append(a)

# Please write your code here.
def remove_min(s):
    diff = max(s) - min(s)

    while diff > k:
        s.pop(s.index(min(s)))
        diff = max(s) - min(s)

    return len(s)


def remove_max(s):
    diff = max(s) - min(s)

    while diff > k:
        s.pop(s.index(max(s)))
        diff = max(s) - min(s)

    return len(s)

res_min = remove_min(arr_min)
res_max = remove_max(arr_max)

print(max(res_min, res_max))
   
