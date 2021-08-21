class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # binary search + prefix
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        def check_val(val, target):
            for i in range(val, len(prefix)):
                if prefix[i] - prefix[i - val] >= target:
                    # val is too larget
                    return True

            return False

        left = 1
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if check_val(mid, target):
                right = mid
            else:
                left = mid + 1

        if check_val(left, target):
            return left
        return 0