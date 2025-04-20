n = int(input())
seats = input()

# Please write your code here.
occupied = []
for idx, s in enumerate(seats): 
    if s == '1':
        occupied.append(idx)


# 0 4 7 11