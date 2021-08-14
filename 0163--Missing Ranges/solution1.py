class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower - 1] + nums + [upper + 1]

        result = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] or nums[i + 1] - nums[i] == 1:
                continue

            l = nums[i] + 1
            r = nums[i + 1] - 1

            if l == r:
                result.append(str(l))
            else:
                result.append(str(l) + '->' + str(r))

        return result
