class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c1 = 0
        c2 = 0

        p1 = None
        p2 = None

        for i in range(len(nums)):
            c = nums[i]
            if c == p1:
                c1 += 1
            elif c == p2:
                c2 += 1
            elif c1 == 0:
                p1 = c
                c1 = 1
            elif c2 == 0:
                p2 = c
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        c1 = 0
        c2 = 0

        for num in nums:
            if num == p1:
                c1 += 1
            elif num == p2:
                c2 += 1

        res = []
        if c1 > len(nums) / 3.0:
            res.append(p1)

        if c2 > len(nums) / 3.0:
            res.append(p2)

        return res