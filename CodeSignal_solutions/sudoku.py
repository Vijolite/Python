#Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.
#This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

def sudoku(grid):

    for i in range(0,len(grid)-2,3):
        for j in range(0,len(grid[0])-2,3):
            li=[]
            for ii in range(i,i+3):
                for jj in range(j,j+3):
                    if grid[ii][jj] not in li:
                        li.append(grid[ii][jj])
                    else:
                        return False
    for i in range(0,len(grid)):
        li=[]
        for j in range(0,len(grid[0])):
            if grid[i][j] not in li:
                li.append(grid[i][j])
            else:
                return False
    for i in range(0,len(grid)):
        li=[]
        for j in range(0,len(grid[0])):
            if grid[j][i] not in li:
                li.append(grid[j][i])
            else:
                return False   
    
    return True

grid=[[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
print(sudoku(grid))
