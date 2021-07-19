class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(1, len(nums) + 1):
            dict1[i] = 0

        for j in range(len(nums)):
            dict1[nums[j]] += 1

        result = []
        for k in dict1.keys():
            if dict1[k] == 0:
                result.append(k)

        return result