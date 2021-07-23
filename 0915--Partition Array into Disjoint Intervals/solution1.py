class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        li1 = [nums[0]]
        li2 = [nums[-1]]

        for i in range(1, len(nums)):
            li1.append(max(li1[-1], nums[i]))

        for j in range(len(nums) - 2, -1, -1):
            li2.append(min(li2[-1], nums[j]))

        for k in range(len(nums) - 1):
            if li1[k] <= li2[len(nums) - 2 - k]:
                return k + 1