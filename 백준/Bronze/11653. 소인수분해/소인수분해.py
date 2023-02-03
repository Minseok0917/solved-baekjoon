
n = int(input())
m = 2
if n > 1:   
    while True:
        if n%m == 0:
            n = n/m
            print(m)
            if n == 1:
                break
            m=2
        else:
            m+=1
