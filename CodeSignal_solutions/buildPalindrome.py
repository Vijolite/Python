#Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
#Example
#For st = "abcdc", the output should be
#buildPalindrome(st) = "abcdcba".

def buildPalindrome(st):
    m=len(st)//2
    while m<len(st):
        i=0
        b=True
        r=0
        l=0
        while b and r<len(st)-1 :
            print('m = ',m)
            if i==0:
                if st[m-1]==st[m]:
                    l=m-1
                    r=m
                    i=1
                if i==0 and m+1<len(st):
                    if st[m-1]==st[m+1]:
                        l=m-1
                        r=m+1
                        i=1
                if i==0:
                    b=False
                print('l = ',l)
                print('r = ',r)
            else:
                l-=1
                r+=1
                print('l = ',l)
                print('r = ',r)
                if st[l]!=st[r]:
                    b=False
                else:
                    i+=1
                   

        if b:
            for j in range(m-i-1,-1,-1):
                st=st+st[j]
            return st
        else:
            m+=1
    return st+st[-2::-1]
    
print(buildPalindrome('abc'))
