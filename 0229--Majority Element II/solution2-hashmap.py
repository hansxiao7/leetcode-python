class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        result = []
        for key in counts.keys():
            if counts[key] > len(nums) // 3:
                result.append(key)

        return result