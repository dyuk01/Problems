n = int(input())
sequence = list(map(int, input().split()))

# Write your code here!

res = []

# Sort seq
sorted_seq = sorted(sequence)

# Compare
for num in sequence:
    # print(num)
    for i in range(n):
        # print(sorted_seq[i])
        if num == sorted_seq[i]:
            res.append(str(i + 1))
            sorted_seq[i] = -1
            break

# Print indices sequentially
print(" ".join(res))