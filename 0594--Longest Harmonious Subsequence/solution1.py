class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        dict1 = {}

        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 0
            dict1[nums[i]] += 1

        key_li = list(dict1.keys())
        key_li.sort()

        result = 0
        for i in range(len(key_li) - 1):
            if key_li[i + 1] - key_li[i] == 1:
                result = max(result, dict1[key_li[i + 1]] + dict1[key_li[i]])

        return result