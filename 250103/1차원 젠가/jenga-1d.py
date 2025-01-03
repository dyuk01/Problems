n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def remove(arr: list, idx1: int, idx2: int) -> list :
    # Initialization.
    temp = []
    idx1 -= 1
    idx2 -= 1
    tempIdx = 0

    # Only add the elements outside of the index range to temp.
    for i in range(len(arr)):
        if i < idx1 or i > idx2:
            temp.append(arr[i])
    
    return temp


temp = remove(blocks, s1, e1)
temp = remove(temp, s2, e2)

print(len(temp))
for i in range(len(temp)):
    print(temp[i])


