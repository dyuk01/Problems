N = int(input())
arr = [int(input()) for _ in range(N)]

consec = 1
res = 0

# Iter through array and determine consecutiveness
# with the prodcut of prev and curr number.
prev_num = arr[0]
for i in range(1, len(arr)):
    curr_num = arr[i]
    if prev_num * curr_num > 0:
        consec += 1
    else:
        consec = 1
    
    
    if consec > res:
        res = consec

    prev_num = curr_num

print(res)