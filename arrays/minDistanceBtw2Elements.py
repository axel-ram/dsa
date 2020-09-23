
def minDistanceBtwElements(nums, first, second):
    n = len(nums)
    if n<2:
        return 0
    indexOfFirst = -1
    indexOfSecond = -1
    minDistance = n
    for i in range(n):
        if first == nums[i]:
            indexOfFirst = i
        elif second == nums[i]:
            indexOfSecond = i
        
        if indexOfFirst != -1 and indexOfSecond != -1:
            minDistance = min(minDistance, abs(indexOfFirst-indexOfSecond))
    return minDistance
    
def minDistanceBtwElements2(nums, first, second):
    n = len(nums)
    if n<2: return 0

    latestIndex = -1
    minDistance = n
    for i in range(n):
        if nums[i] == first or second == nums[i]:
            if latestIndex != -1 and nums[i] != nums[latestIndex]:
                minDistance = min(minDistance, abs(latestIndex - i))
            latestIndex = i
    if minDistance != n:
        return minDistance
    else:
        return 0

print(minDistanceBtwElements([3,1,4,5,6,2], 2, 3))

print(minDistanceBtwElements2([3,1,4,5,2,2], 2, 3))

