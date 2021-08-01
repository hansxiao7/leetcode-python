class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        pos = set()

        helper(pos, result, nums, len(nums), [])

        return result


def helper(pos, result, nums, k, temp):
    if k == 0:
        result.append(temp)
        return

    for i in range(len(nums)):
        if i in pos:
            continue
        pos.add(i)
        helper(pos, result, nums, k - 1, temp + [nums[i]])
        pos.remove(i)



