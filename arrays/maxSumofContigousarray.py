def maxSubarraySum(arr):
    '''
    [1] go through the array
    [2] check for 2 things
    [3] if maxsumsofar > currentmaxsum:
    [4] if it is true then update maxsumsofar
    [5] check if maxsumsofar < 0]
    [6] reset maxsumsofar
    '''
    start = 0
    end = 0

    maxSumSoFar = 0
    currentMaxSum = 0
    for i in range(len(arr)):
        currentMaxSum += arr[i]
        if maxSumSoFar < currentMaxSum:
            maxSumSoFar = currentMaxSum
            start = s
            end = i
        if currentMaxSum < 0:
            currentMaxSum = 0
            s = i+1
    return maxSumSoFar, start, end


print(maxSubarraySum([-2, -3, 4, -1, -2, 1, 5, -3]))