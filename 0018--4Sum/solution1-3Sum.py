class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = merge_sort(nums, 0, len(nums) - 1)
        result = []
        for i in range(len(nums) - 1):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            three_sum_li = three_sum(target - nums[i], nums[i + 1:])

            for j in range(len(three_sum_li)):
                three_sum_li[j].extend([nums[i]])
            result.extend(three_sum_li)

        return result


def merge(a, b):
    result = []
    i = 0
    j = 0

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


def merge_sort(li, left, right):
    if left < right:
        mid = (left + right) // 2
        left_l = merge_sort(li, left, mid)
        right_l = merge_sort(li, mid + 1, right)
        return merge(left_l, right_l)
    else:
        return [li[left]]


def three_sum(target, li):
    result = []
    for i in range(len(li)):
        left = i + 1
        right = len(li) - 1

        if i != 0 and li[i] == li[i - 1]:
            continue

        while left < right:
            if left != (i + 1) and li[left] == li[left - 1]:
                left += 1
                continue

            if right != len(li) - 1 and li[right] == li[right + 1]:
                right -= 1
                continue

            if li[left] + li[right] + li[i] > target:
                right -= 1
            elif li[left] + li[right] + li[i] < target:
                left += 1
            else:
                result.append([li[i], li[left], li[right]])
                left += 1
                right -= 1
    return result


