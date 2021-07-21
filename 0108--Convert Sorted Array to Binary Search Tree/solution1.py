# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return helper(nums, 0, len(nums) - 1)


def helper(li, left, right):
    if left < right:
        mid = (left + right) // 2
        mid_node = TreeNode(val=li[mid])
        mid_node.left = helper(li, left, mid - 1)
        mid_node.right = helper(li, mid + 1, right)
        return mid_node
    elif left == right:
        return TreeNode(val=li[left])
    else:
        return None