class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}

        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = []

            dict1[nums[i]].append(i)

        key_li = list(dict1.keys())
        key_li.sort()

        min_id = [len(nums)]
        for key in key_li:
            min_id.append(min(min(dict1[key]), min_id[-1]))

        max_id = [-1]
        for key in key_li:
            max_id.append(max(dict1[key]))

        result = 0
        for i in range(1, len(max_id)):
            result = max(result, max_id[i] - min_id[i])

        return result