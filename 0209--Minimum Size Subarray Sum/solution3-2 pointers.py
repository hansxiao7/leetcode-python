class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        result = sys.maxint

        left = 0
        right = 1

        while right < len(prefix):
            while right < len(prefix) and prefix[right] - prefix[left] < target:
                right += 1

            result = min(result, right - left)
            left += 1

        if result > len(nums):
            return 0
        return result

