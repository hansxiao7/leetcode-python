# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def helper(node):
            if node is None:
                return

            if node.left is not None and node.right is None:
                result.append(node.left.val)

            elif node.left is None and node.right is not None:
                result.append(node.right.val)

            helper(node.left)
            helper(node.right)

        helper(root)
        return result