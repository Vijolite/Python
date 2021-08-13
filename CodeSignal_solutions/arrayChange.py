#You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

def arrayChange(inputArray):
    moves=0
    for i in range(1,len(inputArray)):
        if inputArray[i]<=inputArray[i-1]:
            diff=inputArray[i-1]-inputArray[i]
            moves+=diff+1
            inputArray[i]=inputArray[i]+diff+1
    return moves

print(arrayChange([1,1,1]))
