answer = []
maxmum = 10000
mm = [i for i in range(maxmum)]
for i in range(2,maxmum):
    if mm[i] == -1: continue
    else:
        answer.append(i)
        for j in range(i*2,maxmum,i):
            mm[j] = -1

arrs = [int(input()) for _ in range(int(input())) ]

for value in arrs:    
    storage = []
    index = 0
    for i in answer:
        if( i >= value): break
        for j in answer[index:]:
            if i+j > value: break
            if i+j == value:
               storage.append([i,j]) 
               break
        index+=1
    print(*storage[-1])
        