n = int(input())

# Write your code here!

# Print the stars from n to 1.
def stars_top_down(k):
    # Base case.
    if k == 0:
        return
    
    print("* " * k)
    stars_top_down(k - 1)
    

# Print the stars from 1 to n.
def stars_bottom_up(k):
    # Base case.
    if k > n:
        return
    
    print("* " * k)
    stars_bottom_up(k + 1)


# Main algorithm.
stars_top_down(n)
stars_bottom_up(1)