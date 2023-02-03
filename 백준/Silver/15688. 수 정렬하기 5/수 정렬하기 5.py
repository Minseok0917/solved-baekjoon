import sys
input = sys.stdin.readline
def m(arr):
    length = len(arr)
    if length == 1:
        return arr
    mid = length//2
    left = m(arr[0:mid])
    right = m(arr[mid:])
    leftIdx = 0
    rightIdx = 0
    leftLength = len(left)
    rightLength = len(right)
    answer = []
    while leftIdx < leftLength and rightIdx < rightLength:
        leftValue = left[leftIdx]
        rightValue = right[rightIdx]
        if leftValue < rightValue:
            answer.append(leftValue)
            leftIdx+=1
        else:
            answer.append(rightValue)
            rightIdx+=1
    while leftIdx < leftLength:
        answer.append(left[leftIdx])
        leftIdx+=1
    while rightIdx < rightLength:
        answer.append(right[rightIdx])
        rightIdx+=1
    return answer

arrs = [ int(input()) for _ in range(int(input()))]
for i in m(arrs):
    print(i)