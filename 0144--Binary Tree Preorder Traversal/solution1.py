# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        helper(result, root)
        return result


def helper(result, node):
    if node:
        result.append(node.val)
        helper(result, node.left)
        helper(result, node.right)