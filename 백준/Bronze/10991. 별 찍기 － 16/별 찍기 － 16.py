import sys
input = sys.stdin.readline

n = int(input())
# n = 10
for i in range(n):
    count = 0
    for j in range(n*2):        
        if j == n-i-1 or j == n+i-1:
            print('*',end="")        
        elif j < n-i-1:
            print(' ',end="")
        elif j < n+i:
            if count:
                count = 0
                print('*',end="")
            else:
                count = 1
                print(' ',end="")

    print()