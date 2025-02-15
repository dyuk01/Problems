n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

def is_out_of_bound(i):
    return i < 0 or i >= n

max_sum = 0
for i in range(n):
    curr_sum = 0
    for di in range(k):
        if is_out_of_bound(di):
            break
        curr_sum += numbers[di]
    
    if max_sum < curr_sum:
        max_sum = curr_sum

print(max_sum)