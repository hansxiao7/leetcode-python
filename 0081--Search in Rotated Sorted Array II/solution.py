class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        p = find_pivot(nums, 0, len(nums) - 1)

        if p == -1:
            return binary_search(nums, target, 0, len(nums) - 1)

        if target > nums[-1]:
            return binary_search(nums, target, 0, p - 1)
        else:
            return binary_search(nums, target, p, len(nums) - 1)


def binary_search(nums, target, left, right):
    if left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            return binary_search(nums, target, left, mid)
        elif nums[mid] < target:
            return binary_search(nums, target, mid + 1, right)
        else:
            return True
    else:
        if nums[left] == target:
            return True
        else:
            return False


def find_pivot(nums, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < nums[left]:
            p = find_pivot(nums, left, mid)
        elif nums[mid] > nums[right]:
            p = find_pivot(nums, mid, right)

        else:
            p_1 = find_pivot(nums, left, mid)
            p_2 = find_pivot(nums, mid, right)
            p = max(p_1, p_2)
    elif left + 1 == right:
        if nums[left] > nums[right]:
            return right
        else:
            return -1
    else:
        return -1

    return p