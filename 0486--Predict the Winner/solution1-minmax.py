class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def helper(nums, l, r):
            if l == r:
                return nums[l]

            return max(nums[l] - helper(nums, l + 1, r), nums[r] - helper(nums, l, r - 1))

        temp = helper(nums, 0, len(nums) - 1)
        if temp >= 0:
            return True
        else:
            return False