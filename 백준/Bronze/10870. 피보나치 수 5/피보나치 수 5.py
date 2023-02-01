def init():
    n = int(input())
    arrs = [0,1,1]
    if n < 2:
        print(arrs[n])
        return
    for i in range(3,n+1):
        arrs.append(arrs[i-1]+arrs[i-2])
    print(arrs[n])

init()