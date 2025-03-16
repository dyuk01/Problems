n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_val = []

def find_path(pos, curr_max):
    curr_max = max(curr_max, arr[pos])
    
    if pos == n - 1:
        max_val.append(curr_max)
        return
    
    for i in range(1, min(k + 1, n - pos)):
        find_path(pos + i, curr_max)


find_path(0, 0)
print(min(max_val))