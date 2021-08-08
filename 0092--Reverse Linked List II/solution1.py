# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head

        def reverse_helper(l, r):
            if l == r:
                l.next is None
                return l, l

            next_h, next_e = reverse_helper(l.next, r)

            l.next = None
            next_e.next = l

            return next_h, l

        # find left and right
        pos = 1
        node = head

        if left == 1:
            start_prev = None
            start = head
        else:
            while node.next:
                if pos + 1 == left:
                    start_prev = node
                    start = node.next
                    break
                node = node.next
                pos += 1

        while node:
            if pos == right:
                end = node
                break
            node = node.next
            pos += 1

        temp = end.next
        start, end = reverse_helper(start, end)

        if start_prev is not None:
            start_prev.next = start
        else:
            head = start
        end.next = temp

        return head

