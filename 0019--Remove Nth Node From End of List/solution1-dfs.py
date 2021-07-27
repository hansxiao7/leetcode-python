# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None

        _, node = helper(head, n)
        return node


def helper(node, n):
    if node is None:
        return 0, None

    result, node.next = helper(node.next, n)
    result += 1
    if result == n:
        return result, node.next
    return result, node