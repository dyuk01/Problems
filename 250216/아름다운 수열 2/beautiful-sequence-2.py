n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sequence = list(map(int, input().split()))

res = 0
for i in range(len(numbers) - m + 1):
    seq_counter = 0
    for di in range(i, i + m):
        number = numbers[di]
        if number not in sequence:
            break

        seq_counter += 1
        if seq_counter == m:
            res += 1

print(res)