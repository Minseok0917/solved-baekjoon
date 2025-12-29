import sys 

n = int(sys.stdin.readline().strip())
points = set(map(int, sys.stdin.readline().strip().split()))
x = int(sys.stdin.readline().strip())

count = 0

while points:
    point = points.pop()
    if x - point in points:
        count += 1
        points.remove(x - point)
print(count)

