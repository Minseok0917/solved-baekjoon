import sys 
input = sys.stdin.readline
t = int(input())
arrs = [ map(int,input().split()) for _ in range(t)]
for v in arrs:
    i,j = v
    i = i%10
    if i == 1:
        print(1)
    elif i == 2:
        print([6,2,4,8][j%4])
    elif i == 3:
        print([1,3,9,7][j%4])
    elif i == 4:
        print([6,4][j%2])
    elif i == 5:
        print(5)
    elif i == 6:
        print(6)
    elif i == 7:
        print([1,7,9,3][j%4])
    elif i == 8:
        print([6,8,4,2][j%4])
    elif i == 9:
        print([1,9][j%2])
    else:
        print(10)
    