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
res = []
for i in range(N):
    if command[i] == "push_back":
        res.append(num[i])
    elif command[i] == "pop_back":
        res.pop()
    elif command[i] == "size":
        print(len(res))
    else:
        print(res[num[i] - 1])