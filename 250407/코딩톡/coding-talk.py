n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# 0-Index p
p -= 1

# Please write your code here.

# 'A' -> N amount of alphabets
# If new person arrive -> reads previous messages

# M amount of message informations

# Find who did not read the pth message
people = [chr(i) for i in range(ord('A'), ord('A') + n)]

def add_suspect(arr):
    if u[p] == 0:
        return ""

    # Go directly to pth message (1-indexed)
    participants = set()

    


suspects = []
for i in range(m):
    suspects = add_suspect(suspects)

print(" ".join(suspects))
