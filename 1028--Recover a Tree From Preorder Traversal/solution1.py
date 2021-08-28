# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """

        def helper(left, right, depth):
            if left > right:
                return None

            i = left
            node_val = 0

            while i <= right and traversal[i].isnumeric():
                node_val = 10 * node_val + int(traversal[i])
                i += 1

            node = TreeNode(val=node_val)

            l = None
            r = None
            while i <= right:
                if traversal[i] == '-':
                    count = 1

                    while i <= right - 1 and traversal[i + 1] == '-':
                        i += 1
                        count += 1

                    if i <= right - 1 and count == depth:
                        if l is None:
                            l = i + 1
                        elif r is None:
                            r = i + 1
                i += 1

            if l:
                if r:
                    node.left = helper(l, r - depth - 1, depth + 1)
                else:
                    node.left = helper(l, right, depth + 1)

            if r:
                node.right = helper(r, right, depth + 1)

            return node

        return helper(0, len(traversal) - 1, 1)

