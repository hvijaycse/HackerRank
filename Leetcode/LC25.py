# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        NHead = tmp = ListNode(val=0, next=head)
        while tmp.next:
            count = 0
            tmp2 = tmp
            while tmp2.next:
                tmp2 = tmp2.next
                count += 1
            # print(count)
            if count >= k:
                count = k
                start = prev = tmp.next
                tmp2 = start.next
                while count - 1:
                    count -= 1
                    tmp3 = tmp2.next
                    tmp2.next = prev
                    prev = tmp2
                    tmp2 = tmp3
                tmp.next = prev
                start.next = tmp2
                tmp = start
            else:
                break
        return NHead.next
