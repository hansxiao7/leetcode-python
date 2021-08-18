# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        heap = []

        def helper(node, depth, y):
            if node is None:
                return

            heapq.heappush(heap, (y, depth, node.val))
            helper(node.left, depth + 1, y - 1)
            helper(node.right, depth + 1, y + 1)

        helper(root, 0, 0)

        result = {}

        while len(heap) != 0:
            y, d, val = heapq.heappop(heap)

            if y not in result:
                result[y] = []
            result[y].append(val)

        k_li = result.keys()
        k_li.sort()

        final = []

        for k in k_li:
            final.append(result[k])
        return final