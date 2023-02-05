import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    for j in range(n):
        if j < i:
            print(' ',end="")
        else:
            print('*',end="")
    print('',end="\n")