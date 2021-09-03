class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            if nums[0] <= nums[1] and nums[1] <= nums[2]:
                return 1
            else:
                return 0
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        res = 0

        for right in range(len(prefix) - 2, 1, -1):
            # find the boundaries for left end
            l = 1
            r = right - 1
            val = prefix[right] / 2.0

            while l < r:
                mid = (l + r) // 2
                if prefix[mid] <= val:
                    l = mid + 1
                else:
                    r = mid

            if prefix[l] > val:
                l = l - 1
            rightBound = l

            l = 1
            r = right - 1
            val = 2 * prefix[right] - prefix[-1]

            while l < r:
                mid = (l + r) // 2
                if prefix[mid] >= val:
                    r = mid
                else:
                    l = mid + 1

            if prefix[l] < val:
                l = l + 1

            leftBound = l

            if leftBound <= rightBound:
                res += rightBound - leftBound + 1

        return res % (10 ** 9 + 7)



