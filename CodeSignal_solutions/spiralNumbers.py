#Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

def spiralNumbers(n):
    m=[]
    for i in range(n):
        m_line=[]
        for j in range (n):
            m_line.append(0)
        m.append(m_line)
    num=1
    line=0
    col=0
    c=n-1
    while num<n*n and c>=1:
        for i in range(c):
            m[line][col]=num
            num+=1
            col+=1
        for i in range(c):
            m[line][col]=num
            num+=1
            line+=1
        for i in range(c):
            m[line][col]=num
            num+=1
            col-=1
        for i in range(c):
            m[line][col]=num
            num+=1
            line-=1
        line+=1
        col+=1
        c-=2
    if c==0:
        m[line][col]=num
    return m
