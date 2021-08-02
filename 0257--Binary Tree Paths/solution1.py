# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return ['']
        self.result = []

        def helper(node, prev):
            if len(prev) == 0:
                prev = str(node.val)
            else:
                prev = prev + '->' + str(node.val)

            if node.left:
                helper(node.left, prev)

            if node.right:
                helper(node.right, prev)

            if node.left is None and node.right is None:
                self.result.append(prev)
                return

        helper(root, '')

        return self.result
