n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

def restore_seq(arr)-> list:
    res = []
    idx = 0

    for i in range(1, adjacent[0]):
        init_num = i
        res.append(init_num)
        for j in arr:
            num = j - init_num
            if num not in res and num > 0:
                res.append(num)
            else:
                res.clear()
                break
            init_num = num

        if len(res) == n:
            return res

    return res

print(' '.join(map(str, restore_seq(adjacent))))
