from typing import List

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

# # Divide array
# def partition(arr: List[int], low: int, high: int) -> List[int]:
#     pivot = arr[high]
#     l = low - 1

#     for r in range(low, high):
#         if arr[r] <= pivot:
#             l += 1
#             arr[l], arr[r] = arr[r], arr[l]
    
#     arr[l + 1], arr[high] = arr[high], arr[l + 1]
#     return l + 1


def quick_sort(arr: List[int]):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left_arr = [i for i in arr[:-1] if i < pivot]
    right_arr = [i for i in arr[:-1] if i > pivot]
    middle_arr = [i for i in arr if i == pivot]

    return quick_sort(left_arr) + middle_arr + quick_sort(right_arr)

sorted_arr = quick_sort(arr)
print(' '.join(map(str, sorted_arr)))