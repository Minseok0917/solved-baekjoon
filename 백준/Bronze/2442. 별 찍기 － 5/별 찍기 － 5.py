import sys
input = sys.stdin.readline
n = int(input())
nn = 2*n-1


for i in range(n):
    for j in range(nn):
        if j < n-i-1:
            print(' ',end="")
        elif j > n+i-1:
            continue
        else:
            print('*',end="")
    print()