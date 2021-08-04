# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = [root]
        flag = False

        result = []

        while len(queue) != 0:
            n = len(queue)
            temp = []

            for i in range(n):
                node = queue.pop(0)
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if flag:
                temp.reverse()
            flag = not flag
            result.append(temp)

        return result