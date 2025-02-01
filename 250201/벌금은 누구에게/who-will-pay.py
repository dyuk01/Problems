N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

def solution():    
    fine_calls = {}
    for person in student:
        if person not in fine_calls:
            fine_calls[person] = 1
        else:
            fine_calls[person] += 1
        if fine_calls[person] == K:
            return person
    return -1

print(solution())