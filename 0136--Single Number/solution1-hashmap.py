class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1

        for j in dict1.keys():
            if dict1[j] == 1:
                return j