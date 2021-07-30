# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_n = 0

        def postorder(node):
            if node is None:
                return 1

            l_len = postorder(node.left)
            r_len = postorder(node.right)

            if node.left:
                if node.left.val == node.val + 1:
                    l_len += 1
                else:
                    l_len = 1

            if node.right:
                if node.right.val == node.val + 1:
                    r_len += 1
                else:
                    r_len = 1

            self.max_n = max(self.max_n, l_len, r_len)

            return max(l_len, r_len)

        postorder(root)

        return self.max_n



