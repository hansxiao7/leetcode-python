class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-sys.maxint] + nums + [-sys.maxint]

        def binary_search(left, right):
            if left < right:
                mid = (left + right) // 2
                if nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                    return binary_search(mid + 1, right)
                elif nums[mid - 1] > nums[mid] and nums[mid] > nums[mid + 1]:
                    return binary_search(left, mid)
                elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    return binary_search(mid + 1, right)

            else:
                return left

        return binary_search(1, len(nums) - 2) - 1
