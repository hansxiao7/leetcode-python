class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        counts = 1

        for i in range(1, len(nums)):
            if counts == 0:
                candidate = nums[i]

            if nums[i] == candidate:
                counts += 1
            else:
                counts -= 1

        return candidate