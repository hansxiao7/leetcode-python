# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 1. calculate the depth
        # 2. remember the paths
        if root is None:
            return None
        curr_d = {None: 0}
        d = tree_depth(root, curr_d)

        node = root
        while node:
            if curr_d[node.left] == curr_d[node.right]:
                return node
            elif curr_d[node.left] > curr_d[node.right]:
                node = node.left
            elif curr_d[node.left] < curr_d[node.right]:
                node = node.right


def tree_depth(node, curr_d):
    if node is None:
        return 0

    l = tree_depth(node.left, curr_d)
    r = tree_depth(node.right, curr_d)
    curr_d[node] = max(l, r) + 1

    return max(l, r) + 1
