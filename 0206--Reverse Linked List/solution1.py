# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        def helper(start, end):
            if start == end:
                start.next = None
                return start, start

            l, r = helper(start.next, end)
            start.next = None
            r.next = start
            return l, start

        node = head
        while node.next:
            node = node.next
        end = node

        start, end = helper(head, node)

        return start