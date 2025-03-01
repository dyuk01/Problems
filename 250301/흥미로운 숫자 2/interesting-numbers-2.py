X, Y = map(int, input().split())

# Please write your code here.
# Interesting number : only one digit is different

# Check if number is interesting number
def is_interesting_num(num):
    return len(set(str(num))) == 2

res = 0
# Iterate from X and Y
for num in range(X, Y + 1):
    if is_interesting_num(num):
        res += 1

print(res)
