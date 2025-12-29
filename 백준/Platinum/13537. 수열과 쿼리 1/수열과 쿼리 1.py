import sys

input = sys.stdin.readline
N = int(input())
N_Tree = [0]*(N*4)
N_Store = list(map(int,input().split()))
M = int(input())
M_Store = []
for _ in range(M):
    M_Store.append(list(map(int,input().split())))

def mergeTree(l,r,k):
    if l == r:
        N_Tree[k] = [N_Store[l-1]]
        return N_Tree[k]
    mid = (l+r)//2
    larray = mergeTree(l,mid,k*2)
    rarray = mergeTree(mid+1,r,k*2+1)
    result = merge(larray,rarray)
    N_Tree[k] = result
    return result

def merge(larray,rarray):
    answer = []
    llen = len(larray)
    lidx = 0
    rlen = len(rarray)
    ridx = 0
    if llen == 0:
        return rarray
    if rlen == 0:
        return larray

    while lidx < llen and ridx < rlen:
        lv = larray[lidx]
        rv = rarray[ridx]
        if lv < rv:
            lidx += 1
            answer.append(lv)
        else:
            ridx += 1
            answer.append(rv)
    if llen == lidx:
        answer+=rarray[ridx:]
    if rlen == ridx:
        answer+=larray[lidx:]
    return answer

def query(start,end,index,i,j,c):
    if j < start or end < i: return 0
    elif i <= start and end <= j:
        value = N_Tree[index]
        length = len(value)-1
        count = upper_bound(value,0,length,c)
        return count
    mid = (start+end)//2
    return query(start,mid,index*2,i,j,c)+query(mid+1,end,index*2+1,i,j,c)

def upper_bound(array,left,right,k):
    while left < right:
        mid = (left+right)//2
        if array[mid] <= k:
            left=mid+1
        else:
            right=mid
    mid = (left+right)//2
    if array[mid] > k:
        return len(array)-mid
    else:
        return 0

mergeTree(1,N,1)
for M_Item in M_Store:
    [a,b,c] = M_Item
    count = query(1,N,1,a,b,c)
    print(count)



