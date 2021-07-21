# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        error = sys.maxint
        node = root
        result = 0

        while node:
            if abs(target - node.val) < error:
                error = abs(target - node.val)
                result = node.val
            if target > node.val:  # on the right
                node = node.right
            else:  # on the left
                node = node.left

        return result
