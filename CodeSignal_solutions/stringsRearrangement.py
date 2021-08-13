#Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.
#Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

def dist(s1,s2):
    d=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            d+=1
    return d

def check(ar):
    for i in range (len(ar)-1):
        if dist(ar[i],ar[i+1])!=1:
            return False
    return True
    
def stringsRearrangement(inputArray):
    from itertools import permutations
    per=list(permutations(inputArray,r=len(inputArray)))
    print(per)
    for i in range(len(per)):
        if check(per[i]):
            return True
    return False

inputArray=["ab",  "bb",  "aa"]
print(stringsRearrangement(inputArray))
