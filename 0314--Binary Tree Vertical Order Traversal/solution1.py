# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        maps = {}

        def helper(node, level, row):
            if node is None:
                return

            if level not in maps:
                maps[level] = []
            maps[level].append((node.val, row))

            helper(node.left, level - 1, row + 1)
            helper(node.right, level + 1, row + 1)

        helper(root, 0, 0)

        levels = maps.keys()
        levels.sort()

        result = []
        for l in levels:
            temp = []
            maps[l].sort(key=lambda x: x[1])
            for i, _ in maps[l]:
                temp.append(i)
            result.append(temp)

        return result