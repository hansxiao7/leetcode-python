class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 1
        right = max(nums)

        def check_val(val, threshold):
            total = 0
            for i in range(len(nums)):
                total += nums[i] // val + (nums[i] % val != 0)

            if total > threshold:
                # value is too small
                return True
            # val is too big
            return False

        while left < right:
            mid = (left + right) // 2
            if check_val(mid, threshold):
                # value is too small
                left = mid + 1
            else:
                right = mid

        return left