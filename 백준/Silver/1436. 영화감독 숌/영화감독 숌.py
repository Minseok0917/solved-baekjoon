n = int(input())
i = 666
count = 1

while True:
    if count == n:
        print(i)
        break
    i+=1
    if '666' in str(i):
        count+=1
    
    