class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # prefix sum
        if k == 1:
            return max(nums)

        temp = [0]
        total = 0
        result = -sys.maxint

        for i in range(len(nums)):
            total += nums[i]
            temp.append(total)
            if i < k - 1:
                continue
            else:
                result = max(result, (total - temp[i + 1 - k]) / float(k))
            print(result)
        return result