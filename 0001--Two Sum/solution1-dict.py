class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # build a dict
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i

        for j in range(len(nums)):
            if num_dict.get(target - nums[j]) is not None and num_dict[target - nums[j]] != j:
                return [j, num_dict[target - nums[j]]]