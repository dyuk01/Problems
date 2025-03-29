n, l = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
# N -> increment L different elements by 1 to make maximum H score

def find_h(arr)-> int:
    hscore = 0
    for i in range(n):
        right = n - i - 1
        if arr[i] <= right:
            hscore = arr[i]
        else:
            break
    return hscore

a.sort()

freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_h = 0

for h in range(1, n + 1):
    count_h = 0
    candidates = []

    for key in freq.keys():
        if key >= h:
            count_h += freq[key]
        elif key + 1 >= h:
            candidates.append(freq[key])
    
    candidates.sort(reverse=True)
    
    total = count_h
    for i in range(min(l, len(candidates))):
        total += candidates[i]
    
    if total >= h:
        max_h = h

print(max_h)