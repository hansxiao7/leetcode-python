class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        m = len(nums)
        cache = {}

        def helper(curr, remaining, visited):
            if remaining == 0:
                return True

            if (curr, remaining, visited) in cache:
                return cache[(curr, remaining, visited)]

            res = False
            for i in range(len(nums)):
                if visited & 1 << i == 0:
                    if curr + nums[i] > target:
                        continue
                    visited |= 1 << i
                    if curr + nums[i] < target:
                        res = res or helper(curr + nums[i], remaining, visited)
                    elif curr + nums[i] == target:
                        res = res or helper(0, remaining - 1, visited)
                    visited -= 1 << i
            cache[(curr, remaining, visited)] = res
            return res

        return helper(0, k, 0)

