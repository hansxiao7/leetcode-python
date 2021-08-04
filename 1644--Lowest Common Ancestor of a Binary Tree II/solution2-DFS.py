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
        p_path = []
        q_path = []

        helper(root, p, p_path, [])
        helper(root, q, q_path, [])

        if len(p_path) == 0 or len(q_path) == 0:
            return None

        length = min(len(p_path), len(q_path))

        for i in range(length):
            if p_path[i] == q_path[i]:
                continue
            else:
                return p_path[i - 1]

        if length == len(p_path):
            return p
        else:
            return q


def helper(node, p, result, curr):
    if node is None:
        return
    if node == p:
        curr.append(p)
        result.extend(list(curr))
        return

    curr.append(node)
    helper(node.left, p, result, curr)
    helper(node.right, p, result, curr)
    curr.pop()