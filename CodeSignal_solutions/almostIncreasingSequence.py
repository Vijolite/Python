#Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
#Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

def  almostIncreasingSequence(sequence):
    m=0
    for i in range (len(sequence)-1):
        if sequence[i+1]<=sequence[i]:
            m+=1
            if i+2<len(sequence) and i!=0:
                if sequence[i+2]<=sequence[i]:
                    if sequence[i+1]<=sequence[i-1]:            
                        m+=1
            
    if m>1:
        return False
    else:
        return True
print(almostIncreasingSequence([1,2,5,3,5]))
