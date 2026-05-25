# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        count1 = 0
        head = headA
        while head:
            count1+=1
            head = head.next
        count2 = 0
        head = headB
        while head:
            count2+=1
            head = head.next
        while count1>count2:
            headA = headA.next
            count1-=1
        
        while count1<count2:
            headB = headB.next
            count2-=1
        print(headA.val, headB.val)
        while headA and headB:
            if headA==headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None