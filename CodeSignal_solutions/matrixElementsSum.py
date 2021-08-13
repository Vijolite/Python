#free rooms, or any of the rooms below any of the free rooms.
#Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

def matrixElementsSum(matrix):
    s=0
    for j in range (len(matrix[0])):
        i=0
        b=True
        while b and i<len(matrix):
            if matrix[i][j]==0:
                b=False
            else:
                s=s+matrix[i][j]
                i+=1
    return s

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

print(matrixElementsSum(matrix))
