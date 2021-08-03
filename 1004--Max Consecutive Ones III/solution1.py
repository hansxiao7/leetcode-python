class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        result = 0

        n_1 = 0
        n_0 = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                n_1 += 1
            else:
                n_0 += 1

            while n_0 > k:
                if nums[left] == 1:
                    n_1 -= 1
                else:
                    n_0 -= 1
                left += 1
            result = max(result, right - left + 1)

        return result