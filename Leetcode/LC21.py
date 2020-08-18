# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        Head = ListNode()
        tmpH = Head
        while l1 and l2:
            tmp = ListNode()
            if l1.val < l2.val:
                tmp.val = l1.val
                l1 = l1.next
            else:
                tmp.val = l2.val
                l2 = l2.next
            tmpH.next = tmp
            tmpH = tmp
        if l1:
            tmpH .next = l1
        if l2:
            tmpH.next = l2
        return Head.next
