# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDistance(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: int
        """
        if p == q:
            return 0

        self.LCA = None

        def findLCA(node, p, q):
            if node is None:
                return False

            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)

            mid = node.val == p or node.val == q

            if left + right + mid >= 2:
                self.LCA = node

            return left or right or mid

        findLCA(root, p, q)
        queue = [self.LCA]

        h = 0
        result = []
        while len(queue) != 0:
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)

                if node.val == p or node.val == q:
                    result.append(h)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            h += 1

        return sum(result)