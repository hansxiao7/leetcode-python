# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue = [(root, [root])]

        path1 = None
        path2 = None

        while len(queue) != 0:
            l_q = len(queue)
            for i in range(len(queue)):
                node, path = queue.pop(0)

                if node == p:
                    path1 = path

                if node == q:
                    path2 = path

                if node.left:
                    queue.append((node.left, path + [node.left]))

                if node.right:
                    queue.append((node.right, path + [node.right]))
            if path1 is not None and path2 is not None:
                break

        if len(path1) > len(path2):
            path1, path2 = path2, path1
        for i in range(len(path1)):
            if path1[i] == path2[i]:
                temp = path1[i]
                continue
            else:
                return temp

        return temp
