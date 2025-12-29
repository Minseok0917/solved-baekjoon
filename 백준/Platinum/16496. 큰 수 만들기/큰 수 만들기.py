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


N = int(sys.stdin.readline())
inputArray = list(map(int,sys.stdin.readline().split()))
isZero = True
for value in inputArray:
    if value > 0:
        isZero = False
        break

if isZero:
    print('0')
else:
    sortArray = merge_sort(inputArray)
    result = ""
    for value in sortArray:
        result += str(value)

    print(result)