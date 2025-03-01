X, Y = map(int, input().split())

# Please write your code here.
# Interesting number : only one digit is different

# Check if number is interesting number
def is_interesting_num(num):
    str_num = str(num)
    unique_digits = {}

    for digit in str_num:
        if digit in unique_digits:
            unique_digits[digit] += 1
        else:
            unique_digits[digit] = 1
    
    if len(unique_digits) != 2:
        return False
    
    counts = list(unique_digits.values())

    return 1 in counts

res = 0
# Iterate from X and Y
for num in range(X, Y + 1):
    if is_interesting_num(num):
        res += 1

print(res)
