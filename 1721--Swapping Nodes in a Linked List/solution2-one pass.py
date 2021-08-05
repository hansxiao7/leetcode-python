# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        p1 = head
        count = 1

        while p1:
            if count == k:
                start = p1
                break
            p1 = p1.next
            count += 1
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next

        temp = start.val
        start.val = p2.val
        p2.val = temp

        return head
