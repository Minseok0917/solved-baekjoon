import sys
input = sys.stdin.readline

n = int(input())
# n = 3

for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(' ',end="")
        else:
            print("*",end="")
    print()
for i in range(1,n):
    for j in range(n):
        if j < i:
            print(' ',end="")
        else:
            print("*",end="")
    print()