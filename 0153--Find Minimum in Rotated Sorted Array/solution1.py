class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binary_search(left, right):
            if left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] > nums[left] and nums[mid] > nums[right]:
                    if nums[left] > nums[right]:
                        return binary_search(mid + 1, right)
                    else:
                        return binary_search(left, mid)
                elif nums[mid] < nums[left] and nums[mid] < nums[right]:
                    if nums[left] < nums[right]:
                        return binary_search(mid + 1, right)
                    else:
                        return binary_search(left, mid)
                else:
                    if nums[left] < nums[right]:
                        return binary_search(left, mid)
                    else:
                        return binary_search(mid + 1, right)
            else:
                return min(nums[left], nums[right])

        return binary_search(0, len(nums) - 1)