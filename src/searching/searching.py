def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    leftMost = 0
    rightMost = (len(arr) -1)

    found = False

    # Your code here
    while leftMost < rightMost and not found:
        middle = ((leftMost + rightMost) // 2)

        if arr[middle] == target:
            found = True

        else:
            if target < arr[middle]:
                rightMost = middle - 1
            # searching the bottom half
            else:
                leftMost = middle +1

    # return found

    return -1  # not found
