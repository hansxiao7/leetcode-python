class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        left = 1
        right = n

        def check_val(val):
            count = 0
            for num in nums:
                if num <= val:
                    count += 1

            if count <= val:
                # too small
                return True
            return False

        while left < right:
            mid = (left + right) // 2
            if check_val(mid):
                left = mid + 1
            else:
                right = mid
        return left