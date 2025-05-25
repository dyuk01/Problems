N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
# res = []
# for i in range(N):
#     if command[i] == "push_back":
#         res.append(num[i])
#     elif command[i] == "pop_back":
#         res.pop()
#     elif command[i] == "size":
#         print(len(res))
#     else:
#         print(res[num[i] - 1])

res = []

def push_back(A: int) -> None:
    res.append(A)

def pop_back() -> None:
    res.pop()

def size() -> int:
    return len(res)

def get(k: int) -> int:
    return res[k - 1]

def solution():
    for i in range(N):
        cmd = command[i]
        n = num[i]

        if cmd == "push_back":
            push_back(n)
        elif cmd == "pop_back":
            pop_back()
        elif cmd == "size":
            print(size())
        elif cmd == "get":
            print(get(n))

solution()
