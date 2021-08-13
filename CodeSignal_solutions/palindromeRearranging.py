#Given a string, find out if its characters can be rearranged to form a palindrome.

def palindromeRearranging(inputString):
    ch_l=[]
    ch_c=[]
    for i in range(len(inputString)):
        if inputString[i] in ch_l:
            ch_c[ch_l.index(inputString[i])]+=1
        else:
            ch_l.append(inputString[i])
            ch_c.append(1)
    odd_count=0
    for i in range(len(ch_c)):
        if ch_c[i]%2!=0:
            odd_count+=1
    if odd_count==0 and len(inputString)%2==0 or odd_count==1 and len(inputString)%2==1:
        return True
    else:
        return False
print(palindromeRearranging('ab3c2a6bc23'))
