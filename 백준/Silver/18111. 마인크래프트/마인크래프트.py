n, m, b = map(int,input().split())
arrs = [list(map(int,input().split())) for _ in range(n) ]
floor = 1
time = 23131823183103821321082


for cfloor in range(257):
    minusBlock, plusBlock = 0, 0
    for row in arrs:
        for column in row:
            if cfloor < column:
                minusBlock += column-cfloor
            elif cfloor > column:
                plusBlock  += cfloor-column
    
    if plusBlock-b <= minusBlock:
        if plusBlock + minusBlock*2 <= time:
            time = plusBlock + minusBlock*2
            floor = cfloor
        
        
        
print(time,floor)