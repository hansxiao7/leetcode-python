class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. sort -> O(nlogn)
        # 2. DFS -> O(n^3)
        # 3. hashtable

        num_set = set(nums)

        result = 0

        for i in nums:
            if i - 1 not in num_set:
                temp = 1
                curr = i

                while curr + 1 in num_set:
                    temp += 1
                    curr += 1

                result = max(result, temp)

        return result



