n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

max_num = max(arr)
k = len(str(max_num))

str_arr = []
for num in arr:
    str_num = str(num)

    padded_num = ""
    if len(str_num) != k:
        for _ in range(k - len(str_num)):
            padded_num += "0"
    str_arr.append(padded_num + str_num)

for pos in range(k - 1, -1, -1):
    arr_new = [[] for _ in range(10)]

    for str_num in str_arr:
        digit = int(str_num[pos])        
        arr_new[digit].append(str_num)
    
    str_arr = []
    for num_new in arr_new:
        str_arr.extend(num_new)

cleansed_res = []
# for i in range(len(str_arr)):
#         sorted_num = str_arr[i]

# print(' '.join(map(str, cleansed_res)))

for s in str_arr:
    cleansed_res.append(s)

print(' '.join(map(str, map(int, cleansed_res))))
