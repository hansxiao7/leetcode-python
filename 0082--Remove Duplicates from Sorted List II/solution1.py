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
            while node and node.next and node.val == node.next.val:
                temp = node.val
                while node and node.val == temp:
                    node = node.next
            tail.next = node
            tail = node
            if node:
                node = node.next
        return dummy.next

