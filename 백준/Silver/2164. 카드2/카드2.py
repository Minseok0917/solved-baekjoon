class q():
    def __init__(self,arrays):
        self.q = arrays
        self.start = 0
        self.end = len(arrays)
        
    def insert(self,value):
        self.q.append(value)
        self.end+=1
    
    def remove(self):
        self.start+=1
        return self.q[self.start-1]
    
    def get(self):
        return self.q[self.start]
    
    def len(self):
        return self.end - self.start
    

n = int(input())
m = q([i+1 for i in range(n)])
while True:
    if m.len() == 1:
        print(m.get())
        break
    m.remove()
    m.insert(m.remove())    
