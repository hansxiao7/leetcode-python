# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        if head is None:
            return None

        node = head
        while node.next:
            node = node.next

        def reverse_nodes(start, end):
            if start == end:
                return end, end

            new_start, new_end = reverse_nodes(start.next, end)
            new_end.next = start
            start.next = None

            return new_start, start

        prev_end = None

        start = head
        end = head

        while end:
            count = 1
            while count < k and end:
                end = end.next
                count += 1

            if end is None:
                prev_end.next = start
                break

            temp = end.next
            new_start, new_end = reverse_nodes(start, end)

            if prev_end is None:
                head = new_start
            else:
                prev_end.next = new_start

            prev_end = new_end
            start = end = temp

        return head
