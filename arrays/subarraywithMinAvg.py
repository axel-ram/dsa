def minAvg(arr, k):
    '''
        time - O(n)
        space - O(1)
    '''
    n = len(arr)
    if k>n:
        return 0
    
    minAvg = sum([arr[i] for i in range(0,k)])/k
    start = 0
    end = k-1
    currentAvg = minAvg
    print(minAvg)
    for i in range(k, n):
        currentAvg += arr[i]/k - arr[i-k]/k
        if currentAvg < minAvg:
            minAvg = currentAvg
            start = i-k+1
            end = i
    return minAvg, start, end

print(minAvg([3, 7, 5, 20, -10, 0, 12], 2))

    