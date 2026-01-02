import sys 

input = sys.stdin.readline

a, b, c = map(int, input().strip().split())


[a,b,c] = sorted([a,b,c])

unit = b-a

if c == b+unit:
    print(c+unit)
else:
    print(c-unit)