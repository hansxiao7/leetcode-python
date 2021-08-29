# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        def helper(node):
            if node is None:
                return ''

            result = str(node.val)
            if node.left:
                result += '(' + helper(node.left) + ')'
                if node.right:
                    result += '(' + helper(node.right) + ')'
            else:
                if node.right:
                    result += '()' + '(' + helper(node.right) + ')'

            return result

        return helper(root)