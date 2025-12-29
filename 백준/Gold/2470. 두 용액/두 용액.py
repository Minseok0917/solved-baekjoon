import sys 

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

numbers.sort()

left = 0
right = n - 1


answer = [0, 10000000000]
while left < right:
    left_value = numbers[left]
    right_value = numbers[right]
    result = abs(left_value + right_value)
    
    
    if result == 0:
        answer = [left_value, right_value]
        if left_value > right_value:
            answer = [right_value, left_value]
        break
    elif result < abs(answer[0] + answer[1]):
        answer = [left_value, right_value]
        if left_value > right_value:
            answer = [right_value, left_value]
    
    if abs(left_value) < abs(right_value):
        right -= 1
    else:
        left += 1


print(answer[0], answer[1])
