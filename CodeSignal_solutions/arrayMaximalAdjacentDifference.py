#Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

def arrayMaximalAdjacentDifference(inputArray):
    m_diff=0
    for i in range (len(inputArray)-1):
        if abs(inputArray[i]-inputArray[i+1])>m_diff:
            m_diff=abs(inputArray[i]-inputArray[i+1])
    return m_diff
