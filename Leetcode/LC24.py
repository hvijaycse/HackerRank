# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        nhead = ListNode(val=0)
        nhead.next = head
        tmp = nhead
        # print(tmp.next)
        while tmp.next != None:
            if not tmp.next or not tmp.next.next:
                break
            a = tmp.next
            b = a.next
            # print(a.val, b.val)
            c = b.next
            tmp.next = b
            b.next = a
            a.next = c
            tmp = a
        return nhead.next
