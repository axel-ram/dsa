def minDiffHeights(heights, k):
    heights.sort()
    diff = heights[-1] - heights[0]
    n = len(heights)
    minHeight = heights[0] + k
    maxHeight = heights[-1] - k
    
    for i in range(1, n-1):
        subtract = heights[i] - k
        add = heights[i] + k
        
        if maxHeight - subtract <= add - minHeight:
            minHeight = subtract
        else:
            maxHeight = add

    return min(diff, maxHeight-minHeight)

print(minDiffHeights([1,15,10], 6))

