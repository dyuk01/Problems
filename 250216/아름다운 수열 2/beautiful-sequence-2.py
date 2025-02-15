n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sequence = list(map(int, input().split()))

res = 0
for i in range(len(numbers) - m + 1):
    seq_counter = 0
    used = []
    for di in range(i, i + m):
        number = numbers[di]
        if number in sequence and number not in used:
            used.append(number)
            seq_counter += 1
            if seq_counter == m:
                res += 1
        else:
            break

print(res)