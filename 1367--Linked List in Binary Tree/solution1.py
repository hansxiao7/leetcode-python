# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        def isSubPath(head, root):
            if head is None:
                return True
            if root is None:
                return False

            if (isSame(head, root)):
                return True
            else:
                return isSubPath(head, root.left) or isSubPath(head, root.right)

        def isSame(head, root):
            if head is None:
                return True
            if root is None:
                return False
            if head.val != root.val:
                return False
            else:
                return isSame(head.next, root.left) or isSame(head.next, root.right)

        return isSubPath(head, root)