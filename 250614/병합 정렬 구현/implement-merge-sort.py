n = int(input())
arr = list(map(int, input().split()))

def mergesort(arr: list)-> list:
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])

    return merge(left_arr, right_arr)

def merge(left: list, right: list)-> list:
    sorted_arr = []
    i, j = 0, 0

    # Both lists in bound
    while i < len(left) and j < len(right):
        # Left list smaller
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        # Right list smaller
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

res = mergesort(arr)
print(' '.join(map(str, res)))
