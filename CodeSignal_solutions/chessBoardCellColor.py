#Given two cells on the standard chess board, determine whether they have the same color or not.

def color(square):
    sum=int(square[1])+ord(square[0])-ord('A')+1
    if sum%2==0:
        c='dark'
    else:
        c='white'
    return c

def chessBoardCellColor(cell1, cell2):
    if color(cell1)==color(cell2):
        return True
    else:
        return False
