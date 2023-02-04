count = 1
def merge(arrs):
    global k, count
    length = len(arrs)
    if length == 1: return arrs
    mid = length//2 if length%2 == 0 else length//2+1
    left = merge(arrs[0:mid])
    right = merge(arrs[mid:])
    leftIdx = 0
    rightIdx = 0
    leftLength = len(left)
    rightLength = len(right)
    answer = []
    while leftIdx < leftLength and rightIdx < rightLength:
        leftValue = left[leftIdx]
        rightValue = right[rightIdx]
        if leftValue < rightValue:
            if count == k: print(leftValue); exit()
            answer.append(leftValue)
            leftIdx+=1
        else:
            if count == k: print(rightValue); exit()
            answer.append(rightValue)
            rightIdx+=1
        count+=1
    while leftIdx < leftLength:
        leftValue = left[leftIdx]
        if count == k: print(leftValue); exit()
        answer.append(leftValue)
        leftIdx+=1
        count+=1
    while rightIdx < rightLength:
        rightValue = right[rightIdx]
        if count == k: print(rightValue); exit()
        answer.append(rightValue)
        rightIdx+=1
        count+=1
    return answer

n, k = map(int,input().split())
a = list(map(int,input().split()))
merge(a); print(-1)