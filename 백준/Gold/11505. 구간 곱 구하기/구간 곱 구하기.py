import sys

""" 

N: 1<= N <= 1,000,000
M: 1<= M <= 10,000 (수의 변경이 일어나는 횟수)
K: 1<= K <= 10,000 (구간의 곱을 구하는 횟수)


a: 1 (b번째수를 c로 변경)
a: 2 (b부터 c까지 곱을 구하여 출력)
"""

MOD = 1000000007

class Segment:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (len(arr) * 4)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(node * 2, start, mid)
            self.build(node * 2 + 1, mid + 1, end)
            self.tree[node] = (self.tree[node * 2] * self.tree[node * 2 + 1]) % MOD

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 1
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(node * 2, start, mid, left, right) * self.query(node * 2 + 1, mid + 1, end, left, right)) % MOD

    def update(self, node, start, end, index, value):
        if index < start or index > end:
            return
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            self.update(node * 2, start, mid, index, value)
            self.update(node * 2 + 1, mid + 1, end, index, value)
            self.tree[node] = (self.tree[node * 2] * self.tree[node * 2 + 1]) % MOD



n, m, k = list(map(int, sys.stdin.readline().strip().split()))
numbers = []
commands = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
for _ in range(m + k):
    commands.append(list(map(int, sys.stdin.readline().split())))


segment = Segment(numbers)
segment.build(1, 0, n - 1)

for command in commands:
    if command[0] == 1:
        segment.update(1, 0, n - 1, command[1] - 1, command[2])
    else:
        print(segment.query(1, 0, n - 1, command[1] - 1, command[2] - 1)%1000000007)
