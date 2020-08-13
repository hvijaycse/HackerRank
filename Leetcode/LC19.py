# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = head
        Length = 0
        while tmp:
            tmp = tmp.next
            Length += 1
        tmp = head
        if n == Length:
            head = head.next
        elif n == 1:
            for _ in range( Length - 2):
                tmp = tmp.next
            tmp.next = None
        else:
            tmp2 = tmp.next
            for _ in range( Length - n - 1):
                tmp = tmp.next
                tmp2 = tmp2.next
            tmp.next = tmp2.next
        return head
