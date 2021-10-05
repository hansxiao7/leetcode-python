# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        queue = [root]
        res = []
        while len(queue) != 0:
            n_q = len(queue)
            temp = 0
            for i in range(n_q):
                node = queue.pop(0)
                temp += node.val
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(temp / float(n_q))

        return res