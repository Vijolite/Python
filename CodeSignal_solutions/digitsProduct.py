#Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

import math

def is_prime(x):
    if x==1:
        answer=False
    else:
        k=1
        answer=True
        if x!=2:
           while k<math.sqrt(x) and answer==True:
                k=k+1
                if x/k==x//k:
                    answer = False
    return answer

def next_prime(x):
    y=x+1
    while not(is_prime(y)): #is_prime(y)==False
        y=y+1
    return(y)


def digitsProduct(product):
    #if a product contains as a factor a prime >=11 -> can not a product of digits
    if is_prime(product) and product>=11:
        return -1
    x=11
    while x<=product//2:
        if product % x ==0:
            return -1
        else:
            x=next_prime(x)
    
    p=1
    x=1
    while p!=product:
        p=1
        x=x+1
        c=x
        while c>0:
            p=p*(c%10)
            c=c//10

    return x
