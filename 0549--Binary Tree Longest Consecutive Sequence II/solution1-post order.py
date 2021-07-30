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
            if node.left is None and node.right is None:
                self.max_n = max(1, self.max_n)
                return 1, 1  # 正序或者倒序
            if node.left:
                l_len1, l_len2 = postorder(node.left)
            else:
                l_len1, l_len2 = 0, 0

            if node.right:
                r_len1, r_len2 = postorder(node.right)
            else:
                r_len1, r_len2 = 0, 0

            if node.left and node.right:
                temp = 0
                if (node.left.val - node.val) == 1 and (node.val - node.right.val) == 1:
                    temp = l_len1 + 1 + r_len2
                elif (node.left.val - node.val) == -1 and (node.val - node.right.val) == -1:
                    temp = l_len2 + 1 + r_len1
                self.max_n = max(self.max_n, temp)

            if node.left:
                if node.left.val == node.val + 1:
                    l_len1 += 1
                else:
                    l_len1 = 1

                if node.left.val == node.val - 1:
                    l_len2 += 1
                else:
                    l_len2 = 1

            if node.right:
                if node.right.val == node.val + 1:
                    r_len1 += 1
                else:
                    r_len1 = 1

                if node.right.val == node.val - 1:
                    r_len2 += 1
                else:
                    r_len2 = 1

            self.max_n = max(self.max_n, l_len1, l_len2, r_len1, r_len2)

            return max(l_len1, r_len1), max(l_len2, r_len2)

        postorder(root)

        return self.max_n




