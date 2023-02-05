import sys
input = sys.stdin.readline

n = int(input())
# n = 3
for i in range(n):
    for j in range(n*2):
        if j == n-i-1 or j == n+i-1:
            print('*',end="")
        elif j < n-i-1:
            print(' ',end="")
        elif j < n+i:
            print(' ',end="")

    print()