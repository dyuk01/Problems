def mergesort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = [0] * (high - low + 1)
    i, j, k = low, mid + 1, 0

    # Both lists in bound
    while i <= mid and j <= high:
        # Left list smaller
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        # Right list smaller
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Merge leftover left list
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Merge leftover right list
    while j <= high:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy back to original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]

n = int(input())
arr = list(map(int, input().split()))
mergesort(arr, 0, len(arr) - 1)
print(' '.join(map(str, arr)))
