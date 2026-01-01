import sys 

# mask = 0

# mask |= 1<<20
# print(mask)
# mask |= 1<<5
# print(mask)

# mask &= ~(1<<3)
# print(mask)

mask = 0
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    compare, *rest = input().strip().split()
    if len(rest) > 0:
        m = int(rest[0])

    if compare == "add":
       mask |= 1<<m

    elif compare == "remove":
        mask &= ~(1<<m)

    elif compare == "check":
        if mask & (1<<m):
            print(1)
        else:
            print(0)
    
    elif compare == "toggle":

        mask ^= 1<<m

    elif compare == "all":
        for i in range(1, 21):
            mask |= 1<<i
    elif compare == "empty":
        mask = 0