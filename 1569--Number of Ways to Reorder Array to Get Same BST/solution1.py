class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (helper(nums) - 1) % (10 ** 9 + 7)


def factorial(n):
    if n == 0:
        return 1
    temp = 1
    for i in range(1, n + 1):
        temp = temp * i

    return temp


def helper(nums):
    if len(nums) == 0 or len(nums) == 1:
        return 1

    root = nums[0]
    left = [nums[i] for i in range(len(nums)) if nums[i] < root]
    right = [nums[i] for i in range(len(nums)) if nums[i] > root]
    l = len(left)
    r = len(right)

    comb = factorial(l + r) / (factorial(l) * factorial(r))

    return comb * helper(left) * helper(right)
   