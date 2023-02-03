arrs = []
while True:
    value = int(input())
    if value == 0:
        break
    else:
        arrs.append(value)

answer = []
mm = [i for i in range(123456*2)]
for i in range(2,123456*2):
    if mm[i] == -1: continue
    else:
        answer.append(i)
        for j in range(i*2,123456*2,i):
            mm[j] = -1
for i in arrs:
    count = 0
    for j in answer:
        if i < j and j <= i*2:
            count+=1
        elif j > i*2:
            break
    print(count)



