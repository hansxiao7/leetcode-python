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

        prev = None

        while l1 and l2:
            if l1.val <= l2.val:
                if prev is None:
                    prev = l1
                    start = l1
                else:
                    prev.next = l1
                    prev = prev.next
                l1 = l1.next
            else:
                if prev is None:
                    prev = l2
                    start = l2
                else:
                    prev.next = l2
                    prev = prev.next
                l2 = l2.next

        if l1:
            prev.next = l1

        if l2:
            prev.next = l2

        return start