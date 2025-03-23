n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# normalized = list(map(lambda x: (min(x), max(x)), pairs))
# normalized.sort()

# max_count = count = 1
# for i in range(1, m):
#     if normalized[i] == normalized[i - 1]:
#         count += 1
#         max_count = max(max_count, count)
#     else:
#         count = 1

# print(max_count)

cnt_dict = {}

for pair in pairs:
    pair = (min(pair), max(pair))
    if pair not in cnt_dict:
        cnt_dict[pair] = 1
    else:
        cnt_dict[pair] += 1

print(max(cnt_dict.values()))