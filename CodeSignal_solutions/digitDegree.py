#Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.
#Given an integer, find its digit degree.

def digitDegree(n):
    c=0
    while n>9:
        s=0
        x=n
        while x>0:
            s+=x%10
            x=x//10
        n=s
        c+=1
    return c
