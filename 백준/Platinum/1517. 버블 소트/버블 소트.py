import sys
dataLength = sys.stdin.readline()
array = list(map(int,sys.stdin.readline().split()))
swap = 0
def merge_sort(array):
    global swap
    length = len(array)
    if length < 2:
        return array
    midIndex = length//2
    leftArray = merge_sort(array[:midIndex])
    rightArray = merge_sort(array[midIndex:])
    leftCount = 0
    rightCount = 0
    leftLength = len(leftArray)
    rightLength = len(rightArray)
    newArray = []
    while ( leftCount<leftLength ) & ( rightCount<rightLength ):
        leftValue = leftArray[leftCount]
        rightValue = rightArray[rightCount]
        if leftValue > rightValue:
            newArray.append(rightValue)
            rightCount+=1
            swap += leftLength-leftCount
        else:
            newArray.append(leftValue)
            leftCount += 1
    if rightCount == rightLength:
        newArray = newArray+leftArray[leftCount:]
    elif leftCount == leftLength:
        newArray = newArray + rightArray[rightCount:]
    return newArray
merge_sort(array)
print(swap)