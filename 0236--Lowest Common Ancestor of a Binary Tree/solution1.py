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
        result = []

        def find_path(node, p, path):
            if node is None:
                return

            if node == p:
                path.append(p)
                result.extend(list(path))
                return

            path.append(node)
            find_path(node.left, p, path)
            find_path(node.right, p, path)
            path.pop()

        find_path(root, p, [])
        p_path = list(result)
        result = []
        find_path(root, q, [])
        q_path = list(result)

        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                continue
            else:
                if i == 0:
                    return p_path[0]
                else:
                    return p_path[i - 1]

        if min(len(p_path), len(q_path)) == len(p_path):
            return p
        else:
            return q