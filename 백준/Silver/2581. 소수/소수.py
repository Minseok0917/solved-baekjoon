m = int(input())
n = int(input())
arrs = [ 0 for _ in range(n+1) ]
answer = []

for i in range(2,n+1):
    if arrs[i] == 0:
        if i >= m:
            answer.append(i)
        for j in range(i,n+1,i): arrs[j] = 1

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)




