#A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.
#Given a string, check whether it is beautiful.

def isBeautifulString(inputString):
    d=dict()
    for i in range(26):
        d[chr(ord('a')+i)]=0
    print(d)
    for i in range(len(inputString)):
        d[inputString[i]]+=1
    print(d)
    f=d['a']
    for i in d:
        print(i,' ',d[i])
        print(f)
        if d[i]>f:
            return False
        f=d[i]
    return True

s='aaabbcc'
print(isBeautifulString(s))
