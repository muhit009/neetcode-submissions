# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1<-2<-3<-4: 4->3->2->1

'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before, current = None, head
        while current:
            after = current.next
            current.next = before 
            before = current
            current = after
        return before