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
        if head is None or head.next is None:
            return head

        node = head
        prev = node
        next = node.next
        prev.next = None

        while next:
            temp = next.next
            next.next = prev
            prev = next
            next = temp
        return prev

