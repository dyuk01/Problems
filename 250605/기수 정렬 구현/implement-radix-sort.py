n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

max_num = max(arr)
k = len(str(max_num))

for pos in range(k - 1, -1, -1):
    arr_new = [[] for _ in range(10)]

    for num in arr:
        digit = (num // (10 ** pos)) % 10
        arr_new[digit].append(num)
    
        res = []
        for num_new in arr_new:
            res.append(num_new)

cleaned_res = []
for i in range(len(res)):
    for j in range(len(res[i])):
        sorted_num = res[i][j]
        if sorted_num is not None:
            cleaned_res.append(sorted_num)

print(' '.join(map(str, cleaned_res)))