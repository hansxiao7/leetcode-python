class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = list(nums)
        temp.sort()

        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            left = mid - 1
            right = len(nums) - 1
        else:
            left = mid
            right = len(nums) - 1

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = temp[left]
                left -= 1
            else:
                nums[i] = temp[right]
                right -= 1

