import sys

n, p, q = list(map(int,sys.stdin.readline().strip().split()))

mm = { 0:1 }

def call(node,p,q):
    if node in mm:
        return mm[node]
    else:
        floor_p_index = node//p
        floor_q_index = node//q
        mm[node] = call(floor_p_index,p,q) + call(floor_q_index,p,q)
        return mm[node]


result = call(n,p,q)
print(result)

