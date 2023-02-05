import sys
input = sys.stdin.readline
n = int(input())
# n = 3
nn = 2*n-1


for i in range(n):
    for j in range(nn):
        if j < i:
            print(' ',end="")
        elif j > nn-i-1:
            continue
            # print(' ',end="")
        else:
            print("*",end="")
    print()