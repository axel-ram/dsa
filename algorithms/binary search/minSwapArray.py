def checkPossibility(nums):
    res = []
    '''
        binarySearch for the numbers where
        nums[i-1]>nums[i]
        put all indexes in res
        if len(res)>2:
        return false
    '''
    n = len(nums)
    return binarySearch(nums, 0, n-1, res)
def binarySearch(nums, low, high, res):
    if low>=high:
        print(low, high, res)
        return len(res)<2


    mid = low+(high-low+1)//2
    print(low, mid, high)
    if nums[mid] < nums[max(mid-1, 0)]:
        res.append(mid-1)
        print(res)
    leftSearch = binarySearch(nums, low, mid-2, res)
    rightSearch = binarySearch(nums, mid, high, res)
    return leftSearch and rightSearch

print(checkPossibility([4,2,3]))