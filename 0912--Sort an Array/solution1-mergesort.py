class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # quick sort
        result = merge_sort(nums, 0, len(nums) - 1)
        return result


def merge(a, b):
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    if i == len(a):
        result.extend(b[j:])

    if j == len(b):
        result.extend(a[i:])

    return result


def merge_sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2
        left_l = merge_sort(nums, left, mid)
        right_l = merge_sort(nums, mid + 1, right)
        result = merge(left_l, right_l)
    else:
        result = [nums[left]]

    return result
