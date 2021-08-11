# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode()
        tail = dummy

        node = head
        while node:
            while node.next and node.val == node.next.val:
                node = node.next

            tail.next = node
            tail = tail.next
            node = node.next

        return dummy.next