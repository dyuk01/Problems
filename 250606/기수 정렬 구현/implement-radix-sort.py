# n = int(input())
# arr = list(map(int, input().split()))

# # Please write your code here.

# max_num = max(arr)
# k = len(str(max_num))

# str_arr = []
# for num in arr:
#     str_num = str(num)

#     padded_num = ""
#     if len(str_num) != k:
#         for _ in range(k - len(str_num)):
#             padded_num += "0"
#     str_arr.append(padded_num + str_num)

# for pos in range(k - 1, -1, -1):
#     arr_new = [[] for _ in range(10)]

#     for str_num in str_arr:
#         digit = int(str_num[pos])        
#         arr_new[digit].append(str_num)
    
#     str_arr = []
#     for num_new in arr_new:
#         str_arr.extend(num_new)

# cleansed_res = []

# for s in str_arr:
#     cleansed_res.append(s)

# print(' '.join(map(str, map(int, cleansed_res))))

from typing import List, Dict

n = int(input())
arr = list(map(int, input().split()))

def pad_nums(n: int, digit: int) -> str:
    return str(n).zfill(digit)
    # return f"{n:0{digit}d}"
    # x = ""
    # for _ in range(digit - len(str(n))):
    #     n += "0"
    # return x + str(n)
    

def flatten(radix: Dict[int, List[str]]) -> List[str]:
    temp = []
    for i in range(10):
        temp.extend(radix[i])
    return temp

def radix_sort() -> List[str]:
    k = len(str(max(arr)))
    pad_arr = [pad_nums(num, k) for num in arr]

    for pos in range(k - 1, -1, -1):
        radix = {i: [] for i in range(10)}
        for num in pad_arr:
            radix[int(num[pos])].append(num)
        pad_arr = flatten(radix)

    return pad_arr

def solution() -> str:
    return " ".join(map(str, list(map(int, radix_sort()))))

print(solution())
