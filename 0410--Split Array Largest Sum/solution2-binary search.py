class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        def check_value(m, val):
            curr_sum = 0
            count = 1
            for i in range(len(nums)):
                curr_sum += nums[i]
                if curr_sum > val:
                    count += 1
                    curr_sum = nums[i]

                if count > m:
                    return False

            return True

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if check_value(m, mid):
                right = mid
            else:
                left = mid + 1
        return left
