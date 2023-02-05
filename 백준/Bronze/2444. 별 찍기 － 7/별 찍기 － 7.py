import sys
input = sys.stdin.readline
n = int(input())
# n = 3
nn = 2*n-1


for i in range(n):
    for j in range(nn):
        if j < n-i-1:
            print(' ',end="")
        elif j > n+i-1:
            # print(' ',end="")
            continue
        else:
            print('*',end="")
    print()
for i in range(1,n):
    for j in range(nn):
        if j < i:
            print(' ',end="")
        elif j > nn-i-1:
            continue
            # print(' ',end="")
        else:
            print("*",end="")
    print()