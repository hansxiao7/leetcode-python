class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = True

        for i in range(len(nums) - 1):
            if nums[i + 1] >= nums[i]:
                continue
            else:
                if flag:
                    if i == 0:
                        nums[i] = nums[i + 1]
                    else:
                        if nums[i + 1] >= nums[i - 1]:
                            nums[i] = nums[i - 1]
                        else:
                            nums[i + 1] = nums[i]
                    flag = not flag
                else:
                    return False

        return True