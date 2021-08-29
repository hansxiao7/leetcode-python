# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # top down
        self.result = 0
        maxHeap = []
        minHeap = []

        def helper(node, currMax, currMin):
            if node is None:
                return

            currMax = max(node.val, currMax)
            currMin = min(node.val, currMin)

            if currMax - currMin > self.result:
                self.result = currMax - currMin

            helper(node.left, currMax, currMin)
            helper(node.right, currMax, currMin)

        helper(root, -sys.maxint, sys.maxint)

        return self.result