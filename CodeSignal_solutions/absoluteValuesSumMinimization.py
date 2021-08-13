#Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum:
#abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
#(where abs denotes the absolute value)
#If there are several possible answers, output the smallest one.

def absoluteValuesSumMinimization(a):
    for i in range (len(a)):
        s=0
        for j in range (len(a)):
            if j!=i:
                s+=abs(a[j]-a[i])
        if i==0:
            m=s
            x=a[i]
        else:
            if s<m:
                m=s
                x=a[i]
    return x
