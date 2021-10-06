# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """

        def helper(lowerBound, upperBound):
            if len(preorder) == 0 or preorder[0] < lowerBound or preorder[0] > upperBound:
                return None

            node = TreeNode(val=preorder.pop(0))

            node.left = helper(lowerBound, node.val)
            node.right = helper(node.val, upperBound)

            return node

        return helper(-sys.maxint, sys.maxint)