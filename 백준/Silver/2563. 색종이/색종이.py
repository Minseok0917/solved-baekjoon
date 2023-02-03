arrs = [  [0 for _ in range(100)] for _ in range(100) ]
inputs = [ map(int,input().split()) for _ in range(int(input())) ]
totals = 0
for v in inputs:
    x0, y0 = v
    for x in range(x0,x0+10):
        for y in range(y0,y0+10):
            if arrs[x][y] == 1: continue
            else:
                arrs[x][y] = 1
                totals +=1
print(totals)
