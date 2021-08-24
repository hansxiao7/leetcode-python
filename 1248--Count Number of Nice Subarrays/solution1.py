class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def helper(k):
            left = 0
            result = 0
            n = 0

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    n += 1

                while n > k:
                    if nums[left] % 2 != 0:
                        n -= 1
                    left += 1

                result += right - left + 1

            return result

        return helper(k) - helper(k - 1)