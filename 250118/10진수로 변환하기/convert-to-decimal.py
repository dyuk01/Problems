binary = input()

# Write your code here!
res = 0

idx = 0
for i in range(len(binary) - 1, -1, -1):
    if binary[i] == '1':
        res += 2 ** idx
    idx += 1

print(res)