# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev  = dummy
        while True:
            kth = self.get_kth(groupPrev, k)
            if not kth:
                break
            groupNext =kth.next

            #reverse
            prev = kth.next #because I need to connect with the kth.next one after reverse

            current = groupPrev.next
            while current!=groupNext:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp
            temp =groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
    def get_kth(self,current, k):
        while current and k>0:
            current =current.next
            k = k-1
        return current
    
