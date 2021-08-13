#Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

def differentSquares(matrix):
    li=[]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if [matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]] not in li:
                li.append([matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]])
    return (len(li))
matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
print(differentSquares(matrix))
