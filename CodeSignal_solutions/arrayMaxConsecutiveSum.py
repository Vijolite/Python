# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

def arrayMaxConsecutiveSum(inputArray, k):
    for i in range(0,len(inputArray)-k+1):
        if i==0:
            s=0
            for j in range(i,i+k):
                s+=inputArray[j]
        else:
            s=s+inputArray[i+k-1]-inputArray[i-1]
        if i==0 or s>ms:
            ms=s
    return ms

print(arrayMaxConsecutiveSum([2,3,5,1,6], 3))
