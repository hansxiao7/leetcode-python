# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def correctBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        visited = set()

        def helper(node):
            if node is None:
                return None

            if node.right in visited:
                return None

            visited.add(node)
            node.right = helper(node.right)
            node.left = helper(node.left)

            return node

        return helper(root)