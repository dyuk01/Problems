n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
normalized = list(map(lambda x: (min(x), max(x)), pairs))
normalized.sort()

max_count = count = 1
for i in range(1, m):
    if normalized[i] == normalized[i - 1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1

print(max_count)