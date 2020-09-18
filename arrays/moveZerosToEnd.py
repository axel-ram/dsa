def moveZerosToEnd(arr):
    '''
    two pointers
    [1] front, end
    [2] front<end
        [3] start at front and find first zero
        [4] simultaneously start from the end and find first non zero element
        [5] swap
        [6] front += 1
        [7] end -= 1
        [8] if arr[front] !=0:
            [9] front += 1
        [10] if arr[end] ==0:
            [11] end -= 1
    

    '''
    n = len(arr)
    if n<2:
        print(arr)
        return 
    front = 0
    end = n-1

    while(front < end):
        if arr[front] == 0 and arr[end] != 0:
            arr[front], arr[end] = arr[end], arr[front]
            front += 1
            end -= 1
        
        else:
            if arr[front] != 0:
                front += 1
            if arr[end] == 0:
                end -= 1
        
    print(arr)

moveZerosToEnd([0,0 ,0,0,0,0,0,0,0,0,0,0,0,0,0,-1, 0])