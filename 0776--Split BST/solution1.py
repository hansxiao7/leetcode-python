# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def splitBST(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[TreeNode]
        """
        if root is None:
            return None, None

        if root.val <= target:
            l, r = self.splitBST(root.right, target)
            root.right = l
            return root, r
        else:
            l, r = self.splitBST(root.left, target)
            root.left = r
            return l, root