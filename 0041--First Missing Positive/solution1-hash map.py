class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()

        for i in range(len(nums)):
            visited.add(nums[i])

        for i in range(1, len(nums) + 1):
            if i not in visited:
                return i

        return len(nums) + 1