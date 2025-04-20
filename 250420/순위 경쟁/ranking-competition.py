n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.

def get_current_leaderboard(scores):
    max_score = max(scores.values())
    winners = []
    for key in scores.keys():
        if scores[key] == max_score:
            winners.append(key)
    return winners

def is_leaderboard_changed(old_leaderboard, new_leaderboard)-> bool:
    return old_leaderboard != new_leaderboard

changes = 0
# Set dict
scores = {}
for ch in range(ord("A"), ord("D")):
    scores[chr(ch)] = 0

curr_leaderboard = get_current_leaderboard(scores)

for ci, si in zip(c, s):
    scores[ci] += si
    new_leaderboard = get_current_leaderboard(scores)

    if is_leaderboard_changed(curr_leaderboard, new_leaderboard):
        curr_leaderboard = new_leaderboard
        changes += 1

print(changes)