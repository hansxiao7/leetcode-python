class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {0: -1}

        total = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1
            if dict1.get(total) is not None:
                result = max(result, i - dict1[total])
            else:
                dict1[total] = i

        print(dict1)
        return result