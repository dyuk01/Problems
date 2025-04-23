n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

def solution()-> int:
    routers = 0
    i = 0
    while i < n:
        if arr[i] == 0:
            i += 1
        else:
            # install here (covers i–M … i+M), but since all < i are already covered,
            # we just jump forward past the right edge:
            routers += 1
            i += 2 * m + 1
    return routers

print(solution())

    

