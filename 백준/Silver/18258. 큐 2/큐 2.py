class qq():
    def __init__(self):
        self.n = []
        self.start = 0
        self.end = 0
    def push(self,value):
        self.n.append(value)
        self.end+=1
    def pop(self):
        if self.empty():
            return -1
        self.start+=1
        return self.n[self.start-1]
    def size(self):
        return self.end-self.start
    def empty(self):
        return self.end-self.start == 0
    def front(self):
        if self.empty():
            return -1
        return self.n[self.start]
    def back(self):
        if self.empty():
            return -1
        return self.n[self.end-1]

p = qq()

arrs  = [input() for _ in  range(int(input()))]
for i in arrs:
    if i == 'pop':
        print(p.pop())
    elif i == 'size':
        print(p.size())
    elif i == 'empty':
        print( 1 if p.empty() else 0 )
    elif i == 'front':
        print(p.front())
    elif i == 'back':
        print(p.back())
    else:
        n, m = i.split()
        p.push(m)