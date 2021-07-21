# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        li = []
        inorder(root, li)
        return li[k - 1]


def inorder(node, li):
    if node:
        inorder(node.left, li)
        li.append(node.val)
        inorder(node.right, li)