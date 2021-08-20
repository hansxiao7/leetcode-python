class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # divide and conquer
        def count_element(val, left, right):
            count = 0
            for i in range(left, right + 1):
                if nums[i] == val:
                    count += 1

            return count

        def helper(left, right):
            if left < right:
                mid = (left + right) // 2

                l = helper(left, mid)
                r = helper(mid + 1, right)

                if l == r:
                    return l
                else:
                    l_count = count_element(l, left, right)
                    r_count = count_element(r, left, right)

                    if l_count >= r_count:
                        return l
                    else:
                        return r

            else:
                return nums[left]

        return helper(0, len(nums) - 1)
