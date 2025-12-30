import sys

n, p, q, x, y = list(map(int,sys.stdin.readline().strip().split()))

mm = {}

def call(node,p,q,x,y):
    if node <= 0:
        mm[node] = 1
        return mm[node]

    elif node in mm:
        return mm[node]
    
    else:
        floor_p_index = node//p - x 
        floor_q_index = node//q - y

        a = call(floor_p_index,p,q,x,y)
        b = call(floor_q_index,p,q,x,y)

        if a <= 0:
            a = 1
        if b <= 0:
            b = 1

        mm[node] = a + b
        

        return mm[node]


result = call(n,p,q,x,y)
print(result)

