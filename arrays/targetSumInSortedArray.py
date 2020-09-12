arr = [1, 4, 45, 6, 10, -8]
def findTargetSum(arr, target):
    arr.sort()
    i=0
    j = len(arr) - 1
    sum = 0
    while(i<j):
        if arr[i]+arr[j] == target:
            return [i,j]
        elif arr[i]+arr[j] > target:
            j -= 1
        else:
            i += 1
    return -1
def findTargetSumUsingHash(arr, target):
    res = dict()
    
    for i in range(len(arr)):
        if target-arr[i] in res:
            return i, res[target-arr[i]]
        res[arr[i]] = i
    return -1
target = 16
print(findTargetSum(arr, 8))
print(findTargetSumUsingHash(arr, target))