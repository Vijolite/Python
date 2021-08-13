#Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
#Given a ticket number n, determine if it's lucky or not.

def dig_sum(s):
    n=int(s)
    su=0
    for i in range(len(s)):
        last_dig=n%10
        n=n//10
        su+=last_dig
    return su
    
    
def isLucky(n):
    s=str(n)
    s1=s[:len(s)//2]
    s2=s[len(s)//2:]
    if dig_sum(s1)==dig_sum(s2):
        return True
    else:
        return False
