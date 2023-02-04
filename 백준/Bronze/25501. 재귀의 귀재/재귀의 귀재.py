import sys
input = sys.stdin.readline

def isPalindrome(s):
    length = len(s)
    answer = 1
    count = 0
    for index in range(length//2):
        if not s[index] == s[length-1-index]:
            answer = 0
            break
        count+=1
    return [answer,count+1]

arrs = [input().strip() for _ in range(int(input()))]
for value in arrs:
    print(*isPalindrome(value))

