n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.

# 'A' -> N amount of alphabets
# If new person arrive -> reads previous messages

# M amount of message informations
# Find who did not read the pth message

# Go directly to pth message (1-indexed)

# Iterate from the pth to the end, and add to set()

# Subtract the elements from c to set(), to find who