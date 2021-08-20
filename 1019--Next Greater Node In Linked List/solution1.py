# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nums = []

        node = head
        while node:
            nums.append(node.val)
            node = node.next

        result = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) != 0 and nums[i] >= stack[-1]:
                stack.pop()

            if len(stack) != 0:
                result[i] = stack[-1]

            stack.append(nums[i])

        return result