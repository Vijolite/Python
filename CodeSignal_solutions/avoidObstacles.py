#You are given an array of integers representing coordinates of obstacles situated on a straight line.
#Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.
#Find the minimal length of the jump enough to avoid all the obstacles.

def avoidObstacles(inputArray):
    jump_coord=0
    jump=1
    inputArray.sort()
    while not(jump_coord in inputArray) and jump_coord<inputArray[-1]:
        jump_coord+=jump
        if jump_coord in inputArray:
            jump_coord=0
            jump+=1
    return jump
