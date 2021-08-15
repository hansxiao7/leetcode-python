class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = list(nums)
        temp.sort()

        left = 0
        right = len(nums) - 1

        flag = True

        for i in range(len(nums)):
            if flag:
                nums[i] = temp[left]
                left += 1
            else:
                nums[i] = temp[right]
                right -= 1

            flag = not flag

        return nums