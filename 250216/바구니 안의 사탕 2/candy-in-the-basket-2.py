n, k = map(int, input().split())

basket = [0 for _ in range(100)]

for _ in range(n):
    c, p = map(int, input().split())
    basket[p] = c

# Return the max amount of candy after finding middle point c
max_candy = 0
for i in range(k, len(basket) - k):
    curr_candy = 0
    for di in range(i - k, i + k + 1):
        curr_candy += basket[di]
    
    max_candy = max(max_candy, curr_candy)

print(max_candy)