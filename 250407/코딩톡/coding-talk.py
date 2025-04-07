n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

p -= 1
# Please write your code here.

# 'A' -> N amount of alphabets
# If new person arrive -> reads previous messages

# M amount of message informations

if u[p - 1] == 0:
    return

# Find who did not read the pth message
people = [chr(i) for i in range(ord('A'), ord('A') + n)]

# Go directly to pth message (1-indexed)
participants = set()

# Iterate from the pth to the end, and add to set()
for i in range(p - 1, m):
    if c[i] not in participants:
        participants.add(c[i])

suspects = []
# Subtract the elements from c to set(), to find who
# did not participate in the conversation + self
for person in people: 
    if person not in participants:
        suspects.append(person)
suspects.sort()

print(" ".join(res))
