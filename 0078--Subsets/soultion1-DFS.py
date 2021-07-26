class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        li = []
        for i in range(len(nums) + 1):
            li.extend(helper(nums, 0, i))
        return li


def helper(nums, m, k):
    result = []
    if k == 0:
        result.append([])
        return result

    for i in range(m, len(nums)):
        temp2 = helper(nums, i + 1, k - 1)
        for j in range(len(temp2)):
            temp1 = [nums[i]]
            temp1.extend(temp2[j])
            result.append(temp1)
    return result