import sys 
import heapq

n = int(sys.stdin.readline().strip())


heap = []

for _ in range(n):
    input_numbers = list(map(int, sys.stdin.readline().strip().split()))
    
    for number in input_numbers:
        if len(heap) < n:
            heapq.heappush(heap, number)
        else:
            if number > heap[0]:
                heapq.heapreplace(heap, number)

print(heap[0])

