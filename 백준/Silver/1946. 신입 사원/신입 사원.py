import sys 

t = int(sys.stdin.readline().strip())

counts = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    
    points = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().strip().split())
        points.append((a, b))
    
    points.sort(key=lambda x: x[0])
    
    
    count = 0
    min_a = 100001
    min_b = 100001
    for a, b in points:
        is_pass = False

        if a < min_a:
            min_a = a
            is_pass = True

        if b < min_b:
            min_b = b
            is_pass = True

        if is_pass:
            count += 1

    counts.append(count)

for count in counts:
    print(count) 