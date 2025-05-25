n = int(input())
digit = []

# Please write your code here.
while True:
    if n < 2:
        digit.append(n)
        break
    
    digit.append(n % 2)
    n //= 2

print("".join(str(x) for x in digit[::-1]))