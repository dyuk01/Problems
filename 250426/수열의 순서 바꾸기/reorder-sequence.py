n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

# Type of insertion sort -> sort in non-decreasing order

# Pick a number at beginning

def solution()-> int:
    sorted_array = sorted(sequence)

    # Base Case check.
    if sequence == sorted_array:
        return 0

    steps = 0
    for i in range(n - 1):
        first_element = sequence[0]
        insert_pos = 1

        # Find the appropriate insert pos
        while insert_pos < n and first_element != n:
            insert_pos += 1
        
        # Make room for insertion
        for j in range(0, insert_pos - 1):
            sequence[j] = sequence[j + 1]
        
        sequence[insert_pos - 1] = first_element
        steps += 1

    return steps

print(solution())
