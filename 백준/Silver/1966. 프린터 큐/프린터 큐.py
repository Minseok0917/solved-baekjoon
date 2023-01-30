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
    def empty(self):
        return self.end - self.start <= 0
    def get(self):
        return self.arrays[self.start]
    def length(self):
        return self.end-self.start
    def isMax(self):
        return self.get() < max(self.arrays[self.start:self.end])
    
c = int(input())
arrs = []
for i in range(c):
    n, index = map(int,input().split())
    arrs.append([index,list(map(int,input().split()))])
    
for i in arrs:
    [index, arr] = i
    count = 1
    q = queue(arr)
    while True:
        if q.isMax():
            if index == 0:
                index = q.length()-1
            else:
                index-=1
            q.back()
        else:
            if index == 0:
                print(count)
                break
            q.remove()
            index-=1
            count+=1
    
    
    