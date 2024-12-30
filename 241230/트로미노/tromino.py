n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Finds the maximum 3Sum among horizontal blocks including rotations
def flat_block():
    maxSum = 0

    def hori_block(row):
        maxSum = 0
        for i in range(len(row) - 2):
            temp = sum(row[i:i+3])
            if temp > maxSum:
                maxSum = temp
        return maxSum

    def vert_block(col):
        maxSum = 0
        for i in range(len(col) - 2):
            temp = sum(col[i:i+3])
            if temp > maxSum:
                maxSum = temp
        return maxSum

    for row in matrix:
        currSum = hori_block(row)
        if currSum > maxSum:
            maxSum = currSum

    for col in zip(*matrix):
        currSum = vert_block(col)
        if currSum > maxSum:
            maxSum = currSum
    
    return maxSum

# Finds the maximum 3Sum among L blocks including rotations
def l_block():
    maxSum = 0

    def noRotation(row, col):
        if col + 1 >= m or row + 1 >= n:
            return -1
        
        maxSum = matrix[row][col] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        return maxSum

    def rightRotation(row, col):
        if col + 1 >= m or row + 1 >= n:
            return -1

        maxSum = matrix[row][col] + matrix[row + 1][col] + matrix[row][col + 1]
        return maxSum

    def leftRotation(row, col):
        if col + 1 >= m or row + 1 >= n:
            return -1
    
        maxSum = matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row][col + 1]
        return maxSum

    def transpose(row, col):
        if col + 1 >= m or row + 1 >= n:
            return -1

        maxSum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col + 1]
        return maxSum

    for i in range(n):
        for j in range(m):
            temp = max(noRotation(i, j), rightRotation(i, j), 
            leftRotation(i, j), transpose(i, j))

            if temp > maxSum:
                maxSum = temp
    
    return maxSum

print(max(flat_block(), l_block()))
