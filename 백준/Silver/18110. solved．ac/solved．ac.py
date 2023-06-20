import sys 

def customRound(num):
    intNum = int(num)
    return intNum+1 if num - intNum >= 0.5 else intNum

n = int(sys.stdin.readline())
limit = customRound(n/100*15)
sum = 0
array = []

if n == 0:
    print(0)
else:
    for _ in range(n):
        k = int(sys.stdin.readline())
        sum += k
        array.append(k)
    array.sort()

    arrayLength = len(array);
    for i in range(limit):
        sum -= array[i]
        sum -= array[arrayLength-i-1]

    print(customRound(sum/(arrayLength-limit*2)))