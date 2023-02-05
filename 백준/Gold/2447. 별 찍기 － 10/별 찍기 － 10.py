import sys
input = sys.stdin.readline
n = int(input())
# n = 27

arrs = [[0 for _ in range(n)] for _ in range(n)]


def block(n,xx,yy):
    global arrs
    if n == 1:
        return
    limit = n//3
    for i in range(3):
        for j in range(3):     
            x = i*limit
            y = j*limit
            nextX = xx+x
            nextY = yy+y
            if i == 1 and j == 1:
                for x0 in range(nextX,nextX+limit):
                    for y0 in range(nextY,nextY+limit):
                        arrs[x0][y0] = " "
            else:
                block(limit,nextX,nextY)

block(n,0,0)

for t in arrs:
    for v in t:
        if v == 0:
            print('*',end="")
        else:
            print(" ",end="")
    print()
