T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
#  d1(k to S) <= d2(k to N)  --> Special distance
#       d1 = abs(S - k)
#       d2 = abs(N - k)
#  d1(k to S) > d2(k to N) --> Not Special distance
#  x = a ~ b


def find_min_s(k):
    min_dist = float('inf')
    for key, value in dimension.items():
        if value == 'S':
            min_dist = min(min_dist, abs(key - k))
    
    return min_dist


def find_min_n(k):
    min_dist = float('inf')
    for key, value in dimension.items():
        if value == 'N':
            min_dist = min(min_dist, abs(key - k))
    
    return min_dist


# Find special distance
def is_special_dist(k):
    return find_min_s(k) <= find_min_n(k)


dimension = {}
for letter, dist in zip(c, x):
    dimension[dist] = letter 
res = 0
# Iterate through a and b
for d in range(a, b + 1):
    if is_special_dist(d):
        res += 1

print(res)