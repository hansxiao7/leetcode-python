# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        if len(nodes) == 0:
            return None
        if len(nodes) == 1:
            return nodes[0]

        nodes = set(nodes)
        self.result = None

        def helper(node):
            if node is None:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            if node in nodes:
                temp = 1 + l + r
            else:
                temp = l + r

            if self.result is None and temp == len(nodes):
                self.result = node

            return temp

        helper(root)
        return self.result