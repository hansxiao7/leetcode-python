class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nums = arr
        n = len(arr)
        deleted = [0 for _ in range(n + 1)]
        not_deleted = [0 for _ in range(n + 1)]
        result = -sys.maxint

        for i in range(1, n + 1):
            deleted[i] = max(nums[i - 1], nums[i - 1] + deleted[i - 1], not_deleted[i - 1])
            not_deleted[i] = max(nums[i - 1], nums[i - 1] + not_deleted[i - 1])

            result = max(result, deleted[i], not_deleted[i])

        if max(arr) < 0:
            return max(arr)

        return result

