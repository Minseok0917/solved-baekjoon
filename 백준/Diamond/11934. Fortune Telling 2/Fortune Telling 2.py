import sys 


card_count, command_count = map(int,sys.stdin.readline().split())

cards = []
commands = []

for _ in range(card_count):
    a, b = map(int, sys.stdin.readline().split())
    max_index = 1 if a < b else 0
    cards.append([a,b,max_index])

for _ in range(command_count):
    k = int(sys.stdin.readline())
    commands.append(k)

""" 
1. SegmentTree를 사용하여 P의 위치를 찾는 코드를 개발함
commands의 값을 정렬을 진행하고, 각 값에 대한 원본 값 배열과, 인덱스 배열을 만들어서 저장함
이미 정렬된 배열의 인덱스 배열을 기준으로, Segment Tree를 구상하여 각 인덱스 값을 기준으로 제일 큰 인덱스를 찾아서 출력하게끔 개발함
"""
def lower_bound(arr, k):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < k:
            left = mid + 1
        else:
            right = mid
    return left

class MergeSortTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[] for _ in range(4 * self.n)]
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = [arr[l]]
            return
        mid = (l + r) // 2
        self.build(arr, node * 2, l, mid)
        self.build(arr, node * 2 + 1, mid + 1, r)

        left_array = self.tree[node * 2]
        right_array = self.tree[node * 2 + 1]

        self.tree[node] = []
        left_index = 0
        right_index = 0

        while left_index < len(left_array) and right_index < len(right_array):
            left_value = left_array[left_index][1]
            right_value = right_array[right_index][1]

            if left_value < right_value:
                self.tree[node].append(left_array[left_index])
                left_index += 1
            else:
                self.tree[node].append(right_array[right_index])
                right_index += 1
        
        while left_index < len(left_array):
            self.tree[node].append(left_array[left_index])
            left_index += 1

        while right_index < len(right_array):
            self.tree[node].append(right_array[right_index])
            right_index += 1

        return

    def query(self, node, l, r, ql, qr, k):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return len(self.tree[node]) - self.lower_bound(self.tree[node], k)
        mid = (l + r) // 2
        return (
            self.query(node * 2, l, mid, ql, qr, k) +
            self.query(node * 2 + 1, mid + 1, r, ql, qr, k)
        )

    def lower_bound(self, arr, k):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][1] < k:
                left = mid + 1
            else:
                right = mid
        return left
class SegmentTreeMaxIndex:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)
    
    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
            return
        mid = (l + r) // 2
        self.build(arr, node * 2, l, mid)
        self.build(arr, node * 2 + 1, mid + 1, r)

        left_value = self.tree[node * 2]
        right_value = self.tree[node * 2 + 1]
        self.tree[node] = right_value if left_value < right_value else left_value
    
    def query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return -1
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2

        left_value = self.query(node * 2, l, mid, ql, qr)
        right_value = self.query(node * 2 + 1, mid + 1, r, ql, qr)
        return right_value if left_value < right_value else left_value




original_commands = [[index, command] for index, command in enumerate(commands)]
sorted_command_instance = MergeSortTree(original_commands)
sorted_commands = sorted_command_instance.tree[1]
sorted_command_values = [command[1] for command in sorted_commands]
sorted_command_indexes = [command[0] for command in sorted_commands]

st_sci = SegmentTreeMaxIndex(sorted_command_indexes)

answer = 0
for card in cards:
    a, b, max_index = card
    if a == b:
        answer += a
        continue

    min_card, max_card = [a, b]
    if max_index == 0:
        min_card, max_card = [b, a]

    query_left = lower_bound(sorted_command_values, min_card)
    query_right = lower_bound(sorted_command_values, max_card) - 1
    p = st_sci.query(1, 0, command_count - 1, query_left, query_right)
    count = sorted_command_instance.query(1, 0, command_count - 1, p+1, command_count - 1, max_card)

    
    arr = [max_card, min_card]
    if p == -1:
        arr = [a, b]


    card = arr[count%2]
    answer += card

    # print([a,b,max_index],p,count,commands,card)
    
print(answer)



# print([6,1,8,4,3])


# print(original_commands)
# print(sorted_commands)
# print(result, query_left, query_right)