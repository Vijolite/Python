#In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

def valid(m,i,j):
    if 0<=i<len(m) and 0<=j<len(m[0]):
        return True
    else:
        return False
    
def new_value(m,i,j):
    v=0
    for ii in range(i-1,i+2):
        for jj in range(j-1,j+2):
            if valid(m,ii,jj) and not(ii==i and jj==j):
                if m[ii][jj]==True:
                    v+=1
    return v

def minesweeper(matrix):
    new=[]
    for i in range(len(matrix)):
        new_line=[]
        for j in range(len(matrix[0])):
            new_line.append(new_value(matrix,i,j))
        new.append(new_line)
    return new

matrix=[[True,False,False],  [False,True,False],  [False,False,False]]
print(minesweeper(matrix))
