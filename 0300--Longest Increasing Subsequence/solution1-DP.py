class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [1 for _ in range(len(nums))]

        for i in range(len(nums) - 2, -1, -1):
            temp = result[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    result[i] = max(result[i], result[j] + temp)

        print(result)

        return max(result)