A = input()

# Write your code here!

res = 0
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] == '(':
            if A[j] == ')':
                res += 1

print(res)