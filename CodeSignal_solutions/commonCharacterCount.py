#Given two strings, find the number of common characters between them.

def commonCharacterCount(s1, s2):
    m=0
    for i in range (ord('a'),ord('z')+1):
        c1=0
        c2=0
        for j in range (len(s1)):
            if s1[j]==chr(i):
                c1+=1
        for j in range (len(s2)):
            if s2[j]==chr(i):
                c2+=1
        m+=min(c1,c2)
    return m
           
s1='aabcc'
s2='adcaa'
print(commonCharacterCount(s1, s2))
