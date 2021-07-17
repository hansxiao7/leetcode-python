class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        # sort the array
        nums = merge_sort(nums, 0, len(nums) - 1)

        # iterate with 2 pointers left & right
        result = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
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


def merge_sort(li, left, right):
    if left < right:
        mid = (left + right) // 2
        left_l = merge_sort(li, left, mid)
        right_l = merge_sort(li, mid + 1, right)
        return merge(left_l, right_l)
    else:
        return [li[left]]