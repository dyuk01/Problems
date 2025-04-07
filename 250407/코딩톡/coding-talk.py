n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# # 0-Index p
p -= 1

# # Please write your code here.

# # 'A' -> N amount of alphabets
# # If new person arrive -> reads previous messages

# # M amount of message informations

# # Find who did not read the pth message
# people = [chr(i) for i in range(ord('A'), ord('A') + n)]

# def sol(arr):
#     if u[p] == 0:
#         return ""

#     # Go directly to pth message (1-indexed)
#     participants = set()

#     # Iterate from the pth to the end, and add to set()
#     for i in range(p, m):
#         if c[i] not in participants:
#             participants.add(c[i])

#     # Subtract the elements from c to set(), to find who
#     # did not participate in the conversation + self
#     for person in people: 
#         if person not in participants:
#             arr.append(person)
#     arr.sort()
#     return arr


# suspects = []
# print(" ".join(sol(suspects))

# Find the non-zero index from u using b-search.
def first_non_zero_idx() -> int:
    l, r = 0, m - 1
    idx = m

    while l <= r:
        mid = (l + r) // 2
        if u[mid] != 0:
            idx = mid
            r = mid - 1
        else:
            l = mid + 1

    return idx if idx < m else -1

# Find the first occurance index from u that has the same value with the u[p].
def first_occurrence_p_idx():
    target = u[p]
    l, r = 0, p
    result = p
    
    while l <= r:
        mid = (l + r) // 2
        if u[mid] == target:
            result = mid
            r = mid - 1
        elif u[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return result

# Return the list in white-space-separated string of potential unread people.
# Empty string if there are no unread candidates.
def solution() -> str:
    none_zero_idx = first_non_zero_idx()
    if none_zero_idx == -1 or p < none_zero_idx:
        return ""

    people = [chr(ord('A') + i) for i in range(n)]
    for j in range(first_occurrence_p_idx(), m):
        if c[j] in people:
            people.remove(c[j])
    
    return " ".join(people)

print(solution())
