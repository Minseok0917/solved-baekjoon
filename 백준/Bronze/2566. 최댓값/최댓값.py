row = 0
column = 0
maxnum = 0
for i in range(9):
    value = list(map(int,input().split()))
    index = 0
    for v in value: 
        if maxnum < v:
            maxnum = v
            row = i
            column = index
        index+=1
print(maxnum)
print(row+1,column+1)