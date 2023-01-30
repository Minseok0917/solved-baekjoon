class queue():
    def __init__(self,arrays):
        self.arrays = arrays
        self.start = 0
        self.end = len(arrays)
    def insert(self,value):
        self.end+=1
        self.arrays.append(value)
    def remove(self):
        self.start+=1
        return self.arrays[self.start-1]
    def back(self):
        self.insert(self.remove())
    def empty(self)        :
        return self.end - self.start <= 0
        
n, k = map(int,input().split())
q = queue([ i+1 for i in range(n) ])
count = 1
answer = []
while True:
    if q.empty():
        break
    if count%k == 0:
        answer.append(str(q.remove()))
    else:
        q.back()
    count+=1

print("<"+", ".join(answer)+">")
