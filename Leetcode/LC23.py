# Definition for singly-linked list.

import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        sentinel, node1, node2 = ListNode(0), l1, l2
        node = sentinel
        while node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next

        node.next = node1 or node2
        return sentinel.next

    def mergeKLists(self, lists: [ListNode]) -> ListNode:

        queue = collections.deque(lists)
        while len(queue) > 1:
            queue.appendleft(self.mergeTwoLists(queue.pop(), queue.pop()))

        return queue[0] if queue else None
