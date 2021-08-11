# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        dups = set()

        node = head
        while node:
            if node.val in seen:
                dups.add(node.val)
            seen.add(node.val)

            node = node.next

        dummy = ListNode()
        tail = dummy

        node = head
        while node:
            while node and node.val in dups:
                node = node.next

            tail.next = node
            tail = tail.next
            if node:
                node = node.next

        return dummy.next