class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        self.result = 0

        def helper(nums, visited, curr_val):
            if len(visited) == len(nums):
                self.result = max(self.result, curr_val)
                return
            n = len(nums)
            for i in range(n):
                if i not in visited:
                    visited.add(i)

                    left = i - 1
                    right = i + 1

                    while left in visited:
                        left -= 1

                    if left < 0:
                        left_val = 1
                    else:
                        left_val = nums[left]

                    while right in visited:
                        right += 1

                    if right >= len(nums):
                        right_val = 1
                    else:
                        right_val = nums[right]

                    helper(nums, visited, curr_val + left_val * nums[i] * right_val)

                    visited.remove(i)

        helper(nums, visited, 0)
        return self.result