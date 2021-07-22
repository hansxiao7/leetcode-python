# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        li = []
        inorder(root, li)
        dis = sys.maxint

        for i in range(len(li) - 1):
            dis = min(dis, abs(li[i + 1] - li[i]))

        return dis


def inorder(node, li):
    if node:
        inorder(node.left, li)
        li.append(node.val)
        inorder(node.right, li)