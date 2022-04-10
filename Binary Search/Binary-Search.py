def BinarySearch(array, target):
    return BinarySearchHelper(array, target, 0, len(array) - 1)


def BinarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potintialmatch = array[middle]
        if target == potintialmatch:
            return middle
        elif target < potintialmatch:
            right = middle - 1
        else:  # target > potintial match
            left = middle + 1
    return -1
  

print(BinarySearch([0,1,2,3,4,5,6,7,8,9,10], 7))