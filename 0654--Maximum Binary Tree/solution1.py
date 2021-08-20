# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def helper(left, right):
            if left == right:
                return TreeNode(val=nums[left])

            if left > right:
                return None

            temp = -1
            pos = -1

            for i in range(left, right + 1):
                if nums[i] > temp:
                    pos = i
                    temp = nums[i]

            node = TreeNode(val=temp)

            l = helper(left, pos - 1)
            r = helper(pos + 1, right)

            node.left = l
            node.right = r

            return node

        return helper(0, len(nums) - 1)