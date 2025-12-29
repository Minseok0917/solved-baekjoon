import sys

def merge(leftArray,rightArray):
    leftCount, rightCount, arrayList = 0, 0, []
    leftArrayLength = len(leftArray)
    rightArrayLength = len(rightArray)

    while (leftCount < leftArrayLength) and (rightCount < rightArrayLength):
        leftValue = str(leftArray[leftCount])
        rightValue = str(rightArray[rightCount])

        left = int(leftValue+rightValue)
        right = int(rightValue+leftValue)

        isLeft = left > right
        isRight = left < right
        if isLeft:
            arrayList.append(int(leftValue))
            leftCount += 1
        else:
            arrayList.append(int(rightValue))
            rightCount += 1
    if rightCount == rightArrayLength:
        arrayList = arrayList + leftArray[leftCount:]
    elif leftCount == leftArrayLength:
        arrayList = arrayList + rightArray[rightCount:]
    return arrayList


def merge_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    midIndex = length//2
    leftArray = merge_sort(arr[:midIndex])
    rightArray = merge_sort(arr[midIndex:])

    return merge(leftArray,rightArray)


K, N = map(int,sys.stdin.readline().split())
inputArray = []
inputMax = 0
for _ in range(K):
    inputValue = int(sys.stdin.readline())
    inputArray.append(inputValue)
    N -= 1
    if inputMax < inputValue:
        inputMax = inputValue

sortArray = merge_sort(inputArray)
result = ""
for value in sortArray:
    if N > 0 and value == inputMax:
        result += str(value)*N
        N = 0
    result += str(value)

print(result)