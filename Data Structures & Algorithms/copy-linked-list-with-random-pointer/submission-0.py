"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store ={None : None}

        curr= head
        while curr:
            copy = Node(curr.val)
            store[curr] = copy
            curr= curr.next
        
        curr= head
        while curr:
            copy = store[curr]
            copy.next = store[curr.next]
            copy.random =store[curr.random]
            curr =curr.next
        return store[head]
