class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        visited = set()
        result = []

        def helper(nums, curr):
            if len(curr) == len(nums):
                result.append(list(curr))
                return

            for i in range(len(nums)):
                if i != 0 and i - 1 not in visited and nums[i - 1] == nums[i]:
                    continue
                if i not in visited:
                    visited.add(i)
                    curr.append(nums[i])
                    helper(nums, curr)
                    curr.pop()
                    visited.remove(i)

        helper(nums, [])
        return result