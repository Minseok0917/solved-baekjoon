import sys 

input = sys.stdin.readline 
n = int(input())

for i in range(n):
    answer = ""
    if i % 2 == 0:
        answer = "* " * n
    else:
        answer = " *" * n
    print(answer)
