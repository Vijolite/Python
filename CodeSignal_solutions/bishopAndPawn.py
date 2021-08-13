# Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

def bishopAndPawn(bishop, pawn):
    Bc=bishop[0]
    Bl=int(bishop[1])
    Pc=pawn[0]
    Pl=pawn[1]
    while Bc<'h' and Bl>1:
        Bc=chr(ord(Bc)+1)
        Bl-=1
        if Bc==Pc and str(Bl)==Pl:
            return True
    Bc=bishop[0]
    Bl=int(bishop[1])
    while Bc>'a' and Bl<8:
        Bc=chr(ord(Bc)-1)
        Bl+=1
        if Bc==Pc and str(Bl)==Pl:
            return True
    Bc=bishop[0]
    Bl=int(bishop[1])
    while Bc>'a' and Bl>1:
        Bc=chr(ord(Bc)-1)
        Bl-=1
        if Bc==Pc and str(Bl)==Pl:
            return True
    Bc=bishop[0]
    Bl=int(bishop[1])
    while Bc<'h' and Bl<8:
        Bc=chr(ord(Bc)+1)
        Bl+=1
        if Bc==Pc and str(Bl)==Pl:
            return True
    return False
