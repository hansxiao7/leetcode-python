# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 0:
            return head

        l = 0
        node = head

        while node:
            l += 1
            node = node.next

        k = k % l
        if k == 0:
            return head

        count = 1
        p1 = head

        while count < k:
            p1 = p1.next
            count += 1

        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next

        # p2 is the new head now
        p1.next = head

        while p1.next != p2:
            p1 = p1.next
        p1.next = None

        return p2