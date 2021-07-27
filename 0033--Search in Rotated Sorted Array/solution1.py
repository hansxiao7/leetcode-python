class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
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
            result = binary_search(nums, target, left, mid)
        elif nums[mid] < target:
            result = binary_search(nums, target, mid + 1, right)
        else:
            result = mid
    else:
        if nums[left] == target:
            return left
        else:
            return -1

    return result


def find_pivot(nums, left, right):
    if left + 1 < right:
        mid = (left + right) // 2

        if nums[left] > nums[mid]:
            p = find_pivot(nums, left, mid)
        elif nums[right] < nums[mid]:
            p = find_pivot(nums, mid, right)
        else:
            p_1 = find_pivot(nums, left, mid - 1)
            p_2 = find_pivot(nums, mid + 1, right)
            p = max(p_1, p_2)

    elif left + 1 == right:
        if nums[right] > nums[left]:
            return -1
        else:
            return right
    else:
        return -1

    return p