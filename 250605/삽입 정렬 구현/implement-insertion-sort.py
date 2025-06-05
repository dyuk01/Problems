n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print(' '.join(map(str, arr)))