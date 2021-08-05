# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        def helper(node):
            if node.next is None:
                return node
            if node.next.next is None:
                temp = node.next
                node.next.next = node
                node.next = None
                return temp

            follow = helper(node.next.next)
            temp = node.next
            node.next.next = node
            node.next = follow

            return temp

        return helper(head)
