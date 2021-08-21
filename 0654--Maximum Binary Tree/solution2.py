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
        left = [-1 for _ in range(len(nums))]
        stack = []

        for i in range(len(nums)):
            while len(stack) != 0 and nums[i] >= nums[stack[-1]]:
                stack.pop()

            if len(stack) != 0:
                left[i] = stack[-1]

            stack.append(i)

        right = [-1 for _ in range(len(nums))]
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            while len(stack) != 0 and nums[i] >= nums[stack[-1]]:
                stack.pop()

            if len(stack) != 0:
                right[i] = stack[-1]

            stack.append(i)

        nodes = []

        for i in range(len(nums)):
            nodes.append(TreeNode(val=nums[i]))

        for i in range(len(nums)):
            if left[i] != -1 and right[i] != -1:
                if nums[left[i]] < nums[right[i]]:
                    nodes[left[i]].right = nodes[i]
                else:
                    nodes[right[i]].left = nodes[i]

            elif left[i] == -1 and right[i] != -1:
                nodes[right[i]].left = nodes[i]
            elif right[i] == -1 and left[i] != -1:
                nodes[left[i]].right = nodes[i]
            else:
                head = nodes[i]

        return head