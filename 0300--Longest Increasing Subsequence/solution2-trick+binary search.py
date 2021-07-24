class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []

        for i in nums:
            if len(result) == 0 or i > result[-1]:
                result.append(i)

            else:
                pos = binary_search(result, 0, len(result) - 1, i)
                result[pos] = i

        return len(result)


def binary_search(li, left, right, target):
    if left < right:
        mid = (left + right) // 2
        if target > li[mid]:
            return binary_search(li, mid + 1, right, target)
        elif target < li[mid]:
            return binary_search(li, left, mid, target)
        else:
            return mid
    else:
        return left