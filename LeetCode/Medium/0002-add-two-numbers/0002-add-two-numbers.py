# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = ''
        s2 = ''        
        while not l1.next == None:
            s1 = str(l1.val)+s1
            l1 = l1.next
        while not l2.next == None:
            s2 = str(l2.val)+s2
            l2 = l2.next
        s1 = str(l1.val)+s1
        s2 = str(l2.val)+s2
        s = str(int(s1)+int(s2))

        nodes = ListNode(s[0])
        for i in range(1,len(s)):
            value = s[i]
            node = ListNode(value)
            node.next = nodes
            nodes = node
        return nodes

    
    
    
        
        
            