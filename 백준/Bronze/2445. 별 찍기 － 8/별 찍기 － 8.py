import sys
input = sys.stdin.readline
n = int(input())
# n = 5
nn = 2*n-1


for i in range(n):
    for j in range(nn+1):
        if i+1 > j:
            print('*',end="")
        elif j > nn-i-1:
            print('*',end="")
        else:
            print(' ',end="")
    print()
for i in range(1,n):
    for j in range(nn+1):
        if j < n-i:
            print('*',end="")
        elif j > n+i-1:
            print('*',end="")
        else:
            print(' ',end="")
    print()

