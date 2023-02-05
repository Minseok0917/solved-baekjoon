import sys
input = sys.stdin.readline

n = int(input())
minX, maxX = 0, n*2
minY, maxY = 0, n  
arrs = [[ 0 for _ in range(maxX) ] for _ in range(maxY)]


def block(x,y):
    global arrs
    n = 6
    n1 = n//2
    n2 = n-1
    for i in range(n1):
        for j in range(n2):
            if i == n1//2 and j == n2//2:
                continue
            elif j < n1-i-1:
                continue
            elif j >n1+i-1:
                continue
            else:
                arrs[i+y][j+x] = "*"

def init(minX,maxX,minY,maxY):
    x = maxX-minX
    y = maxY-minY
    if y <= 3:
        block(minX,minY)
        return 

    limitX = x//4 
    limitX2 = x//2 
    limitY = y//2

    init(minX+limitX,maxX-limitX,minY,minY+limitY)
    init(minX,minX+limitX2,minY+limitY,maxY)
    init(minX+limitX2,maxX,minY+limitY,maxY)


init(minX,maxX,minY,maxY)

for i in arrs:
    for j in i:
        if j == 0:
            print(" ",end="")
        else:
            print("*",end="")
    print()

