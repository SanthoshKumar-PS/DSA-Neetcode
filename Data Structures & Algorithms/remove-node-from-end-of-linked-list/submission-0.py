# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = ListNode(0)
        first.next = head
        head = first
        second = first
        while n>=0:
            n-=1
            second = second.next
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return head.next
        