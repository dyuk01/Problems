n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

# Type of insertion sort -> sort in non-decreasing order

# Pick a number at beginning

def solution()-> int:
    steps = 0
    if sequence == sequence.sort():
        return steps

    for i in range(n):
        for j in range(i, n - 1):
            if sequence[j] > sequence[j + 1]:
                steps += 1
                continue

print(solution())

