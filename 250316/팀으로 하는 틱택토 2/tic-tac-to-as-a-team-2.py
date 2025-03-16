# inp = [input() for _ in range(3)]

# # Please write your code here.

# def check_team_win(s):
#     if len(s) == 2 and s not in answers:
#         answers.append(s)

# answers = []

# # Count answer horizontally
# for i in range(3):
#     check_team_win(set(inp[i]))

# # Count answer vertically
# for j in range(3):
#     num_v = set()
#     for i in range(3):
#         num_v.add(inp[i][j])

#     check_team_win(num_v)

# # Count answer diagonally
# num_d = set()
# for i in range(3):
#     num_d.add(inp[i][i])

# check_team_win(num_d)

# num_d = set()
# for i in range(3):
#     num_d.add(inp[i][2 - i])

# check_team_win(num_d)

# print(len(answers))



from typing import Set

inp = [input() for _ in range(3)]

answers = []

# Check the directional set to see if there is a team win.
def check_team_win(s: Set[int]) -> None:
    if len(s) == 2 and s not in answers:
        answers.append(s)

def solution() -> int:
    # Horizontal.
    for i in range(3):
        check_team_win(set(inp[i]))
    
    # Vertical.
    for j in range(3):
        check_team_win({inp[0][j], inp[1][j], inp[2][j]})
    
    # Bottom-right diagonal.
    check_team_win({inp[0][0], inp[1][1], inp[2][2]})

    # Bottom-left diagonal.
    check_team_win({inp[0][2], inp[1][1], inp[2][0]})

    return len(answers)

print(solution())
    