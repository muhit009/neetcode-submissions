# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.find_mid(head)
        reverse = self.reverse_list(mid.next)
        mid.next = None
        first = head
        second =reverse
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            first =temp1
            second =temp2
    def find_mid(self,head):
        fast= slow = head
        while fast and fast.next:
            fast =fast.next.next
            slow =slow.next
        return slow
    def reverse_list(self,head):
        before = None
        curr = head
        while curr:
            after =curr.next
            curr.next = before
            before= curr
            curr= after
        return before