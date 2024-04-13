# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        head  = prev = l1
        while l1 and l2:
            val = l1.val + l2.val + flag
            l1.val = val%10
            flag = val//10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if l2: prev.next = l1 = l2
        while l1:
            val = l1.val + flag
            l1.val = val%10
            flag = val//10
            prev = l1
            l1 = l1.next
        if flag: prev.next = ListNode(flag)
        return head