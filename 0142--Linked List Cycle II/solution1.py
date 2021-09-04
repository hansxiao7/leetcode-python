# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p1 = head
        p2 = head

        # check if there is a cycle
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                break

        if p2 is None or p2.next is None:
            return None

        p2 = head

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1