class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = merge_sort(nums, 0, len(nums) - 1)
        result = []

        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(len(nums) - 1, i + 2, -1):
                if j != len(nums) - 1 and nums[j] == nums[j + 1]:
                    continue

                curr_sum = nums[i] + nums[j]

                two_sum_li = two_sum(target - curr_sum, nums[i + 1:j])

                if len(two_sum_li) != 0:
                    for k in two_sum_li:
                        k.extend([nums[i], nums[j]])
                result.extend(two_sum_li)

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


def two_sum(target, li):
    left = 0
    right = len(li) - 1
    result = []

    while left < right:
        if left != 0 and li[left - 1] == li[left]:
            left += 1
            continue

        if right != len(li) - 1 and li[right] == li[right] + 1:
            right += 1
            continue

        if li[left] + li[right] < target:
            left += 1
        elif li[left] + li[right] > target:
            right -= 1
        else:
            result.append([li[left], li[right]])
            left += 1
            right -= 1

    return result

