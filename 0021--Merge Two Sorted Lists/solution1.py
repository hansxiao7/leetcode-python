# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        left = l1
        right = l2

        head = None
        prev = None

        while left is not None and right is not None:
            if left.val <= right.val:
                if head is None:
                    head = left
                if prev:
                    prev.next = left
                prev = left
                left = left.next
            else:
                if head is None:
                    head = right
                if prev:
                    prev.next = right
                prev = right
                right = right.next

        if left:
            prev.next = left
        if right:
            prev.next = right

        return head