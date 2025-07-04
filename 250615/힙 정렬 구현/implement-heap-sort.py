# from typing import List

# n = int(input())
# arr = list(map(int, input().split()))

# # Please write your code here.

# # Compare and sort
# def heapify(arr: List[int], n: int, i: int) -> None:
#     largest = i
#     left = 2 * i
#     right = 2 * i + 1

#     if left < n and arr[left] > arr[largest]:
#         largest = left
    
#     if right < n and arr[right] > arr[largest]:
#         largest = right
    
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)


# def heap_sort(arr: List[int]) -> List[int]:
#     for i in range(n//2 - 1, -1, -1):
#         heapify(arr, n, i)
    
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
    
#     return arr

# sorted_arr = heap_sort(arr)
# print(' '.join(map(str, sorted_arr)))

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)  # 1-based indexing

def heapify(n: int, i: int) -> None:
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= n and arr[left] > arr[largest]:
        largest = left
    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(n, largest)

def heap_sort() -> None:
    for i in range(n // 2, 0, -1):
        heapify(n, i)

    for i in range(n, 1, -1):
        arr[i], arr[1] = arr[1], arr[i]
        heapify(i - 1, 1)

def solution() -> str:
    heap_sort()
    return ' '.join(map(str, arr[1:]))

print(solution())
