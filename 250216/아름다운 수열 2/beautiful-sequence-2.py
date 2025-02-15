n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sequence = list(map(int, input().split()))

res = 0
for i in range(len(numbers) - m + 1):
    seq_counter = 0

    seq_check = sequence.copy()
    for di in range(i, i + m):
        number = numbers[di]

        if number in seq_check:
            seq_check.remove(number)
            seq_counter += 1
            if seq_counter == m:
                res += 1
        else:
            break

print(res)