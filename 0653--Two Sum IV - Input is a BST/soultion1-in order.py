# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        li = []
        inorder(root, li)

        left = 0
        right = len(li) - 1

        while left < right:
            if left < right and li[left] + li[right] > k:
                right -= 1
            if left < right and li[left] + li[right] < k:
                left += 1
            if left < right and li[left] + li[right] == k:
                return True

        return False


def inorder(node, li):
    if node:
        inorder(node.left, li)
        li.append(node.val)
        inorder(node.right, li)
