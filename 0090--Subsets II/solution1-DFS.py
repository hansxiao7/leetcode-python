class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(0, len(nums) + 1):
            result.extend(helper(nums, 0, i))

        return result


def helper(nums, m, k):
    result = []
    if k == 0:
        result.append([])
        return result

    for i in range(m, len(nums) - k + 1):
        if i != m and nums[i - 1] == nums[i]:
            continue
        temp = helper(nums, i + 1, k - 1)
        for j in range(len(temp)):
            temp2 = [nums[i]]
            temp2.extend(temp[j])
            result.append(temp2)

    return result
