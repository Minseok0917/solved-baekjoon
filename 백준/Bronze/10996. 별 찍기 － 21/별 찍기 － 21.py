import sys 


input = sys.stdin.readline 


n = int(input())


old = n % 2 != 0


for i in range(n*2):
    answer = ""
    if i % 2 == 0:
        answer = "* " * (n//2)
        if old:
            answer += "*"
    else:
        answer = " *" * (n//2)
        if old:
            answer += " "
    print(answer)
