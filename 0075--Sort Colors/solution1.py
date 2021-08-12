class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # bucket_sort
        b = [0, 0, 0]

        for i in range(len(nums)):
            b[nums[i]] += 1

        pos = 0

        for i in range(len(nums)):
            while b[pos] == 0 and pos < 3:
                pos += 1
            nums[i] = pos
            b[pos] -= 1






